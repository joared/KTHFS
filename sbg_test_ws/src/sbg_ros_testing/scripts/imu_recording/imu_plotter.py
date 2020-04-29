import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
import numpy as np
from itertools import izip
import utm

class ImuPlotter:
	def __init__(self, imu):
		self.imu = imu
		self.pose_arrow = None

	def plot_play(self, update_freq=2.5, play_speed=1, start_time=0):
		#interval=400
		#self.play_done = False
		interval = 1.0/update_freq*1000
		self.play_speed = play_speed
		self.figgy = plt.figure()
		#fig.suptitle("Imu plotting")
		#self.pose_fig = fig.add_subplot(2,2,1)
		#self.vel_fig = fig.add_subplot(2,2,2)
		#self.acc_fig = fig.add_subplot(2,2,3)
		#self.gyr_fig = fig.add_subplot(2,2,4)
		self.start_time = time.time() - start_time
		self.plot_pos()
		self.pose_arrow = None
		self.ani = FuncAnimation(self.figgy, self.animate_imu, interval=interval)

	def show(self):
		plt.show()

	def animate_imu(self, i):
		if len(self.imu.time) == 0: return
		t_rel = (time.time() - self.start_time)*self.play_speed
		t_abs = self.imu.time[0] + t_rel
		idx = self.imu.time_index(t_abs)
		t_abs = self.imu.time[idx]
		t_rel = t_abs - self.imu.time[0]
		fig = plt.figure(self.figgy.number)
		#print(dir(fig))
		fig.suptitle("Time: {} s ({})".format(round(t_rel, 2), round(t_abs, 2)))
		#self.fig.cla()

		self.plot_pose(idx)
		plt.axis("equal")
		
		if idx == len(self.imu.time):
			#self.play_done = True
			self.ani.event_source.stop()
		

	def plot_all(self, i=None):
		# pose
		plt.subplot(2,2,1)
		plt.cla()
		self.plot_pos(i)
		# velocity
		plt.subplot(2,2,2)
		plt.cla()
		self.plot_vel(i)
		# acceleration
		plt.subplot(2,2,3)
		plt.cla()
		self.plot_acc(i)
		# gyroscope
		plt.subplot(2,2,4)
		plt.cla()
		self.plot_gyr(i)
		
	def plot_pose(self, i=None):
		if not i: i = len(self.imu.time)
		if self.pose_arrow: self.pose_arrow.remove()
		x0, y0, zone_nr, _ = utm.from_latlon(self.imu.lat[0], self.imu.long[0])
		x, y, _, _ = utm.from_latlon(self.imu.lat[i], self.imu.long[i], force_zone_number=zone_nr)
		x, y = x-x0, y-y0

		yaw = self.imu.yaw[i]
		yaw = np.pi/2 - yaw # transform from yaw relative north to yaw relative x
		dx = np.cos(yaw)*100
		dy = np.sin(yaw)*100
		self.pose_arrow = plt.arrow(x, y, dx, dy, width=20)

	def plot_pos(self, i=None):
		if not i: i = len(self.imu.time)
		
		x0, y0, zone_nr, _ = utm.from_latlon(self.imu.lat[0], self.imu.long[0])

		x_pos = []
		y_pos = []
		for lat, lon in zip(self.imu.lat[:i], self.imu.long[:i]):
			x, y, _, _ = utm.from_latlon(lat, lon, force_zone_number=zone_nr)
			x_pos.append(x-x0)
			y_pos.append(y-y0)
		plt.plot(x_pos, y_pos)	
		
		# Temp, scatter first and last 0 occcurance in gps signal
		#plt.plot(self.imu.long[:i], self.imu.lat[:i])
		#plt.scatter(x_pos[self.imu.gps_long.index(0)],
		#			y_pos[self.imu.gps_lat.index(0)], color="r")
		#rev_long = list(reversed(self.imu.gps_long))
		#rev_lat = list(reversed(self.imu.gps_lat))
		#plt.scatter(list(reversed(x_pos))[rev_long.index(0)],
		#			list(reversed(y_pos))[rev_lat.index(0)], color="g")
		plt.ylabel("Northings")
		plt.xlabel("Eastings")

	def plot_gps(self, i=None):
		if not i: i = len(self.imu.time)
		#longitude = np.array([None if v == 0.0 else v for v in self.imu.gps_long[:i]]).astype(np.double)
		#long_mask = np.isfinite(longitude)
		#latitude = np.array([None if v == 0.0 else v for v in self.imu.gps_lat[:i]]).astype(np.double)
		#lat_mask = np.isfinite(latitude)
		longitude = []
		latitude = []
		lon_prev = 0
		lat_prev = 0

		for lon, lat in zip(self.imu.gps_long[:i],self.imu.gps_lat[:i]):
			if lon == 0:
				lon = lon_prev
			else:
				lon_prev = lon
			if lat == 0:
				lat = lat_prev
			else:
				lat_prev = lat
			longitude.append(lon)
			latitude.append(lat)

		print(self.imu.gps_lat)
		#print(latitude)
		plt.plot(longitude, latitude)
		plt.ylabel("GPS Latitude")
		plt.xlabel("GPS Longitude")

	def plot_vel(self, i=None):
		if not i: i = len(self.imu.time)
		plt.plot(self.imu.time[:i], self.imu.vel_x[:i])
		plt.plot(self.imu.time[:i], self.imu.vel_y[:i])
		plt.plot(self.imu.time[:i], self.imu.vel_z[:i])
		plt.ylabel("Velocity")
		plt.xlabel("sec")
		plt.legend(["vel_x", "vel_y", "vel_z"])

	def plot_acc(self, i=None):
		if not i: i = len(self.imu.time)
		plt.plot(self.imu.time[:i], self.imu.acc_x[:i])
		plt.plot(self.imu.time[:i], self.imu.acc_y[:i])
		plt.plot(self.imu.time[:i], self.imu.acc_z[:i])
		plt.ylabel("Acceleration")
		plt.xlabel("sec")
		plt.legend(["acc_x", "acc_y", "acc_z"])

	def plot_gyr(self, i=None):
		if not i: i = len(self.imu.time)
		plt.plot(self.imu.time[:i], self.imu.gyr_x[:i])
		plt.plot(self.imu.time[:i], self.imu.gyr_y[:i])
		plt.plot(self.imu.time[:i], self.imu.gyr_z[:i])
		plt.ylabel("Gyroscope")
		plt.xlabel("sec")
		plt.legend(["gyr_x", "gyr_y", "gyr_z"])

#######################################
def plot_pos(imus, real_time=False):
	plt.figure()
	for imu in imus:
		if real_time:
			for lng, lat in zip(imu.long, imu.lat):
				plt.cla()
				plt.scatter(lng, lat)
				plt.pause(0.0001)
		else:
			plt.plot(imu.long, imu.lat)
	plt.legend([imu.NAME for imu in imus])

def plot_time(imus):
	# Plots time in imus time format
	n = len(imus)
	for i, imu in enumerate(imus):
		plt.subplot(1,n,i+1)
		plt.plot(imu.time)
		plt.legend(imu.NAME)
	
	
def print_keys(imu):
	# Prints all data types from imu
	for k in imu.data_keys:
		print(k)

def plot_sensors(imu, real_time=False):
	if real_time:
		for i in range(len(imu.time)):
			plt.subplot(1, 2, 1)
			plt.cla()
			plt.plot(imu.acc_x[:i])
			plt.plot(imu.acc_y[:i])
			plt.plot(imu.acc_z[:i])
			plt.legend(["Acc X", "Acc Y", "Acc Z"])
			plt.subplot(1, 2, 2)
			plt.cla()
			plt.plot(imu.gyr_x[:i])
			plt.plot(imu.gyr_y[:i])
			plt.plot(imu.gyr_z[:i])
			plt.legend(["Gyr X", "Gyr Y", "Gyr Z"])
			plt.pause(0.001)
	else:
		plt.subplot(1, 2, 1)
		plt.plot(imu.acc_x)
		plt.plot(imu.acc_y)
		plt.plot(imu.acc_z)
		plt.legend(["Acc X", "Acc Y", "Acc Z"])
		plt.subplot(1, 2, 2)
		plt.plot(imu.gyr_x)
		plt.plot(imu.gyr_y)
		plt.plot(imu.gyr_z)
		plt.legend(["Gyr X", "Gyr Y", "Gyr Z"])

def plot_angle_error_vs_slip_angle(ref_imu, comp_imus):
	#colors = ["blue", "orange", "green"]
	
	#plt.subplot(2,1,1)
	#plt.ylim([-20, 20])
	plt.plot(ref_imu.time_aligned, ref_imu.slip_angle_aligned)
	for imu in comp_imus:
		sq_errs = []
		for i, yaw_actual in enumerate(ref_imu.yaw_aligned):
			err = min_angle_diff(180, -180, yaw_actual, imu.yaw_aligned[i])
			sq_err = err**2
			sq_errs.append(err)
		plt.plot(ref_imu.time_aligned, sq_errs)
	plt.legend([ref_imu.NAME + " <slip angle>"] + [imu.NAME + " yaw err"  for imu in comp_imus])
	#plt.subplot(2,1,2)
	#plt.ylim([-20, 20])
	#plt.plot(ref_imu.slip_angle)	
		
def plot_yaw(imus):
	for imu in imus:
		for imu in imus:
			#plt.plot(imu.time, imu.yaw)
			plt.plot(imu.yaw)
	plt.legend([imu.NAME + " yaw"  for imu in imus])

if __name__ == "__main__":
	from imu_data_reader import *
	imu = SBGRecording()
	imu.read("SBG_general_000.processed")
	plotter = ImuPlotter(imu)
	plotter.plot_play()
	plotter.show()