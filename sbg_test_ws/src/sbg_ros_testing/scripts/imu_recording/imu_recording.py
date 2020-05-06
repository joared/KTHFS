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
						   "gps_long", # degrees
						   "gps_lat",  # degrees
						   "pos_x", # m
						   "pos_y", # m
						   "vel_x",	# m/s
						   "vel_y",	# m/s
						   "vel_z",	# m/s
						   "roll",	# degrees
						   "pitch", # degrees
						   "yaw",	# degrees
						   "acc_x", # m/s^2
						   "acc_y", # m/s^2
						   "acc_z", # m/s^2
						   "gyr_x", # degrees/s
						   "gyr_y", # degrees/s
						   "gyr_z") # degrees/s
	

	N_INSTANCES = 0

	def __init__(self, name=None, files_dir=""):
		if name: 
			self.name = name
		else: 
			self.name = "IMU_{}".format(self.__class__.N_INSTANCES)
			# incerement N_INSTANCES to have unique names for multiple instances 
			self.__class__.N_INSTANCES += 1 

		self.files_dir = files_dir
		self.processed_data = {key: [] for key in self.PROCESSED_DATA_KEYS}
		self.epsilon = 1e-9 # abs values below this are considered to be zero

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
			
	def __str__(self):
		s = "time: " + str(len(self.processed_data["time"]))
		for k in self.processed_data:
			if k != "time":
				s += "\n{}: {}".format(k, len(self.processed_data[k]))
		return s

	def __eq__(self, other):
		for k in self.processed_data:
			if abs(self.processed_data[k] - other.processed_data[k]) < self.epsilon:
				return False
		return True

	def reset(self):
		self.processed_data = {key: [] for key in self.PROCESSED_DATA_KEYS}
		

	def set_read_dir(self, files_dir):
		"""
		Set the directory path which will be inserted before relative file paths when calling the read() method.
		This is more of a convenience functionality to be able to read multiple files in a dictionary by just passing the relative filename as 
		an argument to file_path in read(). 
		"""
		self.files_dir = files_dir
		
	def verify_data(self):
		"""
		Verifies that the processed_data dict is correct
		"""
		assert all([k in self.PROCESSED_DATA_KEYS for k in self.processed_data]),\
			"Recording contains invalid data fields"

		time_ls = self.processed_data["time"]
		assert all(time_ls[i] <= time_ls[i + 1] for i in range(len(time_ls)-1)),\
			"time data is not in ascending order"

		len_time = len(self.processed_data["time"])
		lengths = [len(self.processed_data[k]) for k in self.PROCESSED_DATA_KEYS]
		len_set = set(lengths)
		
		if len_time > 0:
			# at least one more data field should have the same length
			print(lengths)
			assert lengths.count(len_time) > 1, "The stored data do not have the same lengths"

		if len_time == 0:
			# all data should have 0 length
			assert len(len_set) == 1, "The time data is empty, but there exists data in some other field(s)"
		elif len(len_set) == 2:
			# if there are different lengths in the data, 0 should be one of the lengths 
			# (it is ok to have some empty data fields while others are not)
			assert 0 in len_set, "The stored data do not have the same lengths."
		else:
			assert len(len_set) == 1, "The stored data do not have the same lengths."

	def read(self, file_path, delimiter="\t"):
		"""

		"""
		self.reset()

		if not os.path.isabs(file_path):
			file_path = os.path.join(self.files_dir, file_path)
		# Read processed data file
		ext = os.path.splitext(file_path)[1]
		if not ext == ".processed":
			raise Exception("Can only read .processed data files. Not '.{}'".format(ext))
		
		with open(file_path, "r") as f:
			read_keys = True
			for line in f:
				if read_keys:
					keys = tuple([k.strip() for k in line.split(delimiter)])
					for key in keys:
						assert key in self.PROCESSED_DATA_KEYS, "Invalid .processed file. '{}' is a not a valid data field".format(key)
					read_keys = False
				else:
					vals = [val.strip() for val in line.split(delimiter)]
					for k, val in zip(keys, vals):
						try:
							val = float(val)
						except ValueError:
							# ignore non float values
							raise Exception("Non float value found in .processed file, value is '{}'.".format(val))
						else:
							self.processed_data[k].append(val)
							
		print("Read processed data from '{}'".format(file_path))

	def save(self, file_path, delimiter="\t", keys=None):
		"""
		Saves the data in self.processed_data in file defined by file_path (replaces given extension with .processed)
		"""
		if not keys: 
			keys = self.PROCESSED_DATA_KEYS
		else:
			assert "time" in keys, "time needs to be saved"
			assert len(keys) > 1, "Can't save only time data!"
			for k in keys:
				assert k in self.PROCESSED_DATA_KEYS, "'{}' is an invalid data field"

		assert len(self.processed_data['time']) > 0, "Recording has no time data"
		# verify that the length of all data is equal
		self.verify_data()

		file_path = os.path.splitext(file_path)[0] + ".processed"
		file_path = os.path.join(self.files_dir, file_path)

		with open(file_path, "w") as f:
			non_empty_keys = [key for key in keys if self.processed_data[key]]
			f.write(delimiter.join(non_empty_keys) + "\n")
			
			for i in range(len(self.processed_data['time'])):
				line = []
				
				for k in non_empty_keys:
					line.append(str(self.processed_data[k][i]))

				f.write(delimiter.join(line) + "\n")
		print("Wrote processed data to '{}'".format(file_path))

	def copy(self):
		imu = ImuRecording(files_dir=self.files_dir)
		imu.processed_data = {k:[v for v in self.processed_data[k]] for k in self.processed_data}
		deepcopy(self.processed_data)
		return imu

	def gps_outages(self):
		"""
		TODO 
		"""
		return

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
		assert key != "time", "Nope, it is not alowed to add time like that!"
		assert key in self.PROCESSED_DATA_KEYS, "'{}' is not a valid data field".format(key)
		l = len(self.processed_data["time"])
		l_data = len(self.processed_data[key])


		if time is None or (l > 0 and time == self.time[-1]):
			
			if l_data == 0:
				if l == 0:
					# first data
					self.processed_data["time"].append(time)
				# this essentially makes it ok to have time values but no other values
				# (should it be checked here?)
				self.processed_data[key] = [0]*(l-1) + [val]

			elif l_data < l:
				# should not happen
				raise Exception("'{}' and time have different lengths".format(key))
			elif l_data == l:
				self.processed_data[key][-1] = val
			else: # l_data > l
				raise Exception("Data field '{}' and time has different lengths".format(key))
		else:
			if l == 0:
				# first data added, all data lists should be empty
				assert all([len(self.processed_data[k]) == 0 for k in self.PROCESSED_DATA_KEYS]),\
					"Data field time is empty but not all other data. This should not happen."
				self.processed_data["time"].append(time)
				self.processed_data[key].append(val)
			else:
				# we have already checked if time is equal last time
				assert time > self.processed_data["time"][-1], "Time is earlier than the latest recorded time"
				self.processed_data["time"].append(time)
				self.processed_data[key].append(val)

				# Pad all other values with their respective last value
				for k in self.PROCESSED_DATA_KEYS:
					# pad only if data already exist
					if k != key and k != "time" and self.processed_data[k]:
						# Redundancy check if there are data with wrong/different lengths 
						assert len(self.processed_data[k]) == l, "'{}' and time have different lengths".format(key)
						self.processed_data[k].append(self.processed_data[k][-1]) # pad with last values

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
				if key in ["roll", "pitch", "yaw", "gps_lat", "gps_long"]:
					# assuming degrees
					interpolated_val = interpolate_linear_angle(prev_val, next_val, prev_time, next_time, t, 180, -180)
				else:
					interpolated_val = interpolate_linear(prev_val, next_val, prev_time, next_time, t)
				
				aligned_data.append(interpolated_val)
				
			self.processed_data[key] = aligned_data
		self.processed_data["time"] = [t for t in aligned_time]

	def is_aligned_with(self, imu):
		if len(self.time) != len(imu.time):
			print("time has different lengths, {} and {}".format(len(self.time), len(imu.time)))
			return False
		return all([abs(t1 - t2) < self.epsilon for t1,t2 in zip(self.time, imu.time)])

	def compare(self, other, keys=None):
		assert self.is_aligned_with(other), "Imus are not aligned. Align before comparing."
		if keys is None:
			keys = self.PROCESSED_DATA_KEYS
		else:
			for k in keys:
				assert k != "time", "time should not be compared"
				assert k in self.PROCESSED_DATA_KEYS, "'{}' is not a valid data field"
		comp_imu = ImuRecording(name=self.name + "_vs_" + other.name)
		comp_imu.time = [t for t in self.time]
		for k in keys:
			if k != "time":
				a = np.array(self.processed_data[k])
				b = np.array(other.processed_data[k])
				diff = a - b
				for i, d in enumerate(diff):
					if d > 5:
						print("MMMM")
						print(a[i])
						print(b[i])
				if k in ["roll", "pitch", "yaw", "gps_lat", "gps_long"]:
					# assuming degrees
					diff = (diff + 180) % 360 - 180
				diff = [0 if abs(err) < self.epsilon else err for err in diff]
				comp_imu.processed_data[k] = diff
		return comp_imu


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
		
	def plot_all(self, show=True):
		from imu_plotter import ImuPlotter
		plotter = ImuPlotter([self])
		plotter.plot_all()
		if show: plotter.show()
	
	
if __name__ == "__main__":
	imu = ImuRecording()
	imu.read("SBG_general_000.processed")
	keys = ["time", "vel_x"]
	#for k in imu.PROCESSED_DATA_KEYS:
	#	if k not in keys:
	#		imu.processed_data[k] = []
	imu.add_data("vel_x", 0, 100000)
	imu.save("test_praaa", keys=["time"])