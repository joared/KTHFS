# imu_data_reader.py
import os
import numpy as np
from data_alignment import closest_index, interpolate_linear, interpolate_linear_angle
#from envs.pillow.Tools.scripts.objgraph import ignore

class ImuReader:
	DATA_PROCESSED_KEYS = ["time",
						   "long",
						   "lat",
						   "vel_x",
						   "vel_y",
						   "vel_z",
						   "roll",
						   "pitch",
						   "yaw",
						   "acc_x", 
						   "acc_y", 
						   "acc_z", 
						   "gyr_x", 
						   "gyr_y", 
						   "gyr_z"]
	
	DATA_PROCESSED_DEFAULT = {}
	for k in DATA_PROCESSED_KEYS:
		DATA_PROCESSED_DEFAULT[k] = []
		
	"""
	DATA_PROCESSED = {"time": [],
					  "acc_x": [],
					  "acc_y": [],
					  "acc_z": [],
					  "gyr_x": [],
					  "gyr_y": [],
					  "gyr_z": [],
					  "long": [],
					  "lat": []
					  }
	"""

	def __init__(self, files_dir=""):
		self.files_dir = files_dir
		self.data_raw_keys = [] # data types in order presented in file
		self.data_raw = {} 		# data
		self.data_processed = self.DATA_PROCESSED_DEFAULT.copy() 
		
	def __getattr__(self, attr):
		"""
		Convenient way to access the processed data
		"""
		if attr not in self.DATA_PROCESSED_KEYS:
			raise Exception("'{}' is not an attribute. Check the ImuReader.DATA_PROCESSED_KEYS for which attributes are valid.".format(attr))
		#try:
		return self.data_processed[attr]
		#except:
		#	return getattr(self, attr)
	
	def __setattr__(self, attr, val):
		"""
		Convenient way to set the processed data
		"""
		if attr in self.DATA_PROCESSED_KEYS:
			if not isinstance(val, list):
				raise Exception("Value for attribute '{}' should be a list, not '{}'".format(val, val.__class__))
			self.data_processed[attr] = val
		else:
			self.__dict__[attr] = val
			
	
	def reset(self):
		self.data_raw_keys = []
		self.data_raw = {} 		# data
		self.data_processed = self.DATA_PROCESSED_DEFAULT.copy()
		
	def set_read_dir(self, files_dir):
		"""
		Set the directory path which will be inserted before relative file paths when calling the read() method
		"""
		self.files_dir = files_dir
		
	def read(self, file_path, delimiter=None, debug=False):
		self.reset()
		if not os.path.isabs(file_path):
			file_path = os.path.join(self.files_dir, file_path)
		ignored_lines = []

		# Each sub-class needs to define a _read method which takes 
		# a file path and a delimiter as paramters and returns a list 
		# with all lines that has been ignored 
		ignored_lines = self._read(file_path, delimiter)
					
		if debug: self.log_ignored(ignored_lines)
		return self.data_raw.copy()
	
	def read_processed_data(self, file_path, delimiter=None):
		self.reset()
		if delimiter is None: delimiter = "\t"
		#file_path = os.path.join(self.files_dir, file_path + ".processed")
		file_path = os.path.splitext(file_path)[0] + ".processed"
		file_path = os.path.join(self.files_dir, file_path)
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

	def save_processed_data(self, file_path, delimiter=None):
		if delimiter is None: delimiter = "\t"
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
	
	def read_and_process(self, file_path, delimiter=None, debug=False):
		data = self.read(file_path, delimiter, debug)
		self.process_data()
		return data.copy()
		
	def read_process_save(self, file_path, delimiter_read=None, delimiter_save=None, debug=False):
		self.read(file_path, delimiter=delimiter_read, debug=debug)
		self.process_data()
		self.save_processed_data(file_path, delimiter_save)
		
	def process_data(self, data=None):
		raise Exception("This class should not be instanciated or a process_data method has not been defined in the sub-class")
		
	def log_ignored(self, ignored_lines):
		name = str(self.NAME) + "_ignored_data.txt"
		with open(name, "w") as f:
			f.write("Ignored lines\n")
			f.writelines(ignored_lines)
		
	def read_data_type_line(self, line, delimiter=None):
		print("Reading data types...", end="")
		line_ls = [s.strip() for s in line.split(delimiter)]
		for d in line_ls:
			self.data_raw_keys.append(d)
			self.data_raw[d] = []
		print(" all data types registered!")

	def read_data_line(self, line, delimiter=None):
		values = []
		for s in line.split(delimiter):		
			s = s.strip()
			try:
				val = float(s)
			except ValueError:
				val = s
			values.append(val)
			
		for k, v in zip(self.data_raw_keys, values):
			self.data_raw[k].append(v)

	def align_data(self, attrs, aligned_time):
		
		self.data_processed
		for attr in attrs:
			aligned = []
			for t in aligned_time:
				# Find the previous value
				
				prev_index = closest_index(self.time, t)
				prev_time = self.data_processed["time"][prev_index]
				prev_val = self.data_processed[attr][prev_index]
	
				# Find the next value
				next_index = prev_index + 1
				next_time = self.data_processed["time"][next_index]
				next_val = self.data_processed[attr][next_index]
	
				# Interpolate the value to requested time t
				if attr == "yaw":
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
	N = 0 # Number of times this class has been instanciated (will be appended to self.name)
	NAME = "SBG"
	#DATA_ATTRS = {"longitude": "Longitude", 
	#			  "latitude":"Latitude",
	#			  "yaw": "Yaw"}
	
	def __init__(self, files_dir=""):
		super(SBGReader, self).__init__(files_dir)
		self.name = "{}_{}".format(self.NAME, self.N)

	def process_data(self, data=None):
		if data is None: 
			data = self.data_raw.copy()
		print("Processing raw data...", end="")
		self.time = self._utc_to_sec(data)#self.data["UTC Time"] # UTC Time, GPS Time, Time stamp
		self.vel_x = data["X Velocity"]
		self.vel_y = data["Y Velocity"]
		self.roll = data["Roll"]
		self.pitch = data["Pitch"]
		self.yaw = list(np.array(data["Yaw"]))#/180*np.pi
		self.long = data["Longitude"]
		self.lat = data["Latitude"]
		print(" done!")

	def _read(self, file_path, delimiter):
		ignored_lines = []
		
		with open(file_path, "r") as f:
			for i, line in enumerate(f):
				if i == 0:
					self.read_data_type_line(line, delimiter)
				elif i == 1:
					ignored_lines.append(line)
				else:
					self.read_data_line(line, delimiter)
		return ignored_lines

	def _utc_to_sec(self, data):
		#print("Converting UTC Time to sec")
		sec_values = [] # Init new list
		for t in data["UTC Time"]:
			hour_min_sec = t.split(":")
			sec_values.append(60*60*float(hour_min_sec[0])+60*float(hour_min_sec[1])+float(hour_min_sec[2]))
		return sec_values