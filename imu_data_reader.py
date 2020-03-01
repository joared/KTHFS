# imu_data_reader.py
import os

class ImuReader:
	def __init__(self, files_dir=""):
		self.files_dir = files_dir
		self.data_keys = [] # data types in order presented in file
		self.data = {} 		# data 
		
	def read(self, file_path):
		raise Exception("Abstract class, write your own read method bitch!")
		
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

class XsensReader(ImuReader):
	DELIMITER = "\t"
	NAME = "Xsens"

	def _set_attrs_from_data(self):
		print("Setting attributes from data...")
		self.time = self._utc_to_sec()#self.data["UTC_Minute"]
		#self.acc_x = self.data["Acc_X"]
		#self.acc_y = self.data["Acc_Y"]
		#self.acc_z = self.data["Acc_Z"]
		#self.gyr_x = self.data["Gyr_X"]
		#self.gyr_y = self.data["Gyr_Y"]
		#self.gyr_z = self.data["Gyr_Z"]
		#self.vel_inc_x = self.data["VelInc_X"]
		#self.vel_inc_y = self.data["VelInc_Y"]
		#self.vel_inc_z = self.data["VelInc_Z"]
		self.vel_x = self._velocity_converter()#self.data["Vel_X"]
		self.vel_y = self.data["Vel_Y"]
		#self.vel_z = self.data["Vel_Z"]
		#self.roll = self.data["Roll"]
		#self.pitch = self.data["Pitch"]
		self.heading = self.data["Yaw"]
		self.longitude = self.data["Longitude"]
		self.latitude = self.data["Latitude"]
		
	def read(self, file_path):
		if not os.path.isabs(file_path):
			file_path = os.path.join(self.files_dir, file_path)
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
					
		self.log_ignored(ignored_lines)
		self._set_attrs_from_data()
		return self.data

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

	def _velocity_converter(self):
		pass


		
class VBOXReader(ImuReader):
	NAME = "VBOX"
	DELIMITER = None
	
	def _set_attrs_from_data(self):
		self.time = self._utc_to_sec()#self.data["time"]
		#self.acc_x = self.data["X_Accel"]
		#self.acc_y = self.data["Y_Accel"]
		#self.acc_z = self.data["Z_Accel"]
		#self.gyr_x = self.data["Gyr_X"]
		#self.gyr_y = self.data["Gyr_Y"]
		#self.gyr_z = self.data["Gyr_Z"]
		#self.vel_inc_x = self.data["VelInc_X"]
		#self.vel_inc_y = self.data["VelInc_Y"]
		#self.vel_inc_z = self.data["VelInc_Z"]
		self.vel_x = self.data["Lng._Vel."]
		self.vel_y = self.data["Lat._Vel."]
		#self.vel_z = self.data["Vel_Z"]
		#self.roll = self.data["Roll"]
		#self.pitch = self.data["Pitch"]
		self.heading = self.data["heading"]#["heading"]
		self.longitude = [-v/60 for v in self.data["long"]] # minutes to degrees
		self.latitude = [v/60 for v in self.data["lat"]]  # minutes to degrees
		
	def read(self, file_path):
		if not os.path.isabs(file_path):
			file_path = os.path.join(self.files_dir, file_path)
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
					#print("Ignoring '{}'".format(line))
					ignored_lines.append(line)
					
		self.log_ignored(ignored_lines)
		self._set_attrs_from_data()	
		return self.data

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

	def _set_attrs_from_data(self):
		print("Setting attributes from data...")
		self.time = self._utc_to_sec()#self.data["UTC Time"] # UTC Time, GPS Time, Time stamp
		self.vel_x = self.data["X Velocity"]
		self.vel_y = self.data["Y Velocity"]
		self.roll = self.data["Roll"]
		self.pitch = self.data["Pitch"]
		self.heading = self.data["Yaw"]
		self.longitude = self.data["Longitude"]
		self.latitude = self.data["Latitude"]
		
	def read(self, file_path):
		if not os.path.isabs(file_path):
			file_path = os.path.join(self.files_dir, file_path)
		ignored_lines = []
		
		with open(file_path, "r") as f:
			for i, line in enumerate(f):
				if i == 0:
					self.read_data_type_line(line, self.DELIMITER)
				elif i == 1:
					ignored_lines.append(line)
				else:
					self.read_data_line(line, self.DELIMITER)

		self.log_ignored(ignored_lines)
		self._set_attrs_from_data()
		return self.data

	def _utc_to_sec(self):
		print("Converting UTC Time to sec")
		sec_values = [] # Init new list
		for t in self.data["UTC Time"]:
			hour_min_sec = t.split(":")
			sec_values.append(60*60*float(hour_min_sec[0])+60*float(hour_min_sec[1])+float(hour_min_sec[2]))
		return sec_values