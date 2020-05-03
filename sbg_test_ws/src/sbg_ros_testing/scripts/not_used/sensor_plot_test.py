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
				  	   update_freq=30, play_speed=1, start_time=0, blit=True):
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


		self.ani = FuncAnimation(self.figgy, self._animate, self._time_gen, self._init_plot,
				 				 interval=interval, blit=blit, repeat=False)

		# when calling plt.show after this 
		# an error occurs. This solves it, might be a bug.
		self.figgy.canvas.draw()

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
	

	def _init_plot(self):
		self.ax = plt.subplot()
		#self.ax.set_ylim((0, max(self.imus[0].vel_x)))
		self.ax.set_xlim((0, 30))
		self.ax.plot([])
		self.lines = [self.ax.plot([], [])[0] for _ in self.imus]
		return self.lines

	def _animate(self, t_rel):
		print(t_rel)
		for line, imu in zip(self.lines, self.imus):
			t_abs = imu.time[0] + t_rel
			idx = imu.time_index(t_abs)
			t_abs_act = imu.time[idx]
			start = max([idx-2000, 0])
			times = [t-imu.time[0] for t in imu.time[start:idx+1]]
			times = [t-times[0] for t in times]
			values = imu.vel_x[start:idx+1]
			mean = sum(values)/len(values)
			maximum = max(values)
			minimum = min(values)
			line.set_data(times, values)
			#t_rel_act = t_abs_act - imu.time[0]
		ylim = self.ax.get_ylim()
		self.ax.set_ylim((min([ylim[0], minimum]), max([ylim[1], maximum])))
		return self.lines



if __name__ == "__main__":
	from imu_recording import *
	imu = SBGRecording(files_dir="ascii")
	imu.read("SBG_general_000.processed")
	plotter = ImuPlotter([imu])
	plotter.play_animation()
	plotter.show()