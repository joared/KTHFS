# main.py KTHFormulaStudent

import os

from bisect import bisect_left
import time
import numpy as np
import matplotlib.pyplot as plt

from imu_data_reader import ImuReader, XsensReader, VBOXReader, SBGReader
from data_alignment import align_data, align_time, min_angle_diff
from imu_plotting import plot_sensors, plot_yaw

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
	xsens_path = "XSENS_data"
	#sbg_path = "SBG_data"
	sbg_path = "."
	vbox_path = "VBOX_data"
	#xsens = XsensReader(xsens_path)
	sbg = SBGReader(sbg_path)
	#sbg2 = SBGReader(sbg_path)
	#vbox = VBOXReader(vbox_path)
	
	tests = ["General 8", "General CRC", "Auto 8", "Auto CRC"]
	xsense_files = ["XSENS_general_000.txt", "XSENS_general_crc_0001.txt", "XSENS_auto_0003.txt", "XSENS_auto_crc_0004.txt"]
	sbg_files = ["SBG_general_000.txt", "SBG_general_crc_0001.txt", "SBG_auto_0003.txt", "SBG_auto_crc_0004.txt"]
	vbox_files = ["VBOX0000.VBO", "VBOX0001.VBO", "VBOX0003.VBO", "VBOX0004.VBO"]

	current_test = 0
	sbg_f = sbg_files[current_test]
	#sbg.read(sbg_f, delimiter="\t")
	#sbg.process_data()
	#sbg.save_processed_data(sbg_f)
	#sbg.read_processed_data(sbg_f)
	sbg.read_process_save(sbg_f, delimiter_read="\t", delimiter_save="\t")
	#plot_pos([sbg], True)
	#plot_sensors(sbg)
	plot_yaw([sbg])

	plt.show()
	