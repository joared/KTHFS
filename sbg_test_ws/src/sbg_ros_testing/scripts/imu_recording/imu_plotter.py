import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
from matplotlib import gridspec
import time
import numpy as np
import utm

class ImuPlotter:
	def __init__(self, imus):
		self.imus = imus
		self.aligned = all([self.imus[0].is_aligned_with(imu) for imu in self.imus[1:]]) and len(self.imus) > 1
		# live plotting attributes
		self.figgy = None
		self.pose_arrows = []
		self.markers = []

		self.update_freq = None
		self.play_speed = None
		self.pause = False
		self.reset = False
		self.start_time = None
		self.done_imus = {imu:False for imu in self.imus}
		self.t_rel = 0

	def show(self):
		plt.show()

	def on_resize(self, event):
		self.figgy.canvas.draw()

	def on_click(self, event):
		print(event)

	def on_key_press(self, event):
		k = event.key
		if k in ["p", " "]:
			self.pause = not self.pause
		elif k == "+":
			if abs(self.play_speed) <= 1: self.play_speed += 0.1
			else: self.play_speed += 0.5
		elif k == "-":
			if abs(self.play_speed) <= 1: self.play_speed -= 0.1
			else: self.play_speed -= 0.5
		elif k == "r":
			self.reset = True
		elif k in [str(i) for i in range(1,10)]:
			self.play_speed = int(k)

	def on_scroll(self, event):
		self.t_rel += event.step

	def play_animation(self, pos=False, vel=False, acc=False, gyr=False,
				  	   update_freq=30, play_speed=1, start_time=0, blit=False):
		interval = 1.0/update_freq*1000
		self.update_freq = update_freq
		self.play_speed = play_speed
		self.pause = False
		self.reset = False
		self.start_time = start_time

		self.figgy = plt.figure()

		plt.connect('button_press_event', self.on_click)
		plt.connect('scroll_event', self.on_scroll)
		plt.connect('key_press_event', self.on_key_press)
		#plt.connect('resize_event', self.on_resize)
		
		self.artists = []
		self.done_imus = {imu:False for imu in self.imus}

		#self._init_plot()
		if len(self.imus) == 1:
			self.ani = FuncAnimation(self.figgy, self._animate, self._time_gen, self._init_plot_single,
									 interval=interval, blit=blit, repeat=False)
		else:
			self.ani = FuncAnimation(self.figgy, self._animate, self._time_gen, self._init_plot,
									 interval=interval, blit=blit, repeat=False)

		# when calling plt.show after this 
		# an error occurs. This solves it, might be a bug.
		self.figgy.canvas.draw()

	def _init_plot(self):
		gs = gridspec.GridSpec(3, 3)
		self.gs = gs
		self.ax_pos = plt.subplot(gs[:, :2])
		self.ax_pos.title.set_text("Position")
		self.title = self.ax_pos.text(0, 0, 'time info', horizontalalignment="left",
							 verticalalignment="bottom", transform=self.ax_pos.transAxes)
		self.plot_pos()
		plt.axis("equal")
		#pose_arrows = self.plot_pose()
		plt.legend([imu.name for imu in self.imus])

		rel_times = [[t-imu.time[0] for t in imu.time] for imu in self.imus]
		self.ax_vx = plt.subplot(gs[0, 2])
		self.ax_vx.title.set_text("Velocity") # since they share axis, this can only be done for one
		self.ax_vx.set_ylabel("Velocity X")
		for rel_time, imu in zip(rel_times, self.imus): self.ax_vx.plot(rel_time, imu.vel_x)
		self.ax_vy = plt.subplot(gs[1, 2], sharex=self.ax_vx)
		self.ax_vy.set_ylabel("Velocity Y")
		for rel_time, imu in zip(rel_times, self.imus): self.ax_vy.plot(rel_time, imu.vel_y)
		self.ax_vz = plt.subplot(gs[2, 2], sharex=self.ax_vx)
		self.ax_vz.set_ylabel("Velocity Z")
		for rel_time, imu in zip(rel_times, self.imus): self.ax_vz.plot(rel_time, imu.vel_z)
		#markers = self.plot_markers()
		#return pose_arrows + markers
		return [self.title]

	def _init_plot_single(self):
		gs = gridspec.GridSpec(3, 3)
		self.gs = gs
		self.ax_pos = plt.subplot(gs[:, :2])
		self.ax_pos.title.set_text("Position")
		self.title = self.ax_pos.text(0, 0, 'time info', horizontalalignment="left",
							 verticalalignment="bottom", transform=self.ax_pos.transAxes)
		self.plot_pos()
		plt.axis("equal")
		#pose_arrows = self.plot_pose()
		plt.legend([imu.name for imu in self.imus])

		rel_time = [t-imu.time[0] for t in self.imus[0].time]
		self.ax_vx = plt.subplot(gs[0, 2])
		self.ax_vy = self.ax_vx
		self.ax_vz = self.ax_vx
		self.ax_vx.title.set_text("Velocity") # since they share axis, this can only be done for one
		self.ax_vx.plot(rel_time, self.imus[0].vel_x)
		self.ax_vy.plot(rel_time, self.imus[0].vel_y)
		self.ax_vz.plot(rel_time, self.imus[0].vel_z)
		self.ax_vx.legend(["Vel X", "Vel Y", "Vel Z"])
		self.ax_a = plt.subplot(gs[1, 2])
		self.ax_a.plot(rel_time, self.imus[0].acc_x)
		self.ax_a.plot(rel_time, self.imus[0].acc_y)
		self.ax_a.plot(rel_time, self.imus[0].acc_z)
		self.ax_a.legend(["Acc X", "Acc Y", "Acc Z"])
		self.ax_g = plt.subplot(gs[2, 2])
		self.ax_g.plot(rel_time, self.imus[0].gyr_x)
		self.ax_g.plot(rel_time, self.imus[0].gyr_y)
		self.ax_g.plot(rel_time, self.imus[0].gyr_z)
		self.ax_g.legend(["Gyr X", "Gyr Y", "Gyr Z"])
		return [self.title]

	def _time_gen(self):
		time_ref = time.time()
		# change to start time
		self.t_rel = self.start_time
		self.start_time = 0 # only want to start here the first time
		while True:
			if all(self.done_imus.values()):
				if self.reset:
					self.done_imus = {imu:False for imu in self.imus}
					self.t_rel = 0
					self.reset = False
					time_ref = time.time()
			elif self.reset:
				self.done_imus = {imu:False for imu in self.imus}
				self.t_rel = 0
				self.reset = False
			elif self.pause:
				time_ref = time.time()
			else:
				curr_time = time.time()
				self.t_rel = self.t_rel + (curr_time - time_ref)*self.play_speed
				self.t_rel = max([self.t_rel, 0])
				self.t_rel = min([self.t_rel, max([imu.time[-1]-imu.time[0] for imu in self.imus])])
				time_ref = curr_time
			yield self.t_rel

	def _animate(self, t_rel):
		title_string = "Playback speed: {}".format(self.play_speed)
		if self.pause: title_string += " (paused)"
		
		time_template = "Time: {} s (UTC {} s)\n"
		time_string = ""
		for imu in self.imus:
			t_abs = imu.time[0] + t_rel
			idx = imu.time_index(t_abs)
			t_abs_act = imu.time[idx]
			t_rel_act = t_abs_act - imu.time[0]
			if not self.aligned:
				time_string += time_template.format(round(t_rel_act, 2), round(t_abs_act, 2))
			if idx == len(imu.time)-1:
				self.done_imus[imu] = True

		if self.aligned: 
			#if the imus are aligned, only one time indication is necessary
			time_string += "Time (aligned): {} s (UTC {} s)\n".format(round(t_rel_act, 2), round(t_abs_act, 2))
		if all(self.done_imus.values()): 
			title_string += "(done)"
		title_string += "\n" + time_string[:-1] # remove new line
		self.title.set_text(title_string)
		pose_arrows = self.plot_pose(t_rel)
		markers = self.plot_markers(t_rel)

		return markers + pose_arrows + [self.title]
		
	def plot_pose(self, t_rel=None):
		try:
			for a in self.pose_arrows: a.remove()
		except:
			print("failed to remove arrows")
		
		prop_cycle = plt.rcParams['axes.prop_cycle']
		colors = prop_cycle.by_key()['color']

		pose_arrows = []
		track_lines = []

		for imu, color in zip(self.imus, colors):
			if not t_rel: 
				i = 0
			else:
				i = imu.time_index(imu.time[0]+t_rel)
			
			
			#start = max([i-100, 0])
			#x_pos, y_pos = imu.pos(start, i)
			#x, y = x_pos[-1], y_pos[-1]
			#print("xy: {},{}".format(x,y))
			#lines = self.ax_pos.plot([x_pos], y_pos) # this messes everything up for some reason
			#lines = self.ax_pos.plot([1,2,3,4,5], [1,2,5,7,9]) # this messes everything up for some reason
			#track_lines.append(lines[0])

			x0, y0, zone_nr, _ = utm.from_latlon(imu.lat[0], imu.long[0])
			x, y, _, _ = utm.from_latlon(imu.lat[i], imu.long[i], force_zone_number=zone_nr)
			x, y = x-x0, y-y0

			yaw = imu.yaw[i]
			yaw = np.pi/2 - yaw # transform from yaw relative north to yaw relative x
			xy_lim = self.ax_pos.get_xlim() # same as ylim
			scale = (xy_lim[1] - xy_lim[0])
			dx = np.cos(yaw)*scale*0.02 #0.05 # magic 
			dy = np.sin(yaw)*scale*0.02 #0.05 # magic
			pose_arrow = self.ax_pos.arrow(x, y, dx, dy, width=scale/150.0, color=color) #/77.0
			pose_arrows.append(pose_arrow)
		self.pose_arrows = pose_arrows + track_lines
		return self.pose_arrows

	def plot_markers(self, t_rel=None):

		try: 
			for m in self.markers: m.remove()
		except: 
			print("failed to remove markers")
			print(m)
		
		prop_cycle = plt.rcParams['axes.prop_cycle']
		colors = prop_cycle.by_key()['color']

		markers = []
		for imu, color in zip(self.imus, colors):
			if not t_rel: 
				i = 0
				t_rel_act = 0
			else:
				t_abs = imu.time[0]
				i = imu.time_index(t_abs+t_rel)
				t_rel_act = imu.time[i] - t_abs
				
			markers.append(self.ax_vx.scatter(t_rel_act, imu.vel_x[i], color="black"))
			markers.append(self.ax_vx.axvline(t_rel_act, color="black"))

			markers.append(self.ax_vy.scatter(t_rel_act, imu.vel_y[i], color="black"))
			markers.append(self.ax_vy.axvline(t_rel_act, color="black"))

			markers.append(self.ax_vz.scatter(t_rel_act, imu.vel_z[i], color="black"))
			markers.append(self.ax_vz.axvline(t_rel_act, color="black"))
		self.markers = markers
		return markers

	def plot_pos(self, t_rel=None):
		for imu in self.imus:
			if not t_rel: 
				idx = len(imu.time)
			else:
				idx = imu.time_index(imu.time[0]+t_rel)+1
			
			x_pos = imu.pos_x[:idx]
			y_pos = imu.pos_y[:idx]
			plt.plot(x_pos[:idx], y_pos[:idx])#, color="lightgray")	
			plt.ylabel("Northings")
			plt.xlabel("Eastings")

	def plot_all(self, t_rel=None):
		# pose
		plt.subplot(2,2,1)
		plt.cla()
		self.plot_pos(t_rel)
		# velocity
		plt.subplot(2,2,2)
		plt.cla()
		self.plot_vel(t_rel)
		# acceleration
		plt.subplot(2,2,3)
		plt.cla()
		self.plot_acc(t_rel)
		# gyroscope
		plt.subplot(2,2,4)
		plt.cla()
		self.plot_gyr(t_rel)

	def plot_pos_err(self, t_rel=None):
		if not t_rel: 
			idx = len(imu.time)
		else:
			idx = imu.time_index(imu.time[0]+t_rel)

	def plot_gps(self, t_rel=None):
		if not t_rel: 
			idx = len(imu.time)
		else:
			idx = imu.time_index(imu.time[0]+t_rel)
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

	def plot_vel(self, t_rel=None):
		for imu in self.imus:
			if not t_rel: 
				i = len(imu.time)
			else:
				i = imu.time_index(imu.time[0]+t_rel)
			time_rel = [t-imu.time[0] for t in imu.time[:i]]
			plt.plot(time_rel, imu.vel_x[:i])
			plt.plot(time_rel, imu.vel_y[:i])
			plt.plot(time_rel, imu.vel_z[:i])
			plt.ylabel("Velocity")
			plt.xlabel("sec")
			plt.legend(["vel_x", "vel_y", "vel_z"])

	def plot_acc(self, t_rel=None):
		for imu in self.imus:
			if not t_rel: 
				i = len(imu.time)
			else:
				i = imu.time_index(imu.time[0]+t_rel)
			plt.plot(imu.time[:i], imu.acc_x[:i])
			plt.plot(imu.time[:i], imu.acc_y[:i])
			plt.plot(imu.time[:i], imu.acc_z[:i])
			plt.ylabel("Acceleration")
			plt.xlabel("sec")
			plt.legend(["acc_x", "acc_y", "acc_z"])

	def plot_gyr(self, t_rel=None):
		for imu in self.imus:
			if not t_rel: 
				i = len(imu.time)
			else:
				i = imu.time_index(imu.time[0]+t_rel)
			plt.plot(imu.time[:i], imu.gyr_x[:i])
			plt.plot(imu.time[:i], imu.gyr_y[:i])
			plt.plot(imu.time[:i], imu.gyr_z[:i])
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