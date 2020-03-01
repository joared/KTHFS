# main.py KTHFormulaStudent

import os
import matplotlib.pyplot as plt
from bisect import bisect_left
import time
import numpy as np

from imu_data_reader import XsensReader, VBOXReader, SBGReader
from data_alignment import align_data, align_time

def plot_pos(imus):
	for imu in imus:
		plt.plot(imu.latitude, imu.longitude)
	plt.legend([imu.NAME for imu in imus])

def plot_velocity_and_yaw(imus):
	for imu in imus:
		plt.subplot(3, 1, 1)
		plt.plot(imu.vel_x)
		plt.ylabel("Velocity X")
		plt.legend([imu.NAME])
		plt.subplot(3, 1, 2)
		plt.plot(imu.vel_y)
		plt.ylabel("Velocity Y")
		plt.subplot(3, 1, 3)
		plt.plot(imu.yaw)
		plt.ylabel("Yaw")
	
def plot_pos_real_time(imus):
	# Doesn't work
	n = len(imus)
	min_n_data = min([len(imu.latitude) for imu in imus])
	
	min_n_data = 1000
	x = range(1000)
	y = range(1000)
	
	for i in range(min_n_data):
		for imu in imus:
			#plt.scatter(imu.latitude[i], imu.longitude[i])
			if i == 0:
				#plt.plot(imu.latitude[i], imu.longitude[i])
				pass
			else:
				#plt.plot(imu.latitude[i-1:i], imu.longitude[i-1:i])
				plt.scatter(imu.latitude[i], imu.longitude[i])
				#plt.plot(x[i-1:i], y[i-1:i])
				#plt.scatter(x[i], y[i])
				
			plt.pause(0.05)
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


def normalize_angles(angles):
	new_angles = np.array([])
	for angle in angles:
		new_angle = angle
		if new_angle <= -180:
			new_angle += 360
		elif new_angle > 180:
			new_angle -= 360
		new_angles = np.append(new_angles, new_angle)
	return new_angles



	
if __name__ == '__main__':
	xsens_path = "XSENS_data"
	sbg_path = "SBG_data"
	vbox_path = "VBOX_data"
	xsens = XsensReader(xsens_path)
	sbg = SBGReader(sbg_path)
	vbox = VBOXReader(vbox_path)
	
	tests = ["General 8", "General CRC", "Auto 8", "Auto CRC"]
	xsense_files = ["XSENS_general_000.txt", "XSENS_general_crc_0001.txt", "XSENS_auto_0003.txt", "XSENS_auto_crc_0004.txt"]
	sbg_files = ["SBG_general_000.txt", "SBG_general_crc_0001.txt", "SBG_auto_0003.txt", "SBG_auto_crc_0004.txt"]
	vbox_files = ["VBOX0000.VBO", "VBOX0001.VBO", "VBOX0003.VBO", "VBOX0004.VBO"]
	
	
	i = 0
	for test, f_xsens, f_sbg, f_vbox in zip(tests, xsense_files, sbg_files, vbox_files):
		
		if i in[0]:
			plt.figure()
			xsens.read(f_xsens)
			sbg.read(f_sbg)
			vbox.read(f_vbox)
			
			
			#plt.subplot(4, 2, i*2+1)
			#plot_pos([xsens, vbox])
			plt.ylabel(test)
			#plt.subplot(4, 2, i*2+2)
			#plot_pos([sbg, xsens, vbox])
			plt.plot(sbg.vel_x)
			v_x = np.array(sbg.data["X Velocity"])
			v_y = np.array(sbg.data["Y Velocity"])
			v_tot = np.sqrt(v_x*v_x+v_y*v_y)
			plt.plot(v_tot)
			plt.plot(sbg.vel_y)
			
			#plot_velocity_and_yaw([xsens, vbox])
			
			#break
		i += 1
	plt.show()	
"""
	current_test = 0
	xsens.read(xsense_files[current_test])
	sbg.read(sbg_files[current_test])
	vbox.read(vbox_files[current_test])

	xsens_vel = []
	for i in range(len(xsens.vel_inc_x)):
		xsens_vel.append(sum(xsens.vel_inc_x[:i]))
	xsens.vel_x = xsens_vel

	imus = [sbg, xsens, vbox]
	[sbg, xsens, vbox] = align_time(imus)

	aligned_imus = align_data([sbg, xsens, vbox], vel_x=True)
	sbg = aligned_imus[0]
	xsens = aligned_imus[1]
	vbox = aligned_imus[2]

	# numpy for calculation plots
	vbox_temp = 1000/(60*60)*np.array(vbox.vel_x_aligned)
	#vbox_temp = np.array(vbox.vel_x_aligned)
	sbg_temp = np.array(sbg.vel_x_aligned)
	xsens_temp = np.array(xsens.vel_x_aligned)	
	#xsens_temp = np.array(xsens.yaw_aligned)*-1+93

	#vbox_temp = normalize_angles(vbox_temp)
	#xsens_temp = normalize_angles(xsens_temp)

	diff_sbg = np.abs(vbox_temp - sbg_temp)
	diff_xsens = np.abs(vbox_temp - xsens_temp)
	#print(diff_sbg[4000:4200])

	avg_sbg = np.sum(diff_sbg)/np.size(diff_sbg)
	avg_xsens = np.sum(diff_xsens)/np.size(diff_xsens)

	print("Average error SBG: {}".format(avg_sbg))
	print("Average error Xsens: {}".format(avg_xsens))

	plt.plot(sbg.time_aligned, sbg_temp, label='SBG')
	plt.plot(vbox.time_aligned, vbox_temp, label='VBOX')
	plt.plot(xsens.time_aligned, xsens_temp, label='Xsens')
	plt.legend()
	plt.ylabel("v_x [m/s]")
	plt.xlabel("UTC Time [s]")
	plt.show()
	"""
	