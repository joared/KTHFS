# imu_data_reader.py
import os
import numpy as np
from data_alignment import closest_index, interpolate_linear, interpolate_linear_angle
from copy import deepcopy
import argparse
import utm

class ImuRecording(object):
	"""
	TODO: names like processed and raw are a bit inconsistent, maybe change that
	Base class for IMU readers that read IMU data from a generated ASCII file. 
	This class should not be instanciated. 
	Create sub-classes that inherit this class. The sub-class should define:

	read_ascii(self, file_path, delimiter): Reads the lines in the ASCII file and 
										    puts the data in the .ascii_data dictionary. 
										    Should return a list of ignored lines for debugging.

	General:

	Only difference between read and read_ascii is that ignored lines are being logged in a file in read while
	read_ascii is actually reading the 

	The methods 'read_data_type_line' and 'read_data_line' are helping methods that can be used in read_ascii.
	For example the ASCII formats from SBG, Xsens and VBOX are similar and data can be read in a similar way
	using these helping methods.

	Using the align_data method, aligns the data in processed_data to a specific time alignment and also sets the
	'time' key in processed_data to that time. This can be useful when multiple IMUs have different time alignments
	and a comparision wants to be made between them. Linear interpolation is used to adjust the values.
	This aligned time can be retrieved by using the align_time function in the data_alignment module.
	"""

	# Pre-defined data keys that will be tried to be set from the raw data in a read_ascii() call
	# TODO: not sure if all of these units are correct
	PROCESSED_DATA_KEYS = ["time", 	# UTC time in seconds
						   "gps_long",
						   "gps_lat",
						   "long", 	# degrees
						   "lat",  	# degrees
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
						   "gyr_z"] # radians/s
	
	# This class attribute is used to initialize the .processed_data 
	# attribute of instances of this class by copying this dict
	PROCESSED_DATA_DEFAULT = {}
	for k in PROCESSED_DATA_KEYS:
		PROCESSED_DATA_DEFAULT[k] = []


	def __init__(self, files_dir=""):
		self.files_dir = files_dir
		self.ascii_data_keys = [] # data types in order presented in ascii file
		self.ascii_data = {} 		# ascii file data
		self.processed_data = deepcopy(self.PROCESSED_DATA_DEFAULT) # data processed from ascii file

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
			
	
	def reset(self):
		self.ascii_data_keys = []
		self.ascii_data = {}
		self.processed_data = deepcopy(self.PROCESSED_DATA_DEFAULT)
		

	def set_read_dir(self, files_dir):
		"""
		Set the directory path which will be inserted before relative file paths when calling the read() method.
		This is more of a convenience functionality to be able to read multiple files in a dictionary by just passing the relative filename as 
		an argument to file_path in read(). 
		"""
		self.files_dir = files_dir
		
		
	def read(self, file_path, delimiter="\t", save=False, debug=False):
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

		if save: self.save_processed_data(file_path, delimiter)
		if debug: self.log_ignored_data(ignored_lines)


	def read_ascii(self, file_path, delimiter):
		raise Exception("The base class '{}' can't read ASCII files. Instanciate the proper sub-class to read ASCII files.")


	def read_data_type_line(self, line, delimiter=None):
		line_ls = [s.strip() for s in line.split(delimiter)]
		for d in line_ls:
			self.ascii_data_keys.append(d)
			self.ascii_data[d] = []
			#print("'" + d + "'")
		#print("Data types registered!")


	def read_data_line(self, line, delimiter=None):
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

	def read_processed_data(self, file_path, delimiter=None):
		self.reset()
		assert os.path.splitext(file_path)[1] == ".processed", "Extension has to be '.processed'"
		if delimiter is None: delimiter = "\t"

		with open(file_path, "r") as f:
			read_keys = True
			for line in f:
				if read_keys:
					keys = [k.strip() for k in line.split(delimiter)]
					assert keys == self.PROCESSED_DATA_KEYS, "Invalid .processed file. {} != {}".format(keys, self.PROCESSED_DATA_KEYS)
					read_keys = False
				else:
					vals = [val.strip() for val in line.split(delimiter)]
					for k, val in zip(self.PROCESSED_DATA_KEYS, vals):
						try:
							val = float(val)
						except ValueError:
							pass
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

	def pos(self, i=None):
		if not i: i = len(self.time)
		x0, y0, zone_nr, _ = utm.from_latlon(self.lat[0], self.long[0])

		x_pos = []
		y_pos = []
		for lat, lon in zip(self.lat[:i], self.long[:i]):
			x, y, _, _ = utm.from_latlon(lat, lon, force_zone_number=zone_nr)
			x_pos.append(x-x0)
			y_pos.append(y-y0)
		return x_pos, y_pos

	def gps_out(self):
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
			keys = deepcopy(self.PROCESSED_DATA_KEYS)
			keys.pop(keys.index("time")) # time should not be included
		else:
			for k in keys:
				assert k in self.PROCESSED_DATA_KEYS, "'{}' is not a valid key".format(k)
				assert k != "time", "time should not be a key"

		max_idx = len(self.processed_data["time"])-1
		for key in keys:
			aligned_data = []
			for t in aligned_time:

				# Find the previous value
				prev_index = closest_index(self.processed_data["time"], t)
				
				prev_time = self.processed_data["time"][prev_index]
				prev_val = self.processed_data[key][prev_index]
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
		plotter = ImuPlotter(self)
		plotter.plot_all()
		plotter.show()

class VBOXReader(ImuRecording):
	NAME = "VBOX"
	

class XsensReader(ImuRecording):
	NAME = "Xsens"

		
class SBGRecording(ImuRecording):
	N = 0 # Number of times this class has been instanciated ('_N' will be appended to self.name)
	NAME = "SBG"

	def __init__(self, files_dir=""):
		ImuRecording.__init__(self, files_dir)
		self.name = "{}_{}".format(self.NAME, self.N)
		self.__class__.N += 1 # incerement N to have unique names for multiple instances 


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
		self.processed_data["gps_long"] = data["Lon"]
		self.processed_data["gps_lat"] = data["Lat"]
		self.processed_data["long"] = data["Longitude"]
		self.processed_data["lat"] = data["Latitude"]
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