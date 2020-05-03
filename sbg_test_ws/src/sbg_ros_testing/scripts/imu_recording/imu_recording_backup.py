# imu_data_reader.py
import os
import numpy as np
from data_alignment import closest_index, interpolate_linear, interpolate_linear_angle, convert_angle_in_range
from copy import deepcopy
import argparse
import utm

class ImuRecording(object):

	# Pre-defined data keys that will be tried to be set from the raw data in a read_ascii() call
	# TODO: not sure if all of these units are correct
	PROCESSED_DATA_KEYS = ("time", 	# UTC time in seconds
						   "gps_long",
						   "gps_lat",
						   "long", 	# degrees
						   "lat",  	# degrees
						   "pos_x",
						   "pos_y",
						   "vel_x",	# m/s
						   "vel_y",	# m/s
						   "vel_z",	# m/s
						   "roll",	# radians
						   "pitch", # radians
						   "yaw",	# radians
						   "acc_x", # m/s^2
						   "acc_y", # m/s^2
						   "acc_z", # m/s^2
						   "gyr_x", # radians/s
						   "gyr_y", # radians/s
						   "gyr_z") # radians/s
	

	N_INSTANCES = 0

	def __init__(self, name=None, files_dir=""):
		if name: 
			self.name = name
		else: 
			self.name = "{}{}".format(self.__class__.__name__, self.__class__.N_INSTANCES)
			# incerement N_INSTANCES to have unique names for multiple instances 
			self.__class__.N_INSTANCES += 1 

		self.files_dir = files_dir
		self.ascii_data_keys = []
		self.ascii_data = {}
		self.processed_data = {key: [] for key in self.PROCESSED_DATA_KEYS}

	def __getattr__(self, attr):
		"""
		Convenient way to access the processed data
		Remove this functionality (unintuitive)?
		"""
		
		if attr not in self.PROCESSED_DATA_KEYS:
			raise Exception("'{}' is not an attribute. Check the ImuRecording.PROCESSED_DATA_KEYS for which attributes are valid.".format(attr))
		return self.processed_data[attr]


	def __setattr__(self, attr, val):
		"""
		Convenient way to set the processed data
		Remove this functionality (unintuitive)?
		"""
		if attr in self.PROCESSED_DATA_KEYS:
			if not isinstance(val, list):
				raise Exception("Value for attribute '{}' should be a list, not '{}'".format(val, val.__class__))
			self.processed_data[attr] = val
		else:
			self.__dict__[attr] = val
			
	def __eq__(self, other):
		for k in self.processed_data:
			if self.processed_data[k] != other.processed_data[k]:
				return False
		return True

	def reset(self):
		"""
		Resets all data. We use deepcopy to get new instances of the list.
		"""
		self.ascii_data_keys = []
		self.ascii_data = {}
		self.processed_data = {key: [] for key in self.PROCESSED_DATA_KEYS}
		

	def set_read_dir(self, files_dir):
		"""
		Set the directory path which will be inserted before relative file paths when calling the read() method.
		This is more of a convenience functionality to be able to read multiple files in a dictionary by just passing the relative filename as 
		an argument to file_path in read(). 
		"""
		self.files_dir = files_dir
		
	def read(self, file_path, delimiter="\t", save_processed_data=False, debug=False):
		"""
		Reads .processed or ascii file. If the extension of the file_path is .processed, 
		read_processed_data will be called. Any other extension is assumed to be an ascii file and 
		read_ascii will be called.
		delimiter: data separator in the file
		save_processed_data: if True, save .processed file after reading
		debug: saves ignored lines returned from read_ascii in a log file. Useful to see if 
			   reading is done correctly
		"""
		self.reset()
		
		if not os.path.isabs(file_path):
			file_path = os.path.join(self.files_dir, file_path)
		# Read processed data file
		ext = os.path.splitext(file_path)[1]
		if ext == ".processed":
			self.read_processed_data(file_path)
			ignored_lines = []
			print("Read processed data from '{}'".format(file_path))
		else:
			# Read ascii data file
			# Each sub-class needs to define a read_ascii method which takes 
			# a file path and a delimiter as paramters and returns a list 
			# with all lines that has been ignored
			
			try:
				ignored_lines = self.read_ascii(file_path, delimiter) 
			except KeyError as e:
				print(e)
				raise KeyError("A key error occured during reading, is the delimiter set correctly? (check the printed ascii_data_key if they look reasonable)") 
			else:
				print("Read ASCII data from '{}'".format(file_path))

		if save_processed_data: self.save_processed_data(file_path, delimiter)
		if debug: self.log_ignored_data(ignored_lines)


	def read_ascii(self, file_path, delimiter):
		raise Exception("The base class '{}' can't read ASCII files. Instanciate the proper sub-class to read ASCII files.")


	def read_data_type_line(self, line, delimiter):
		"""
		Reads line 
		"""
		line_ls = [s.strip() for s in line.split(delimiter)]
		for d in line_ls:
			self.ascii_data_keys.append(d)
			self.ascii_data[d] = []


	def read_data_line(self, line, delimiter):
		values = []
		for s in line.split(delimiter):		
			s = s.strip()
			try:
				val = float(s)
			except ValueError:
				val = s
			values.append(val)
			
		for k, v in zip(self.ascii_data_keys, values):
			self.ascii_data[k].append(v)


	def log_ignored_data(self, ignored_lines):
		name = str(self.NAME) + "_ignored_data.txt"
		with open(name, "w") as f:
			f.write("Ignored lines\n")
			f.writelines(ignored_lines)

	def read_processed_data(self, file_path, delimiter="\t"):
		self.reset()
		assert os.path.splitext(file_path)[1] == ".processed", "Extension has to be '.processed'"

		with open(file_path, "r") as f:
			read_keys = True
			keys = ()
			for line in f:
				if read_keys:
					keys = tuple([k.strip() for k in line.split(delimiter)])
					assert keys == self.PROCESSED_DATA_KEYS, "Invalid .processed file. {} != {}".format(keys, self.PROCESSED_DATA_KEYS)
					read_keys = False
				else:
					vals = [val.strip() for val in line.split(delimiter)]
					for k, val in zip(self.PROCESSED_DATA_KEYS, vals):
						try:
							val = float(val)
						except ValueError:
							# ignore non float values
							pass
						else:
							self.processed_data[k].append(val)

	def save(self, file_path, delimiter="\t"):
		"""
		Saves the data in self.processed_data in file defined by file_path (replaces given extension with .processed)
		"""
		#path, ext = os.path.splitext(file_path)
		file_path = os.path.splitext(file_path)[0] + ".processed"
		file_path = os.path.join(self.files_dir, file_path)
		
		# verify that the length of all data is equal
		len_set = set([len(self.processed_data[k]) for k in self.PROCESSED_DATA_KEYS])
		if len(len_set) == 2:
			assert 0 in len_set, "The stored data do not have the same lengths."
		else:
			assert len(len_set) == 1, "The stored data do not have the same lengths."

		with open(file_path, "w") as f:
			f.write(delimiter.join(self.PROCESSED_DATA_KEYS) + "\n")
			
			for i in range(len(self.time)):
				line = []
				
				for k in self.PROCESSED_DATA_KEYS:
					try:
						line.append(str(self.processed_data[k][i]))
					except IndexError:
						line.append("N/A")

				#print(delimiter.join(line))
				f.write(delimiter.join(line) + "\n")
		print("Wrote processed data to '{}'".format(file_path))

	def copy(self):
		imu = self.__class__()
		imu.processed_data = deepcopy(self.processed_data)
		imu.ascii_data = deepcopy(self.ascii_data)
		imu.ascii_data_keys = deepcopy(self.ascii_data_keys)
		return imu

	def latlon_to_pos(self):
		x0, y0, zone_nr, _ = utm.from_latlon(self.lat[0], self.long[0])
		x_pos = []
		y_pos = []
		for lat, lon in zip(self.lat, self.long):
			x, y, _, _ = utm.from_latlon(lat, lon, force_zone_number=zone_nr)
			x_pos.append(x-x0)
			y_pos.append(y-y0)
		return x_pos, y_pos

	def gps_outages(self):
		"""Returns 
		"""

	def deg_to_rad(self, *keys):
		"""
		Converts the data for given key in processed_data from degrees to radians
		"""
		for key in keys:
			self.processed_data[key] = list(np.array(self.processed_data[key])/180*np.pi)

	def rad_to_deg(self, *keys):
		"""
		Converts the data for given key in processed_data from radians to degrees
		"""
		for key in keys:
			self.processed_data[key] = list(np.array(self.processed_data[key])/np.pi*180)			

	def time_index(self, time):
		"""
		Returns index of the closest time lower than time. 
		"""
		return closest_index(self.time, time)


	def add_data(self, key, val, time=None):
		l = len(self.processed_data["time"])
		if l > 0:
			
			if time is None or time == self.time[-1]:
				assert len(self.processed_data[key]) == l, "Data has different length from time data"
				self.processed_data[key][-1] = val
				return

			assert time > self.time[-1], "Time is earlier than the latest recorded time"

		assert time >= 0, "Time has to be positive"
		assert key != "time", "time should not be changed like this."
		assert key in self.PROCESSED_DATA_KEYS, "'{}' is not a valid data key.".format(key)
		
		self.processed_data["time"].append(time)

		for k in self.PROCESSED_DATA_KEYS:
			if k == "time": continue
			data = self.processed_data[k]
			assert len(data) == l, "Data has different length from time data"

			if k == key:
				data.append(val)
			elif k == "time":
				data.append(time)
			else:
				if l == 0:
					data.append(0) # adding a zero for all other values
				else:
					data.append(data[-1])

	def time_with_freq(self, freq):
		"""
		Returns a list of discrete time with specified frequency in the interval of 
		this recordings current time
		"""
		assert len(self.time) > 1, "Not enough time values, need at least 2"
		start = self.time[0]
		end = self.time[-1]
		n_samples = float(end-start)*freq + 1
		return np.linspace(start, end, n_samples).tolist()

	def align_freq(self, freq):
		t = self.time_with_freq(freq)
		self.align_data(t)

	def align_data(self, aligned_time, keys=None):
		# TODO: reset all values that are not aligned?
		if keys is None: 
			keys = self.processed_data.keys()
			keys.pop(keys.index("time")) # time should not be included
		else:
			for k in keys:
				assert k in self.PROCESSED_DATA_KEYS, "'{}' is not a valid key".format(k)
				assert k != "time", "time should not be a key"

		max_idx = len(self.processed_data["time"])-1
		for key in self.PROCESSED_DATA_KEYS:
			if key == "time" or len(self.processed_data[key]) == 0:
				continue
			if key not in keys: 
				self.processed_data[key] = []
				continue

			aligned_data = []
			for t in aligned_time:

				# Find the previous value
				prev_index = closest_index(self.processed_data["time"], t)
				prev_time = self.processed_data["time"][prev_index]
				try:
					prev_val = self.processed_data[key][prev_index]
				except:
					print(key)
					raise Exception()
				if prev_index == max_idx:
					aligned_data.append(prev_val)
					break
				# Find the next value
				next_index = prev_index + 1
				next_time = self.processed_data["time"][next_index]
				next_val = self.processed_data[key][next_index]
	
				# Interpolate the value to requested time t
				if key in ["roll", "pitch", "yaw"]:
					# assuming radians
					interpolated_val = interpolate_linear_angle(prev_val, next_val, prev_time, next_time, t, np.pi, -np.pi)
				elif key in ["lat", "long"]:
					# assuming degrees
					interpolated_val = interpolate_linear_angle(prev_val, next_val, prev_time, next_time, t, 180, -180)
				else:
					interpolated_val = interpolate_linear(prev_val, next_val, prev_time, next_time, t)
				
				aligned_data.append(interpolated_val)
				
			self.processed_data[key] = aligned_data
		self.processed_data["time"] = [t for t in aligned_time]

	def is_aligned_with(self, imu):
		return all([t1 == t2 for t1,t2 in zip(self.time, imu.time)])

	""" Some methods with implementations refactored elsewhere"""

	def to_rosbag(self, file_path,
				  gps_topic="gps", gps_frame="gps_frame",
				  imu_topic="imu", imu_frame="imu_base_link",
				  wheel_topic="wheel_odom", wheel_frame="wheel_odom", wheel_child_frame="rear_axle",
				  odometry_topic="odometry", odometry_frame="map", odometry_child_frame="base_link"):

		from recording_to_rosbag import RecordingToBag
		file_path = os.path.splitext(file_path)[0] + ".bag"
		file_path = os.path.join(self.files_dir, file_path)
		bagger = RecordingToBag(self,
								gps_topic=gps_topic, gps_frame=gps_frame,
				 	  		 	imu_topic=imu_topic, imu_frame=imu_frame,
				 	  		 	wheel_topic=wheel_topic, wheel_frame=wheel_frame, 
							 	wheel_child_frame=wheel_child_frame,
				 	  		 	odometry_topic=odometry_topic, odometry_frame=odometry_frame, 
							 	odometry_child_frame=odometry_child_frame)
		bagger.create_rosbag(file_path)
		print("Wrote data to rosbag '{}'".format(file_path))
		
	def plot_all(self):
		from imu_plotter import ImuPlotter
		plotter = ImuPlotter([self])
		plotter.plot_all()
		plotter.show()

class XsensRecording(ImuRecording):
	DELIMITER = "\t"
	NAME = "Xsens"
		
	def read_ascii(self, file_path, delimiter):
		ignored_lines = []
		read_data = False
		
		with open(file_path, "r") as f:
			for line in f:
				if "PacketCounter" in line:
					self.read_data_type_line(line, delimiter)
					read_data = True
				elif read_data is True:
					self.read_data_line(line, delimiter)
				else:
					ignored_lines.append(line)
					
		self._process_data(self.ascii_data)
		return ignored_lines

	def _process_data(self, data):
		data = data.copy()
		self.time = self._utc_to_sec(data)
		#self.acc_x = self.data["Acc_X"]
		#self.acc_y = self.data["Acc_Y"]
		#self.acc_z = self.data["Acc_Z"]
		#self.gyr_x = self.data["Gyr_X"]
		#self.gyr_y = self.data["Gyr_Y"]
		#self.gyr_z = self.data["Gyr_Z"]
		#self.vel_inc_x = self.data["VelInc_X"]
		#self.vel_inc_y = self.data["VelInc_Y"]
		#self.vel_inc_z = self.data["VelInc_Z"]
		self.processed_data["vel_x"] = data["Vel_X"]#self._velocity_converter()#
		self.processed_data["vel_y"] = data["Vel_Y"]
		#self.vel_z = self.data["Vel_Z"]
		#self.roll = self.data["Roll"]
		#self.pitch = self.data["Pitch"]
		self.processed_data["yaw"] = [convert_angle_in_range(180, -180, a) for a in list(-np.array(data["Yaw"]) + 90)]
		self.processed_data["long"] = data["Longitude"]
		self.processed_data["lat"] = data["Latitude"]
		(self.processed_data["pos_x"], 
		 self.processed_data["pos_y"]) = self.latlon_to_pos(self.processed_data["lat"],
		 													 self.processed_data["long"])

	def _utc_to_sec(self, data):
		#print("Converting UTC Time to sec")
		sec_values = [] # Init new list
		for i in range(len(data["UTC_Minute"])):
			hour = data["UTC_Hour"][i]
			minute = data["UTC_Minute"][i]
			second = data["UTC_Second"][i]
			mili = data["UTC_Nano"][i]/1000000000.0

			sec_values.append(60*60*hour+60*minute+second+mili)
		return sec_values

	def _velocity_converter(self):
		pass


		
class VBOXRecording(ImuRecording):
		
	def read_ascii(self, file_path, delimiter=" "):
		ignored_lines = []
		with open(file_path, "r") as f:
			
			read_data_types = False
			read_data = False
			
			for line in f:
				if "[column names]" in line:
					read_data_types = True
					
				elif "[data]" in line:
					read_data = True
					
				elif read_data_types is True:
					read_data_types = False
					self.read_data_type_line(line, delimiter)
					
				elif read_data is True:
					self.read_data_line(line, delimiter)
				else:
					#print("Ignoring '{}'".format(line))
					ignored_lines.append(line)
					
		self._process_data(self.ascii_data)	
		return ignored_lines

	def _process_data(self, data):
		# TODO: units not used atm
		data = data.copy()
		self.processed_data["time"] = self._utc_to_sec(data)
		#self.processed_data["gps_long"] = data["Lon"]
		#self.processed_data["gps_lat"] = data["Lat"]
		self.processed_data["long"] = [-v/60 for v in data["long"]] # minutes to degrees
		self.processed_data["lat"] = [v/60 for v in data["lat"]]  # minutes to degrees
		(self.processed_data["pos_x"], 
		 self.processed_data["pos_y"]) = self.latlon_to_pos(self.processed_data["lat"],
		 													 self.processed_data["long"])
		self.processed_data["vel_x"] = data["velocity"]
		self.processed_data["vel_y"] = [-v for v in data["vert-vel"]]
		self.processed_data["vel_z"] = data["vert-vel"]
		#self.processed_data["vel_z"] = data["Z Velocity"]
		#self.processed_data["roll"] = data["Roll"]
		#self.processed_data["pitch"] = data["Pitch"]
		self.processed_data["yaw"] = data["heading"]#["heading"]
		#self.processed_data["acc_x"] = data["Accelerometer X"]
		#self.processed_data["acc_y"] = data["Accelerometer Y"]
		#self.processed_data["acc_z"] = data["Accelerometer Z"]
		#self.processed_data["gyr_x"] = data["Gyroscope X"]
		#self.processed_data["gyr_y"] = data["Gyroscope Y"]
		#self.processed_data["gyr_z"] = data["Gyroscope Z"]

	def _utc_to_sec(self, data):
		#print("Converting UTC Time to sec")
		sec_values = [] # Init new list
		for t in data["time"]:
			t_str = str(t)
			hour = float(t_str[0:2])
			minute = float(t_str[2:4])
			sec = float(t_str[4:])
			sec_values.append(60*60*hour+60*minute+sec)
		return sec_values

		
class SBGRecording(ImuRecording):

	def read_ascii(self, file_path, delimiter):
		ignored_lines = []
		with open(file_path, "r") as f:
			for i, line in enumerate(f):
				if i == 0:
					self.read_data_type_line(line, delimiter)
				elif i == 1:
					#ignored_lines.append(line)
					units = line.split(delimiter)
				else:
					self.read_data_line(line, delimiter)
		
		self._process_data(self.ascii_data, units)
		return ignored_lines


	def _process_data(self, data, units):
		# TODO: units not used atm
		data = data.copy()
		self.processed_data["time"] = self._utc_to_sec(data)
		#self.processed_data["gps_long"] = data["Lon"]
		#self.processed_data["gps_lat"] = data["Lat"]
		self.processed_data["long"] = data["Longitude"]
		self.processed_data["lat"] = data["Latitude"]
		(self.processed_data["pos_x"], 
		 self.processed_data["pos_y"]) = self.latlon_to_pos(self.processed_data["lat"],
		 													 self.processed_data["long"])
		self.processed_data["vel_x"] = data["X Velocity"]
		self.processed_data["vel_y"] = data["Y Velocity"]
		self.processed_data["vel_z"] = data["Z Velocity"]
		self.processed_data["roll"] = data["Roll"]
		self.processed_data["pitch"] = data["Pitch"]
		self.processed_data["yaw"] = data["Yaw"]
		self.processed_data["acc_x"] = data["Accelerometer X"]
		self.processed_data["acc_y"] = data["Accelerometer Y"]
		self.processed_data["acc_z"] = data["Accelerometer Z"]
		self.processed_data["gyr_x"] = data["Gyroscope X"]
		self.processed_data["gyr_y"] = data["Gyroscope Y"]
		self.processed_data["gyr_z"] = data["Gyroscope Z"]

		# convert long/lat data to degrees
		#for k1, k2 in zip(["Longitude", "Latitude"], ["long", "lat"]):
		#	if not "\xc2" in units[self.ascii_data_keys.index(k1)]:
		#		print("hurraaa")
		#		self.rad_to_deg(k2)

		#for k1, k2 in zip(["Roll", "Pitch", "Yaw"], ["roll", "pitch", "yaw"]):
		#	if "\xc2" in units[self.ascii_data_keys.index(k1)]:
		#		self.deg_to_rad(k2)

		#print("Processed ASCII data!")


	def _utc_to_sec(self, data):
		sec_values = [] # Init new list
		for t in data["UTC Time"]:
			hour_min_sec = t.split(":")
			sec_values.append(60*60*float(hour_min_sec[0])+60*float(hour_min_sec[1])+float(hour_min_sec[2]))
		return sec_values

if __name__ == "__main__":
	from imu_plotter import ImuPlotter
	imu = ImuRecording()
	imu.read("SBG_general_000.processed")

	print(len(imu.time))
	imu.align_freq(0.1)
	print(len(imu.time))
	plotter = ImuPlotter(imu)
	plotter.plot_all()
	plotter.show()
	print(dir(imu))
	
	

if __name__ == "__main__e":
	reader_classes = ImuRecording.__subclasses__()
	reader_classes.append(ImuRecording)
	reader_names = [cls.__name__ for cls in reader_classes]
	parser = argparse.ArgumentParser(description="Converts an IMU ASCII recording to a .processed file.")
	parser.add_argument('reader', type=str, choices=reader_names, help="The class which will be used for reading the file.")
	parser.add_argument('file', type=str, help="ASCII file recording containing the recorded IMU values.")
	parser.add_argument("-d", '--delimiter', default="t", choices=["t", "s", ""], type=str, help="Delimiter used in the recording.")
	args = parser.parse_args()

	if args.delimiter == "t": args.delimiter = "\t"
	if args.delimiter == "s": args.delimiter = " "
	if args.delimiter == "": args.delimiter = None

	try:
		reader_idx = reader_names.index(args.reader)
	except ValueError:
		print("Reader '{}' does not exist. Choose from: {}".format(args.reader, reader_names))
	else:
		imu_reader = reader_classes[reader_idx]()

	imu_reader.read(args.file, delimiter=args.delimiter)
	imu_reader.save(args.file)