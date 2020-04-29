# main.py KTHFormulaStudent

import os

from bisect import bisect_left
import time
import numpy as np
import matplotlib.pyplot as plt

from imu_recording import ImuRecording
#from data_alignment import align_data, align_time, min_angle_diff
#from imu_plotting import plot_sensors, plot_yaw

def __plot_angle_squared_error(ref_imu, comp_imus):
	#colors = ["blue", "orange", "green"]
	#plt.ylim(top=30000)
	plt.xlim([min(ref_imu.time_aligned), max(ref_imu.time_aligned)])
	for i, yaw_actual in enumerate(ref_imu.yaw_aligned):
		for imu in comp_imus:
			
			err = min_angle_diff(180, -180, yaw_actual, imu.yaw_aligned[i])
			sq_err = err**2
			plt.scatter(ref_imu.time_aligned[i], sq_err)
		plt.pause(0.00001)
	#plt.legend([imu.NAME for imu in comp_imus])	
			
if __name__ == '__main__':
	#xsens_path = "XSENS_data"
	#sbg_path = "SBG_data"
	#sbg_path = "."
	#vbox_path = "VBOX_data"
	#xsens = XsensReader(xsens_path)
	#sbg = SBGRecording(sbg_path)
	#vbox = VBOXReader(vbox_path)
	
	#tests = ["General 8", "General CRC", "Auto 8", "Auto CRC"]
	#xsense_files = ["XSENS_general_000.txt", "XSENS_general_crc_0001.txt", "XSENS_auto_0003.txt", "XSENS_auto_crc_0004.txt"]
	#sbg_files = ["SBG_general_000.txt", "SBG_general_crc_0001.txt", "SBG_auto_0003.txt", "SBG_auto_crc_0004.txt"]
	#vbox_files = ["VBOX0000.VBO", "VBOX0001.VBO", "VBOX0003.VBO", "VBOX0004.VBO"]

	#current_test = 0
	#sbg_f = sbg_files[current_test]

	imu = ImuRecording("ascii")
	imu.read("general_dead_reck.processed")
	imu.deg_to_rad("yaw")

	imu2 = ImuRecording("ascii")
	imu2.read("auto_dead_reck.processed")
	imu2.deg_to_rad("yaw")
	#imu.align_freq(1)
	#plt.plot(imu.long, imu.lat)
	#plt.show()
	from imu_plotter import ImuPlotter
	p1 = ImuPlotter(imu)
	p2 = ImuPlotter(imu2)
	#plotter.plot_play(1, start_time=0)
	#plotter.show()
	#imu.plot_all()
	
	p1.plot_play(update_freq=30, play_speed=5)
	p2.plot_play(update_freq=30, play_speed=5)
	#p2.plot_gps()
	#p2.plot_pose()
	#plt.xlim(-1850, 0)
	#plt.xlim(-4300, 110)
	#plt.ylim(-10, 4400)
	#plt.axis("equal")
	plt.legend(["general", "automotive"])
	plt.show()
	