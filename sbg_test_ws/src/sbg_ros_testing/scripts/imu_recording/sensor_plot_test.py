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
		self.track_idx = None
		self.free_panning = False

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
			self.play_speed = 1
		elif k == "z":
			self.free_panning = not self.free_panning
			self.track_idx = None
		elif k in [str(i) for i in range(1,10)]:
			self.free_panning = False
			if int(k) <= len(self.imus):
				self.track_idx = int(k)-1

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

		gs = gridspec.GridSpec(3, 3)
		self.figgy = plt.figure()
		self.ax_pose = plt.subplot(gs[:2, :2])
		self.ax_vel = plt.subplot(gs[2, :2])
		#self.info_text = self.ax_pose.text(0, 0, 'time info', horizontalalignment="left",
		#					 		  verticalalignment="bottom", transform=self.ax_pose.transAxes)

		plt.connect('button_press_event', self.on_click)
		plt.connect('scroll_event', self.on_scroll)
		plt.connect('key_press_event', self.on_key_press)
		#plt.connect('resize_event', self.on_resize)
		
		self.done_imus = {imu:False for imu in self.imus}
		self.ani = FuncAnimation(self.figgy, self._update, self._time_gen, self._init_plot,
				 				 interval=interval, blit=blit, repeat=False)

		# when calling plt.show after this 
		# an error occurs. This solves it, might be a bug.
		self.figgy.canvas.draw()

	def _time_gen(self):
		
		# change to start time
		self.t_rel = 0
		self.start_time = 0 # only want to start here the first time
		interval = 1.0/float(self.update_freq)
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
				pass
			else:
				self.t_rel = self.t_rel + interval*self.play_speed
				self.t_rel = max([self.t_rel, 0])
				self.t_rel = min([self.t_rel, max([imu.time[-1]-imu.time[0] for imu in self.imus])])
			yield self.t_rel
	

	def _init_plot(self):
		# init pose plot
		self.ax_pose.cla()
		self.lines = [self.ax_pose.plot([], [])[0] for _ in self.imus]
		self.next_lines = [self.ax_pose.plot([], [], color="lightgray")[0] for _ in self.imus]
		self.pose_arrows = [self.ax_pose.arrow(0,0,0,0) for _ in self.imus]

		# init velocity plot
		self.ax_vel.cla()
		self.ax_vel.plot(self.imus[0].vel_x)
		self.ax_vel.cla()
		min_vx = min(min([imu.vel_x for imu in self.imus]))
		max_vx = max(max([imu.vel_x for imu in self.imus]))
		min_vy = min(min([imu.vel_y for imu in self.imus]))
		max_vy = max(max([imu.vel_y for imu in self.imus]))
		min_y = min([min_vx, min_vy])
		max_y = max([max_vx, max_vy])
		min_x = 0
		max_x = max([imu.time[-1] - imu.time[0] for imu in self.imus])
		self.ax_vel.set_xlim(min_x, max_x)
		self.ax_vel.set_ylim(min_y, max_y)
		self.vel_x = [self.ax_vel.plot([], [])[0] for _ in self.imus]
		self.vel_y = [self.ax_vel.plot([], [])[0] for _ in self.imus]
		self.vel_x_vlines = [self.ax_vel.axvline(color="black") for _ in self.imus]
		

		return self.lines + self.next_lines + self.pose_arrows + self.vel_x + self.vel_y + self.vel_x_vlines

	def _update(self, t_rel):
		
		pose_artists = self._update_pose(t_rel)
		vel_artists = self._update_vel(t_rel)

		return pose_artists + vel_artists

	def _update_pose(self, t_rel):
		prop_cycle = plt.rcParams['axes.prop_cycle']
		colors = prop_cycle.by_key()['color']
		pose_arrows = []
		xylim = self.ax_pose.get_xlim() # same for both x and y
		scale = (xylim[1] - xylim[0])
		# plotting lines and pose arrows
		for imu, line, n_line, pose_arrow, color in zip(self.imus, self.lines, self.next_lines, self.pose_arrows, colors):
			t_abs = imu.time[0] + t_rel
			idx = imu.time_index(t_abs)

			x, y = imu.pos_x[idx], imu.pos_y[idx]

			line.set_data(imu.pos_x[:idx+1], imu.pos_y[:idx+1])
			n_line.set_data(imu.pos_x[idx:], imu.pos_y[idx:])
			#n_line.set_color("lightgray")

			pose_arrow.remove()
			yaw = np.pi/2.0 - np.deg2rad(imu.yaw[idx])
			dx = np.cos(yaw)*scale*0.02 #0.05 # magic 
			dy = np.sin(yaw)*scale*0.02 #0.05 # magic
			pose_arrow = self.ax_pose.arrow(x, y, dx, dy, width=scale/150.0, color=color) #/77.0
			pose_arrows.append(pose_arrow)
		self.pose_arrows = pose_arrows

		# changing axis limits
		if not self.free_panning:
			if self.track_idx is not None:
				imu = self.imus[self.track_idx]
				t_abs = imu.time[0] + t_rel
				idx = imu.time_index(t_abs)
				x = imu.pos_x[idx]
				y = imu.pos_y[idx]
				self.ax_pose.set_ylim(y-10, y+10)
				self.ax_pose.set_xlim(x-10, x+10)
			else:
				max_x = -np.inf
				max_y = -np.inf
				min_x = np.inf
				min_y = np.inf
				for imu in self.imus:
					#t_abs = imu.time[0] + t_rel
					#idx = imu.time_index(t_abs) # to adjust to data unitl t_rel
					idx = len(imu.time)-1 # to adjust to all data
					max_x = max(imu.pos_x[:idx+1] + [max_x])
					min_x = min(imu.pos_x[:idx+1] + [min_x])
					max_y = max(imu.pos_y[:idx+1] + [max_y])
					min_y = min(imu.pos_y[:idx+1] + [min_y])

				x_diff = max_x - min_x
				y_diff = max_y - min_y
				max_diff = max(x_diff, y_diff)
				x_center = min_x + x_diff/2.0
				y_center = min_y + y_diff/2.0
				max_diff += scale/20
				
				self.ax_pose.set_xlim(x_center-max_diff/2.0, x_center+max_diff/2.0)
				self.ax_pose.set_ylim(y_center-max_diff/2.0, y_center+max_diff/2.0)
		self.ax_pose.set_aspect('equal', 'box')
		
		return self.lines + self.next_lines + self.pose_arrows 

	def _update_vel(self, t_rel):
		for i, imu in enumerate(self.imus):
			t_abs = imu.time[0] + t_rel
			idx = imu.time_index(t_abs)
			t_rel_act = imu.time[idx] - t_abs

			time = [t - imu.time[0] for t in imu.time[:idx+1]]
			#print(len(time))
			#print(len(imu.vel_x[:idx+1]))
			self.vel_x[i].set_data(time, imu.vel_x[:idx+1])
			self.vel_y[i].set_data(time, imu.vel_y[:idx+1])
			
			self.vel_x_vlines[i].set_data([t_rel_act, t_rel_act], [t_rel_act, 0])
			#markers.append(self.ax_vx.scatter(t_rel_act, imu.vel_x[i], color="black"))
			#markers.append(self.ax_vx.axvline(t_rel_act, color="black"))
			#markers.append(self.ax_vy.scatter(t_rel_act, imu.vel_y[i], color="black"))
			#markers.append(self.ax_vy.axvline(t_rel_act, color="black"))
		return self.vel_x + self.vel_y + self.vel_x_vlines

if __name__ == "__main__":
	from imu_reader import read_sbg, read_vbox, read_xsens
	sbg = read_sbg("SBG_general_000.txt", "\t", files_dir="ascii")
	sbg2 = read_sbg("auto_dead_reck.txt", "\t", files_dir="ascii")
	vbox = read_vbox("VBOX0000.VBO", " ", files_dir="ascii")
	#xsens = read_vbox("", "\t", files_dir="ascii")
	plotter = ImuPlotter([vbox, sbg])#, sbg2])
	plotter.play_animation()
	
	# to just plot everything
	#plotter.ax = plt.subplot()
	#plotter._init_plot()
	#plotter._animate(1000)

	plotter.show()
	#Writer = animation.writers['ffmpeg']
	#writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
	#plotter.ani.save("test.mp4")