# imu_data_reader.py
import os
import numpy as np
from data_alignment import closest_index, interpolate_linear, interpolate_linear_angle
from envs.pillow.Tools.scripts.objgraph import ignore

class ImuReader:
	def __init__(self, files_dir=""):
		self.files_dir = files_dir
		self.data_keys = [] # data types in order presented in file
		self.data = {} 		# data 
		
	#def __getattr__(self, attr):
	#	return self.data[self.DATA_ATTRS[attr]]
	
	#def __setattr__(self, attr, val):
	#	self.data[self.DATA_ATTRS[attr]] = val
	
	def read(self, file_path):
		if not os.path.isabs(file_path):
			file_path = os.path.join(self.files_dir, file_path)
		ignored_lines = []

		ignored_lines = self._read(file_path)
					
		self.log_ignored(ignored_lines)
		self.set_attrs_from_data()
		return self.data
		
	def log_ignored(self, ignored_lines):
		name = str(self.NAME) + "_ignored_data.txt"
		with open(name, "w") as f:
			f.write("Ignored lines\n")
			f.writelines(ignored_lines)
		
	def read_data_type_line(self, line, delimiter=None):
		print("Reading data types...")
		line_ls = [s.strip() for s in line.split(delimiter)]
		for d in line_ls:
			self.data_keys.append(d)
			self.data[d] = []
		print("...all data types registered.")

	def read_data_line(self, line, delimiter=None):
		values = []
		for s in line.split(delimiter):		
			s = s.strip()
			try:
				val = float(s)
			except ValueError:
				val = s
			values.append(val)
			
		for k, v in zip(self.data_keys, values):
			self.data[k].append(v)

	def align_data(self, attrs):
		"""
		Align the datafields set to True
	
		Input: list of the IMU objects in order [sbg, xsens, vbox], the IMUs NEED to be processed by align_time first!
		Output: A list of the updated IMUs with new attributes DATAFIELD_aligned of the datafields set to true
		"""
	
		attrs_actual = ["vel_x", "vel_y", "latitude", "longitude", "yaw"]
	
		for attr in attrs:
			aligned = []
			for t in self.time_aligned:
				# Find the previous value
				
				prev_index = closest_index(self.time, t)
				prev_time = self.time[prev_index]
				prev_val = getattr(self, attr)[prev_index]
	
				# Find the next value
				next_index = prev_index + 1
				next_time = self.time[next_index]
				next_val = getattr(self, attr)[next_index]
	
				# Interpolate the value to requested time t
				if attr == "yaw":
					#interpolated_val = interpolate_linear_angle(prev_val, next_val, prev_time, next_time, t)
					interpolated_val = interpolate_linear_angle(prev_val, next_val, prev_time, next_time, t)
				else:
					interpolated_val = interpolate_linear(prev_val, next_val, prev_time, next_time, t)
				aligned.append(interpolated_val)
			setattr(self, attr + "_aligned", aligned)

class XsensReader(ImuReader):
	DELIMITER = "\t"
	NAME = "Xsens"
	
	#DATA_ATTRS = {"longitude": "Longitude", 
	#			  "latitude":"Latitude",
	#			  "yaw": "Yaw"}
	
	def set_attrs_from_data(self):
		print("Setting attributes from data...")
		self.time = self._utc_to_sec()#self.data["UTC_Minute"]
		self.acc_x = self.data["Acc_X"]
		self.acc_y = self.data["Acc_Y"]
		self.gyr_z = self.data["Gyr_Z"]

		self.vel_x, self.vel_y, self.vel_z = self._vel_inc_to_vel()
		self.roll = self.data["Roll"]
		self.pitch = self.data["Pitch"]
		self.yaw = -np.array(self.data["Yaw"])+95 # offset of 95 for some reason
		self.longitude = self.data["Longitude"]
		self.latitude = self.data["Latitude"]
		

	def convert_data(self):
		print("Setting attributes from data...")
		#self.time = self._utc_to_sec()#self.data["UTC_Minute"]
		self.acc_x = self.data["Acc_X"]
		self.acc_y = self.data["Acc_Y"]
		self.gyr_z = self.data["Gyr_Z"]

		self.vel_x, self.vel_y, self.vel_z = self._vel_inc_to_vel()
		self.roll = self.data["Roll"]
		self.pitch = self.data["Pitch"]
		self.yaw = -np.array(self.data["Yaw"])+95 # offset of 95 for some reason
		self.longitude = self.data["Longitude"]
		self.latitude = self.data["Latitude"]
	
	def _read(self, file_path):
		ignored_lines = []
		read_data = False
		
		with open(file_path, "r") as f:
			for line in f:
				if "PacketCounter" in line:
					self.read_data_type_line(line, self.DELIMITER)
					read_data = True
				elif read_data is True:
					self.read_data_line(line, self.DELIMITER)
				else:
					ignored_lines.append(line)
		return ignored_lines

	def _utc_to_sec(self):
		print("Converting UTC Time to sec")
		sec_values = [] # Init new list
		for i in range(len(self.data["UTC_Minute"])):
			hour = self.data["UTC_Hour"][i]
			minute = self.data["UTC_Minute"][i]
			second = self.data["UTC_Second"][i]
			mili = self.data["UTC_Nano"][i]/1000000000

			sec_values.append(60*60*hour+60*minute+second+mili)
		return sec_values
		
	def _vel_inc_to_vel(self):
		vel_x, vel_y, vel_z = [], [], []
		vx, vy, vz = 0, 0, 0
		for vx_inc, vy_inc, vz_inc in zip(self.data["VelInc_X"], self.data["VelInc_Y"], self.data["VelInc_Z"]):
			vx += vx_inc
			vy += vy_inc
			vz += vz_inc
			vel_x.append(vx)
			vel_y.append(vy)
			vel_z.append(vz)
		
		return vel_x, vel_y, vel_z
		
class VBOXReader(ImuReader):
	NAME = "VBOX"
	DELIMITER = None
	
	#DATA_ATTRS = {"longitude": "long", 
	#			  "latitude":"lat",
	#			  "yaw": "heading"}
	
	def set_attrs_from_data(self):
		self.time = self._utc_to_sec()#self.data["time"]
		self.acc_x = self.data["X_Accel"]
		self.acc_y = self.data["Y_Accel"]

		#self.gyr_z = self.data["Gyr_Z"]
		self.slip_angle = self.data["Slip_Angle"]
		self.vel_x = 1000/(60*60)*np.array(self.data["Lng._Vel."])
		self.vel_y = 1000/(60*60)*np.array(self.data["Lat._Vel."])
		
		self.yaw = np.array(self.data["heading"])#-180#/180*np.pi - np.pi
		self.longitude = [-v/60 for v in self.data["long"]] # minutes to degrees
		self.latitude = [v/60 for v in self.data["lat"]]  # minutes to degrees

	def _read(self, file_path):
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
					self.read_data_type_line(line)
					
				elif read_data is True:
					self.read_data_line(line)
				else:
					ignored_lines.append(line)
		return ignored_lines

	def _utc_to_sec(self):
		print("Converting UTC Time to sec")
		sec_values = [] # Init new list
		for t in self.data["time"]:
			t_str = str(t)
			hour = float(t_str[0:2])
			minute = float(t_str[2:4])
			sec = float(t_str[4:])
			sec_values.append(60*60*hour+60*minute+sec)
		return sec_values
		
class SBGReader(ImuReader):
	DELIMITER = "\t"
	NAME = "SBG"

	#DATA_ATTRS = {"longitude": "Longitude", 
	#			  "latitude":"Latitude",
	#			  "yaw": "Yaw"}

	def set_attrs_from_data(self):
		print("Setting attributes from data...")
		self.time = self._utc_to_sec()#self.data["UTC Time"] # UTC Time, GPS Time, Time stamp
		self.vel_x = self.data["X Velocity"]
		self.vel_y = self.data["Y Velocity"]
		self.roll = self.data["Roll"]
		self.pitch = self.data["Pitch"]
		self.yaw = np.array(self.data["Yaw"])#/180*np.pi
		self.longitude = self.data["Longitude"]
		self.latitude = self.data["Latitude"]

	def _read(self, file_path):
		ignored_lines = []
		
		with open(file_path, "r") as f:
			for i, line in enumerate(f):
				if i == 0:
					self.read_data_type_line(line, self.DELIMITER)
				elif i == 1:
					ignored_lines.append(line)
				else:
					self.read_data_line(line, self.DELIMITER)
		return ignored_lines

	def _utc_to_sec(self):
		print("Converting UTC Time to sec")
		sec_values = [] # Init new list
		for t in self.data["UTC Time"]:
			hour_min_sec = t.split(":")
			sec_values.append(60*60*float(hour_min_sec[0])+60*float(hour_min_sec[1])+float(hour_min_sec[2]))
		return sec_values