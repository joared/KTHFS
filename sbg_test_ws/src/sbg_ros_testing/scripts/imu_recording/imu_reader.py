# imu_reader.py
import os
import numpy as np
import utm
import argparse
from imu_recording import ImuRecording
from data_alignment import (closest_index, 
						   interpolate_linear, 
						   interpolate_linear_angle, 
						   convert_angle_in_range)
class ImuReader:
	"""
	Template class for reading the raw data values from ascii file
	"""
	def __init__(self, files_dir=""):
		self.files_dir = files_dir
		self.ascii_data_keys = []
		self.ascii_data = {}

	def __str__(self):
		s = ""
		for k in self.ascii_data:
			s += "\n{}: {}".format(k, len(self.ascii_data[k]))
		return s

	def reset(self):
		self.ascii_data_keys = []
		self.ascii_data = {}
	
	def read_data_type_line(self, line, delimiter):
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
		name = str(self.__class__.__name__) + "_ignored_data.txt"
		with open(name, "w") as f:
			f.write("This file contains the ignored data "\
				"from an ascii file read by a '{}':\n".format(self.__class__.__name__))
			f.writelines(ignored_lines)


	def latlon_to_pos(self, latitude, longitude):
		x0, y0, zone_nr, _ = utm.from_latlon(latitude[0], longitude[0])
		x_pos = []
		y_pos = []
		for lat, lon in zip(latitude, longitude):
			x, y, _, _ = utm.from_latlon(lat, lon, force_zone_number=zone_nr)
			x_pos.append(x-x0)
			y_pos.append(y-y0)
		return x_pos, y_pos


	def read(self, file_path, delimiter):
		raise Exception("Abstract class, instanciate sub class")

	def readffd(self, file_path, delimiter, files_dir="."):
		return self.read(os.path.join(files_dir, file_path), delimiter)

class XsensReader(ImuReader):
		
	def _data_to_recording(self, data):
		imu = ImuRecording()
		imu.time = self._utc_to_sec(data)
		imu.acc_x = data["Acc_X"]
		imu.acc_y = data["Acc_Y"]
		imu.acc_z = data["Acc_Z"]
		imu.gyr_x = data["Gyr_X"]
		imu.gyr_y = data["Gyr_Y"]
		imu.gyr_z = data["Gyr_Z"]
		#imu.vel_inc_x = self.data["VelInc_X"]
		#imu.vel_inc_y = self.data["VelInc_Y"]
		#imu.vel_inc_z = self.data["VelInc_Z"]
		
		#imu.roll = self.data["Roll"]
		#imu.pitch = self.data["Pitch"]
		imu.yaw = [convert_angle_in_range(180, -180, a) for a in list(-np.array(data["Yaw"]) + 90)]
		
		#for yaw, vx, vy in zip(data["Yaw"], data["Vel_X"], data["Vel_Y"]):
		#	vx_rel = 
		#	imu.vel_x.append()
		imu.vel_x = data["Vel_X"]
		imu.vel_y = data["Vel_Y"]
		imu.vel_z = data["Vel_Z"]
		#self.processed_data["long"] = data["Longitude"]
		#self.processed_data["lat"] = data["Latitude"]
		imu.pos_x, imu.pos_y = self.latlon_to_pos(data["Latitude"], data["Longitude"])
		return imu

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

	def read(self, file_path, delimiter, debug=False):
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
		if debug: self.log_ignored_data(ignored_lines)	
		return self._data_to_recording(self.ascii_data)


class VBOXReader(ImuReader):

	def _data_to_recording(self, data):
		data = data.copy()
		imu = ImuRecording()
		imu.processed_data["time"] = self._utc_to_sec(data)

		(imu.processed_data["pos_x"], 
		 imu.processed_data["pos_y"]) = self.latlon_to_pos([v/60. for v in data["lat"]],
		 												   [-v/60. for v in data["long"]])
		imu.processed_data["vel_x"] = list(np.array(data["velocity"])/3600.0*1000.0)
		imu.processed_data["vel_y"] = [-v for v in data["vert-vel"]]
		imu.processed_data["vel_z"] = data["vert-vel"]
		imu.processed_data["acc_x"] = data["X_Accel"]
		imu.processed_data["acc_y"] = data["Y_Accel"]
		imu.processed_data["acc_z"] = data["Z_Accel"]
		imu.processed_data["gyr_x"] = data["RollRate"]
		imu.processed_data["gyr_y"] = data["PitchRate"]
		imu.processed_data["gyr_z"] = data["YawRate"]
		imu.processed_data["yaw"] = data["heading"]
		return imu

	def _utc_to_sec(self, data):
		sec_values = []
		for t in data["time"]:
			t_str = str(t)
			hour = float(t_str[0:2])
			minute = float(t_str[2:4])
			sec = float(t_str[4:])
			sec_values.append(60*60*hour+60*minute+sec)
		return sec_values

	def read(self, file_path, delimiter, debug=False):
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
					ignored_lines.append(line)

		if debug: self.log_ignored_data(ignored_lines)
		return self._data_to_recording(self.ascii_data)

		
class SBGReader(ImuReader):

	def _data_to_recording(self, data):
		# TODO: units not used atm
		imu = ImuRecording()
		imu.processed_data["time"] = self._utc_to_sec(data)
		#imu.processed_data["gps_long"] = data["Lon"]
		#imu.processed_data["gps_lat"] = data["Lat"]
		(imu.processed_data["pos_x"], 
		 imu.processed_data["pos_y"]) = self.latlon_to_pos(data["Latitude"],
		 												   data["Longitude"])
		imu.processed_data["vel_x"] = data["X Velocity"]
		imu.processed_data["vel_y"] = data["Y Velocity"]
		imu.processed_data["vel_z"] = data["Z Velocity"]
		imu.processed_data["roll"] = data["Roll"]
		imu.processed_data["pitch"] = data["Pitch"]
		imu.processed_data["yaw"] = data["Yaw"]
		imu.processed_data["acc_x"] = data["Accelerometer X"]
		imu.processed_data["acc_y"] = data["Accelerometer Y"]
		imu.processed_data["acc_z"] = data["Accelerometer Z"]
		imu.processed_data["gyr_x"] = data["Gyroscope X"]
		imu.processed_data["gyr_y"] = data["Gyroscope Y"]
		imu.processed_data["gyr_z"] = data["Gyroscope Z"]

		return imu


	def _utc_to_sec(self, data):
		sec_values = [] # Init new list
		for t in data["UTC Time"]:
			hour_min_sec = t.split(":")
			sec_values.append(60*60*float(hour_min_sec[0])+60*float(hour_min_sec[1])+float(hour_min_sec[2]))
		return sec_values

	def read(self, file_path, delimiter, debug=False):
		ignored_lines = []
		with open(file_path, "r") as f:
			for i, line in enumerate(f):
				if i == 0:
					self.read_data_type_line(line, delimiter)
				elif i == 1:
					ignored_lines.append(line)
					#units = line.split(delimiter)
				else:
					self.read_data_line(line, delimiter)
		if debug: self.log_ignored_data(ignored_lines)
		return self._data_to_recording(self.ascii_data)

read_sbg = SBGReader().readffd
read_vbox = VBOXReader().readffd
read_xsens = XsensReader().readffd

if __name__ == "__main__":
	pass