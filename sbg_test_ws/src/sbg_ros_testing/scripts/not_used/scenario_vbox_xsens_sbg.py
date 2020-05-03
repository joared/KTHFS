# main.py KTHFormulaStudent

import os

from bisect import bisect_left
import time
import numpy as np
import matplotlib.pyplot as plt

from data_alignment import align_time
from imu_recording import ImuRecording, SBGRecording, VBOXRecording, XsensRecording
#from data_alignment import align_data, align_time, min_angle_diff
#from imu_plotting import plot_sensors, plot_yaw

			
if __name__ == '__main__':
	xsens_files = ["XSENS_general_000.txt", "XSENS_general_crc_0001.txt", "XSENS_auto_0003.txt", "XSENS_auto_crc_0004.txt"]
	sbg_files = ["SBG_general_000.txt", "SBG_general_crc_0001.txt", "SBG_auto_0003.txt", "SBG_auto_crc_0004.txt"]
	vbox_files = ["VBOX0000.VBO", "VBOX0001.VBO", "VBOX0003.VBO", "VBOX0004.VBO"]
	current_test = 0

	sbg = SBGRecording(files_dir="ascii")
	xsens = XsensRecording(files_dir="ascii")
	vbox = VBOXRecording(files_dir="ascii")

	#sbg.read(sbg_files[current_test])
	#vbox.read(vbox_files[current_test], delimiter=" ")
	#xsens.read(xsens_files[current_test])

	sbg.deg_to_rad("yaw")
	vbox.deg_to_rad("yaw")
	xsens.deg_to_rad("yaw")

	sbg.read("SBG_general_000.processed")
	vbox.read("VBOX0000.processed")
	#xsens.read("XSENS_general_000.processed")

	#t = align_time([sbg, vbox, xsens])
	#keys = ["yaw", "lat", "long"]
	#sbg.align_data(t)#, keys)
	#vbox.align_data(t)#, keys)
	#xsens.align_data(t, keys)
	
	#sbg.save(sbg_files[current_test])
	#vbox.save(vbox_files[current_test])
	#xsens.save(xsens_files[current_test])

	from imu_plotter import ImuPlotter
	#p = ImuPlotter([vbox, xsens, sbg])
	p = ImuPlotter([sbg])
	p.play_animation(update_freq=60, play_speed=1, start_time=0)
	#p.plot_pos()
	p.show()
	#Writer = animation.writers['ffmpeg']
	#writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
	#p.ani.save("test.mp4")
	