# main.py KTHFormulaStudent

import os

from bisect import bisect_left
import time
import numpy as np
import matplotlib.pyplot as plt

from data_alignment import align_time
from imu_recording import ImuRecording
			
if __name__ == '__main__':
	imu = ImuRecording(files_dir="ascii")
	imu.read("general_dead_reck.processed")
	imu.deg_to_rad("yaw")

	imu2 = ImuRecording(files_dir="ascii")
	imu2.read("auto_dead_reck.processed")
	imu2.deg_to_rad("yaw")

	from imu_plotter import ImuPlotter
	p = ImuPlotter([imu, imu2])
	p.play_animation(update_freq=30, play_speed=5)
	#plt.legend(["general", "automotive"])
	plt.show()
	