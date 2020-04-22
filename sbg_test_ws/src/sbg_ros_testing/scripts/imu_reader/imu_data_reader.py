# imu_data_reader.py
import os
import numpy as np
from data_alignment import closest_index, interpolate_linear, interpolate_linear_angle

class ImuReader(object):
	"""
	TODO: names like processed and raw are a bit inconsistent, maybe change that
	Base class for IMU readers that read IMU data from a generated ASCII file. 
	This class should not be instanciated. 
	Create sub-classes that inherit this class. The sub-class should define:

	read_ascii(self, file_path, delimiter): Reads the lines in the ASCII file and 
										    puts the data in the .data_ascii dictionary. 
										    Should return a list of ignored lines for debugging.

	General:

	Only difference between read and read_ascii is that ignored lines are being logged in a file in read while
	read_ascii is actually reading the 

	The methods 'read_data_type_line' and 'read_data_line' are helping methods that can be used in read_ascii.
	For example the ASCII formats from SBG, Xsens and VBOX are similar and data can be read in a similar way
	using these helping methods.

	Using the align_data method, aligns the data in data_processed to a specific time alignment and also sets the
	'time' key in data_processed to that time. This can be useful when multiple IMUs have different time alignments
	and a comparision wants to be made between them. Linear interpolation is used to adjust the values.
	This aligned time can be retrieved by using the align_time function in the data_alignment module.
	"""

	# Pre-defined data keys that will be tried to be set from the raw data in a read_ascii() call
	# TODO: not sure if all of these units are correct
	DATA_PROCESSED_KEYS = ["time", 	# UTC time in seconds
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
						   "gyr_x", # degrees/s
						   "gyr_y", # degrees/s
						   "gyr_z"] # degrees/s
	
	# This class attribute is used to initialize the .data_processed 
	# attribute of instances of this class by copying this dict
	DATA_PROCESSED_DEFAULT = {}
	for k in DATA_PROCESSED_KEYS:
		DATA_PROCESSED_DEFAULT[k] = []


	def __init__(self, files_dir=""):
		self.files_dir = files_dir
		self.data_ascii_keys = [] # data types in order presented in ascii file
		self.data_ascii = {} 		# ascii file data
		self.data_processed = self.DATA_PROCESSED_DEFAULT.copy() # data processed from ascii file

	def __getattr__(self, attr):
		"""
		Convenient way to access the processed data
		Remove this functionality (unintuitive)?
		"""
		if attr not in self.DATA_PROCESSED_KEYS:
			raise Exception("'{}' is not an attribute. Check the ImuReader.DATA_PROCESSED_KEYS for which attributes are valid.".format(attr))
		return self.data_processed[attr]


	def __setattr__(self, attr, val):
		"""
		Convenient way to set the processed data
		Remove this functionality (unintuitive)?
		"""
		if attr in self.DATA_PROCESSED_KEYS:
			if not isinstance(val, list):
				raise Exception("Value for attribute '{}' should be a list, not '{}'".format(val, val.__class__))
			self.data_processed[attr] = val
		else:
			self.__dict__[attr] = val
			
	
	def reset(self):
		self.data_ascii_keys = []
		self.data_ascii = {}
		self.data_processed = self.DATA_PROCESSED_DEFAULT.copy()
		

	def set_read_dir(self, files_dir):
		"""
		Set the directory path which will be inserted before relative file paths when calling the read() method.
		This is more of a convenience functionality to be able to read multiple files in a dictionary by just passing the relative filename as 
		ans argument to file_path in read(). 
		"""
		self.files_dir = files_dir
		
		
	def read(self, file_path, delimiter=None, save=False, debug=False):
		self.reset()
		
		if not os.path.isabs(file_path):
			file_path = os.path.join(self.files_dir, file_path)

		# Read processed data file
		ext = os.path.splitext(file_path)[1]
		if ext == ".processed":
			self.read_processed_data(file_path)
			ignored_lines = []
		else:
			# Read ascii data file
			# Each sub-class needs to define a read_ascii method which takes 
			# a file path and a delimiter as paramters and returns a list 
			# with all lines that has been ignored
			try:
				ignored_lines = self.read_ascii(file_path, delimiter) 
			except KeyError as e:
				raise KeyError("A key error occured during reading, is the delimiter set correctly? (check the printed data_ascii_key if they look reasonable)") 
				
		if save: self.save_processed_data(file_path, delimiter)
		if debug: self.log_ignored_data(ignored_lines)
		return self.data_ascii.copy()


	def read_ascii(self, file_path, delimiter):
		raise Exception("The base class '{}' can't read ASCII files. Instanciate the proper sub-class to read ASCII files.")


	def read_data_type_line(self, line, delimiter=None):
		print("Reading data types:")
		line_ls = [s.strip() for s in line.split(delimiter)]
		for d in line_ls:
			self.data_ascii_keys.append(d)
			self.data_ascii[d] = []
			print("'" + d + "'")
		print("Data types registered!")


	def read_data_line(self, line, delimiter=None):
		values = []
		for s in line.split(delimiter):		
			s = s.strip()
			try:
				val = float(s)
			except ValueError:
				val = s
			values.append(val)
			
		for k, v in zip(self.data_ascii_keys, values):
			self.data_ascii[k].append(v)


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
					assert keys == self.DATA_PROCESSED_KEYS, "Invalid .processed file. {} != {}".format(keys, self.DATA_PROCESSED_KEYS)
					read_keys = False
				else:
					vals = [val.strip() for val in line.split(delimiter)]
					for k, val in zip(self.DATA_PROCESSED_KEYS, vals):
						try:
							val = float(val)
						except ValueError:
							pass
						self.data_processed[k].append(val)
						
		print("Read processed data from '{}'".format(file_path))


	def save(self, file_path, delimiter=None):
		"""
		Saves the data in self.data_processed in file defined by file_path (replaces given extension with .processed)
		"""
		if delimiter is None: delimiter = "\t"
		#path, ext = os.path.splitext(file_path)
		file_path = os.path.splitext(file_path)[0] + ".processed"
		file_path = os.path.join(self.files_dir, file_path)
		with open(file_path, "w") as f:
			f.write(delimiter.join(self.DATA_PROCESSED_KEYS) + "\n")
			
			for i in range(len(self.time)):
				line = []
				
				for k in self.DATA_PROCESSED_KEYS:
					try:
						line.append(str(self.data_processed[k][i]))
					except IndexError:
						line.append("N/A")

				#print(delimiter.join(line))
				f.write(delimiter.join(line) + "\n")
		print("Wrote processed data to '{}'".format(file_path))
	

	def align_data(self, attrs, aligned_time):
		# TODO: reset all values that are not aligned?
		for attr in attrs:
			assert attr in self.data_processed, "'{}' is not a valid attribute".format(attr)
			aligned = []
			for t in aligned_time:

				# Find the previous value
				prev_index = closest_index(self.data_processed["time"], t)
				prev_time = self.data_processed["time"][prev_index]
				prev_val = self.data_processed[attr][prev_index]
	
				# Find the next value
				next_index = prev_index + 1
				next_time = self.data_processed["time"][next_index]
				next_val = self.data_processed[attr][next_index]
	
				# Interpolate the value to requested time t
				if attr in ["roll", "pitch", "yaw"]:
					#interpolated_val = interpolate_linear_angle(prev_val, next_val, prev_time, next_time, t)
					interpolated_val = interpolate_linear_angle(prev_val, next_val, prev_time, next_time, t)
				else:
					interpolated_val = interpolate_linear(prev_val, next_val, prev_time, next_time, t)
				aligned.append(interpolated_val)
			self.data_processed[attr] = aligned

		
class VBOXReader(ImuReader):
	NAME = "VBOX"
	

class XsensReader(ImuReader):
	NAME = "Xsens"

		
class SBGReader(ImuReader):
	N = 0 # Number of times this class has been instanciated ('_N' will be appended to self.name)
	NAME = "SBG"
	
	def __init__(self, files_dir=""):
		ImuReader.__init__(self, files_dir)
		self.name = "{}_{}".format(self.NAME, self.N)
		self.__class__.N += 1 # incerement N to have unique names for multiple instances 


	def read_ascii(self, file_path, delimiter):
		ignored_lines = []
		with open(file_path, "r") as f:
			for i, line in enumerate(f):
				if i == 0:
					self.read_data_type_line(line, delimiter)
				elif i == 1:
					ignored_lines.append(line)
				else:
					self.read_data_line(line, delimiter)
		print("Read ASCII data from '{}'".format(file_path))
		self._process_data(self.data_ascii)
		return ignored_lines


	def _process_data(self, data):
		data = data.copy()
		self.data_processed["time"] = self._utc_to_sec(data)
		self.data_processed["long"] = data["Longitude"]
		self.data_processed["lat"] = data["Latitude"]
		self.data_processed["vel_x"] = data["X Velocity"]
		self.data_processed["vel_y"] = data["Y Velocity"]
		self.data_processed["roll"] = list(np.array(data["Roll"])/180*np.pi)
		self.data_processed["pitch"] = list(np.array(data["Pitch"])/180*np.pi)
		self.data_processed["yaw"] = list(np.array(data["Yaw"])/180*np.pi)
		self.data_processed["acc_x"] = data["Accelerometer X"]
		self.data_processed["acc_y"] = data["Accelerometer Y"]
		self.data_processed["acc_z"] = data["Accelerometer Z"]
		self.data_processed["gyr_x"] = list(np.array(data["Gyroscope X"])/180*np.pi)
		self.data_processed["gyr_y"] = list(np.array(data["Gyroscope Y"])/180*np.pi)
		self.data_processed["gyr_z"] = list(np.array(data["Gyroscope Z"])/180*np.pi)
		print("Processed ASCII data!")


	def _utc_to_sec(self, data):
		sec_values = [] # Init new list
		for t in data["UTC Time"]:
			hour_min_sec = t.split(":")
			sec_values.append(60*60*float(hour_min_sec[0])+60*float(hour_min_sec[1])+float(hour_min_sec[2]))
		return sec_values