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
		self.pose_arrows = []

		self.pos_fig = None # position and gps
		self.vel_fig = None 
		self.acc_fig = None
		#self.wheel_fig = None

		# live plotting attributes
		self.update_freq = None
		self.play_speed = None
		self.pause = False
		self.reset = False
		self.start_time = None

	def show(self):
		plt.show()

	def on_click(self, event):
		print(event)

	def on_key_press(self, event):
		k = event.key
		if k in ["p", " "]:
			self.pause = not self.pause
		elif k == "+":
			self.play_speed += 0.5
		elif k == "-":
			self.play_speed -= 0.5
		elif k == "r":
			self.reset = True
		elif k in [str(i) for i in range(1,10)]:
			self.play_speed = int(k)

	def on_scroll(self, event):
		self.t_rel += event.step

	def play_animation(self, pos=False, vel=False, acc=False,
				  	   update_freq=30, play_speed=1, start_time=0, blit=True):
		interval = 1.0/update_freq*1000
		self.update_freq = update_freq
		self.play_speed = play_speed
		self.pause = False
		self.reset = False
		self.start_time = start_time

		self.figgy = plt.figure()
		#title = fig.suptitle(time_string)
		plt.connect('button_press_event', self.on_click)
		plt.connect('scroll_event', self.on_scroll)
		plt.connect('key_press_event', self.on_key_press)
		
		#plt.connect('xlim_changed', lambda event: self.ani._blit_cache.clear())
		#plt.connect('ylim_changed', lambda event: self.ani._blit_cache.clear())
		#plt.connect('resize_event', self.on_resize)
		
		self.artists = []
		self.done_imus = {imu:False for imu in self.imus}

		#self._init_plot()
		self.ani = FuncAnimation(self.figgy, self._animate, self._time_gen, self._init_plot,
								 interval=interval, blit=blit, repeat=False)

		# when calling plt.show after this 
		# an error occurs. This solves it, might be a bug.
		self.figgy.canvas.draw()

	def _init_plot(self):
		
		ax = plt.subplot(1, 4, 1)
		plt.cla()
		self.title = ax.text(0, 0, 'matplotlib', horizontalalignment="left",
							 verticalalignment="bottom", transform=ax.transAxes)
		self.plot_pos()
		#pose_arrows = self.plot_pose()
		
		plt.axis("equal")
		plt.legend([imu.name for imu in self.imus])
		#self.figgy.add_subplot(self.gs[0, 1]) # vx
		plt.subplot(1, 4, 2)
		plt.cla()
		rel_times = [[t-imu.time[0] for t in imu.time] for imu in self.imus]
		for rel_time, imu in zip(rel_times, self.imus): plt.plot(rel_time, imu.vel_x)
		#self.figgy.add_subplot(self.gs[0, 2]) # vy
		plt.subplot(1, 4, 3)
		plt.cla()
		for rel_time, imu in zip(rel_times, self.imus): plt.plot(rel_time, imu.vel_y)
		#self.figgy.add_subplot(self.gs[0, 3]) # vz
		plt.subplot(1, 4, 4)
		plt.cla()
		for rel_time, imu in zip(rel_times, self.imus): plt.plot(rel_time, imu.vel_z)
		#markers = self.plot_markers()
		#return pose_arrows + markers
		return []

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
			elif self.reset:
				self.done_imus = {imu:False for imu in self.imus}
				self.t_rel = 0
				self.reset = False
			elif self.pause:
				# dont change t_rel
				time_ref = time.time()
			else:
				curr_time = time.time()
				self.t_rel = self.t_rel + (curr_time - time_ref)*self.play_speed
				self.t_rel = max([self.t_rel, 0])
				self.t_rel = min([self.t_rel, max([imu.time[-1]-imu.time[0] for imu in self.imus])])
				time_ref = curr_time
			yield self.t_rel

	def _animate(self, t_rel):
		#t_rel = (time.time() - self.start_time)*self.play_speed
		#self.clear()
		title_string = "Playback speed: {}".format(self.play_speed)
		if self.pause: title_string += " (paused)"
		title_string += "\n"
		for imu in self.imus:
			#if self.done_imus[imu]:
			#	t_abs_act = imu.time[-1]
			#	t_rel_act = t_abs_act - imu.time[0]
			#	time_string += "Time: {} s (UTC {} s)\n".format(round(t_rel_act, 2), round(t_abs_act, 2))
			#	continue
			t_abs = imu.time[0] + t_rel
			idx = imu.time_index(t_abs)
			t_abs_act = imu.time[idx]
			t_rel_act = t_abs_act - imu.time[0]
			title_string += "Time: {} s (UTC {} s)\n".format(round(t_rel_act, 2), round(t_abs_act, 2))
			if idx == len(imu.time)-1:
				print(imu.name + " done: " + str(t_rel_act))
				self.done_imus[imu] = True
			
		plt.figure(self.figgy.number)
		self.title.set_text(title_string)
		

		plt.subplot(1, 4, 1)
		pose_arrows = self.plot_pose(t_rel)
		markers = self.plot_markers(t_rel)
		
		if all(self.done_imus.values()):
			pass
			#self.ani.event_source.stop()
		self.artists = markers + pose_arrows + [self.title]
		return self.artists
		
	def plot_pose(self, t_rel=None):
		try:
			for a in self.pose_arrows: a.remove()
		except:
			print("failed to remove arrows")
		pose_arrows = []

		prop_cycle = plt.rcParams['axes.prop_cycle']
		colors = prop_cycle.by_key()['color']

		for imu, color in zip(self.imus, colors):
			if not t_rel: 
				i = 0
			else:
				i = imu.time_index(imu.time[0]+t_rel)
			
			x0, y0, zone_nr, _ = utm.from_latlon(imu.lat[0], imu.long[0])
			x, y, _, _ = utm.from_latlon(imu.lat[i], imu.long[i], force_zone_number=zone_nr)
			x, y = x-x0, y-y0

			yaw = imu.yaw[i]
			yaw = np.pi/2 - yaw # transform from yaw relative north to yaw relative x
			dx = np.cos(yaw)*5 #100
			dy = np.sin(yaw)*5 #100
			pose_arrow = plt.arrow(x, y, dx, dy, width=1, color=color) #width=20
			pose_arrows.append(pose_arrow)
		self.pose_arrows = pose_arrows
		return pose_arrows

	def plot_markers(self, t_rel=None):
		for i in range(3):
			plt.subplot(1, 4, 2+i)
			try: 
				for m in self.markers: m.remove()
			except: pass
		markers = []
		prop_cycle = plt.rcParams['axes.prop_cycle']
		colors = prop_cycle.by_key()['color']
		for imu, color in zip(self.imus, colors):
			if not t_rel: 
				i = 0
				t_rel_act = 0
			else:
				t_abs = imu.time[0]
				i = imu.time_index(t_abs+t_rel)
				t_rel_act = imu.time[i] - t_abs

			
			plt.subplot(1, 4, 2)
			markers.append(plt.scatter(t_rel_act, imu.vel_x[i], color="black"))
			markers.append(plt.axvline(t_rel_act, color="black"))
			plt.subplot(1, 4, 3)
			markers.append(plt.scatter(t_rel_act, imu.vel_y[i], color="black"))
			markers.append(plt.axvline(t_rel_act, color="black"))
			plt.subplot(1, 4, 4)
			markers.append(plt.scatter(t_rel_act, imu.vel_z[i], color="black"))
			markers.append(plt.axvline(t_rel_act, color="black"))
		self.markers = markers
		return markers

	def plot_pos(self, t_rel=None):
		for imu in self.imus:
			if not t_rel: 
				idx = len(imu.time)
			else:
				idx = imu.time_index(imu.time[0]+t_rel)
			
			x_pos, y_pos = imu.pos(idx)
			plt.plot(x_pos[:idx], y_pos[:idx])	
			
			# Temp, scatter first and last 0 occcurance in gps signal
			"""
			plt.scatter(x_pos[imu.gps_long.index(0)],
						y_pos[imu.gps_lat.index(0)], color="r")
			rev_long = list(reversed(imu.gps_long[:i]))
			rev_lat = list(reversed(imu.gps_lat[:i]))
			#rev_long = list(reversed(imu.gps_long))
			#rev_lat = list(reversed(imu.gps_lat))
			plt.scatter(list(reversed(x_pos))[rev_long.index(0)],
						list(reversed(y_pos))[rev_lat.index(0)], color="g")
			"""
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