# main.py KTHFormulaStudent

import os
import matplotlib.pyplot as plt
from bisect import bisect_left
import time
import numpy as np

from imu_data_reader import XsensReader, VBOXReader, SBGReader
from data_alignment import align_data, align_time, min_angle_diff

def plot_pos(imus):
	for imu in imus:
		plt.plot(imu.latitude, imu.longitude)
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



def plot_angle_error_vs_slip_angle(ref_imu, comp_imus):
	#colors = ["blue", "orange", "green"]
	
	#plt.subplot(2,1,1)
	plt.ylim([-20, 20])
	plt.plot(ref_imu.time_aligned, ref_imu.slip_angle_aligned)
	for imu in comp_imus:
		sq_errs = []
		for i, yaw_actual in enumerate(ref_imu.yaw_aligned):
			err = min_angle_diff(180, -180, yaw_actual, imu.yaw_aligned[i])
			sq_err = err**2
			sq_errs.append(err)
		print("Plotting")
		plt.plot(ref_imu.time_aligned, sq_errs)
	plt.legend([ref_imu.NAME + " <slip angle>"] + [imu.NAME + " yaw err"  for imu in comp_imus])
	#plt.subplot(2,1,2)
	#plt.ylim([-20, 20])
	#plt.plot(ref_imu.slip_angle)	
		
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
	sbg_path = "SBG_data"
	vbox_path = "VBOX_data"
	xsens = XsensReader(xsens_path)
	sbg = SBGReader(sbg_path)
	vbox = VBOXReader(vbox_path)
	
	tests = ["General 8", "General CRC", "Auto 8", "Auto CRC"]
	xsense_files = ["XSENS_general_000.txt", "XSENS_general_crc_0001.txt", "XSENS_auto_0003.txt", "XSENS_auto_crc_0004.txt"]
	sbg_files = ["SBG_general_0000.txt", "SBG_general_crc_0001.txt", "SBG_auto_0003.txt", "SBG_auto_crc_0004.txt"]
	vbox_files = ["VBOX0000.VBO", "VBOX0001.VBO", "VBOX0003.VBO", "VBOX0004.VBO"]
	
	
	i = 0
	for test, f_xsens, f_sbg, f_vbox in zip(tests, xsense_files, sbg_files, vbox_files):
		#xsens.read(f_xsens)
		#sbg.read(f_sbg)
		#vbox.read(f_vbox)
		
		#plt.subplot(4, 2, i*2+1)
		#plot_pos([xsens, vbox])
		#plt.ylabel(test)
		#plt.subplot(4, 2, i*2+2)
		#plot_pos([sbg, vbox])
		
		#plot_velocity_and_yaw([xsens, vbox])
		break
		i += 1

	current_test = 0
	xsens.read(xsense_files[current_test])
	sbg.read(sbg_files[current_test])
	vbox.read(vbox_files[current_test])
	

	#xsens_vel = []
	#for i in range(len(xsens.vel_inc_x)):
	#	xsens_vel.append(sum(xsens.vel_inc_x[:i]))
	#xsens.vel_x = xsens_vel

	imus = [sbg, xsens, vbox]
	[sbg, xsens, vbox] = align_time(imus)

	#align_data([sbg, xsens, vbox], vel_x=True)
	attrs_to_align = ["yaw"]
	sbg.align_data(attrs_to_align)
	xsens.align_data(attrs_to_align)
	vbox.align_data(attrs_to_align + ["slip_angle"])

	
	# numpy for calculation plots
	vbox_temp = np.array(vbox.yaw_aligned)	
	sbg_temp = np.array(sbg.yaw_aligned)
	xsens_temp = np.array(xsens.yaw_aligned)

	diff_sbg = vbox_temp - sbg_temp
	diff_xsens = vbox_temp - xsens_temp

	avg_sbg = np.sum(diff_sbg)/np.size(diff_sbg)
	avg_xsens = np.sum(diff_xsens)/np.size(diff_xsens)

	print(avg_sbg)
	print(avg_xsens)

	#for imu in imus:
	#	plt.plot(imu.yaw_aligned)
	#plt.legend([imu.NAME for imu in imus])
	
	plot_angle_error_vs_slip_angle(vbox, [sbg, xsens])
	
	#plt.plot(xsens.time, xsens.vel_inc_x)
	plt.show()
	