import matplotlib.pyplot as plt

def plot_pos(imus, real_time=False):
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
			plt.plot(imu.time_aligned, imu.yaw_aligned)
	plt.legend([imu.NAME + " yaw"  for imu in imus])
