import matplotlib.pyplot as plt

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
	
	
def print_keys(imu):
	# Prints all data types from imu
	for k in imu.data_keys:
		print(k)

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