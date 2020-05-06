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
		self.track_idx = 0
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

		self.figgy = plt.figure()
		self.ax = plt.subplot()

		plt.connect('button_press_event', self.on_click)
		plt.connect('scroll_event', self.on_scroll)
		plt.connect('key_press_event', self.on_key_press)
		#plt.connect('resize_event', self.on_resize)
		
		self.artists = []
		self.done_imus = {imu:False for imu in self.imus}


		self.ani = FuncAnimation(self.figgy, self._animate, self._time_gen, self._init_plot,
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

	def _time_gen_old(self):
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
	

	def _init_plot(self):

		self.ax.cla()
		self.lines = [self.ax.plot([], [])[0] for _ in self.imus]
		self.pose_arrows = [self.ax.arrow(0,0,0,0) for _ in self.imus]
		#plt.axis("equal")
		return self.lines + self.pose_arrows

	def _animate(self, t_rel):
		prop_cycle = plt.rcParams['axes.prop_cycle']
		colors = prop_cycle.by_key()['color']

		#print(t_rel)
		pose_arrows = []

		xylim = self.ax.get_xlim() # same for both x and y
		scale = (xylim[1] - xylim[0])
		# plotting lines and pose arrows
		for imu, line, pose_arrow, color in zip(self.imus, self.lines, self.pose_arrows, colors):
			t_abs = imu.time[0] + t_rel
			idx = imu.time_index(t_abs)

			x, y = imu.pos_x[idx], imu.pos_y[idx]
			line.set_data(imu.pos_x[:idx+1], imu.pos_y[:idx+1])

			pose_arrow.remove()
			yaw = np.pi/2.0 - np.deg2rad(imu.yaw[idx])
			dx = np.cos(yaw)*scale*0.02 #0.05 # magic 
			dy = np.sin(yaw)*scale*0.02 #0.05 # magic
			pose_arrow = self.ax.arrow(x, y, dx, dy, width=scale/150.0, color=color) #/77.0
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
				self.ax.set_ylim(y-10, y+10)
				self.ax.set_xlim(x-10, x+10)
			else:
				max_x = -np.inf
				max_y = -np.inf
				min_x = np.inf
				min_y = np.inf
				for imu in self.imus:
					t_abs = imu.time[0] + t_rel
					idx = imu.time_index(t_abs)
					max_x = max(imu.pos_x[:idx+1] + [max_x])
					min_x = min(imu.pos_x[:idx+1] + [min_x])
					max_y = max(imu.pos_y[:idx+1] + [max_y])
					min_y = min(imu.pos_y[:idx+1] + [min_y])

				x_diff = max_x - min_x
				y_diff = max_y - min_y
				max_diff = max(x_diff, y_diff)
				x_center = min_x + x_diff/2.0
				y_center = min_y + y_diff/2.0
				print(scale/20)
				max_diff += scale/20
				
				self.ax.set_xlim(x_center-max_diff/2.0, x_center+max_diff/2.0)
				self.ax.set_ylim(y_center-max_diff/2.0, y_center+max_diff/2.0)
		self.ax.set_aspect('equal', 'box')
		
		return self.lines + self.pose_arrows 



if __name__ == "__main__":
	from imu_reader import read_sbg, read_vbox, read_xsens
	sbg = read_sbg("SBG_general_000.txt", "\t", files_dir="ascii")
	sbg2 = read_sbg("auto_dead_reck.txt", "\t", files_dir="ascii")
	vbox = read_vbox("VBOX0000.VBO", " ", files_dir="ascii")
	#xsens = read_vbox("", "\t", files_dir="ascii")
	plotter = ImuPlotter([sbg, sbg2, vbox])
	plotter.play_animation()
	plotter.show()
	#Writer = animation.writers['ffmpeg']
	#writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
	#plotter.ani.save("test.mp4")