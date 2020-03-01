import numpy as np
from bisect import bisect_left


def align_time(imus):
	"""
	Add aligned time to start at same time with the same frequency
	
	input: list with the imus objects in the order [SBG, Xsens, VBOX]
	output: imu objects with aligned time data field
	"""
	sbg = imus[0]
	xsens = imus[1]
	vbox = imus[2]
	start_time = max([sbg.time[0], xsens.time[0], vbox.time[0]])
	end_time = min([sbg.time[-1], xsens.time[-1], vbox.time[-1]])

	# Find highest frequency signal
	sbg_period = sbg.time[2]-sbg.time[1]
	xsens_period = xsens.time[2]-xsens.time[1]
	vbox_period = vbox.time[2]-vbox.time[1]
	imu_periods = [sbg_period, xsens_period, vbox_period]
	min_period = min(imu_periods)
	min_period_imu = imus[imu_periods.index(min_period)]

	# Align start and end time for highest frequency signal
	start_index = closest_index(min_period_imu.time, start_time) + 1 # +1 and -1 only to guarantee valid values/index
	end_index = closest_index(min_period_imu.time, end_time) - 1
	new_time = min_period_imu.time[start_index:end_index]
	
	# Add new aligned time attribute to every imu
	sbg.time_aligned = new_time
	xsens.time_aligned = new_time
	vbox.time_aligned = new_time

	updated_imus = [sbg, xsens, vbox]
	return updated_imus

def align_data(imus, vel_x=False, vel_y=False, latitude=False, longitude=False, yaw=False):
	"""
	Align the datafields set to True

	Input: list of the IMU objects in order [sbg, xsens, vbox], the IMUs NEED to be processed by align_time first!
	Output: A list of the updated IMUs with new attributes DATAFIELD_aligned of the datafields set to true
	"""

	#sbg = imus[0]
	#xsens = imus[0]
	#vbox = imus[0]

	# Align x velocity
	if vel_x:
		for imu in imus:
			aligned_velocity = []
			for t in imu.time_aligned:
				# Find the previous value
				prev_index = closest_index(imu.time, t)
				prev_time = imu.time[prev_index]
				prev_velocity = imu.vel_x[prev_index]

				# Find the next value
				next_index = prev_index + 1
				next_time = imu.time[next_index]
				next_velocity = imu.vel_x[next_index]

				# Interpolate the value to requested time t
				interpolated_velocity = interpolate_linear(prev_velocity, next_velocity, prev_time, next_time, t)
				aligned_velocity.append(interpolated_velocity)
			imu.vel_x_aligned = aligned_velocity

	# Align y velocity
	if vel_y:
		for imu in imus:
			aligned_velocity = []
			for t in imu.time_aligned:
				# Find the previous value
				prev_index = closest_index(imu.time, t)
				prev_time = imu.time[prev_index]
				prev_velocity = imu.vel_y[prev_index]

				# Find the next value
				next_index = prev_index + 1
				next_time = imu.time[next_index]
				next_velocity = imu.vel_y[next_index]

				# Interpolate the value to requested time t
				interpolated_velocity = interpolate_linear(prev_velocity, next_velocity, prev_time, next_time, t)
				aligned_velocity.append(interpolated_velocity)
			imu.vel_y_aligned = aligned_velocity

	# Align latitude
	if latitude:
		for imu in imus:
			aligned_lat = []
			for t in imu.time_aligned:
				# Find the previous value
				prev_index = closest_index(imu.time, t)
				prev_time = imu.time[prev_index]
				prev_lat = imu.latitude[prev_index]

				# Find the next value
				next_index = prev_index + 1
				next_time = imu.time[next_index]
				next_lat = imu.latitude[next_index]

				# Interpolate the value to requested time t
				interpolated_lat = interpolate_linear(prev_lat, next_lat, prev_time, next_time, t)
				aligned_lat.append(interpolated_lat)
			imu.latitude_aligned = aligned_lat

	# Align longitude
	if longitude:
		for imu in imus:
			aligned_long = []
			for t in imu.time_aligned:
				# Find the previous value
				prev_index = closest_index(imu.time, t)
				prev_time = imu.time[prev_index]
				prev_long = imu.longitude[prev_index]

				# Find the next value
				next_index = prev_index + 1
				next_time = imu.time[next_index]
				next_long = imu.longitude[next_index]

				# Interpolate the value to requested time t
				interpolated_long = interpolate_linear(prev_long, next_long, prev_time, next_time, t)
				aligned_long.append(interpolated_long)
			imu.longitude_aligned = aligned_long

	# Align yaw
	if yaw:
		for imu in imus:
			aligned_yaw = []
			for t in imu.time_aligned:
				# Find the previous value
				prev_index = closest_index(imu.time, t)
				prev_time = imu.time[prev_index]
				prev_yaw = imu.yaw[prev_index]

				# Find the next value
				next_index = prev_index + 1
				next_time = imu.time[next_index]
				next_yaw = imu.yaw[next_index]

				# Interpolate the value to requested time t
				interpolated_yaw = interpolate_linear(prev_yaw, next_yaw, prev_time, next_time, t)
				aligned_yaw.append(interpolated_yaw)
			imu.yaw_aligned = aligned_yaw

	return imus


def interpolate_linear(prev_val, next_val, prev_t, next_t, new_t):
	"""
	Linear interpolation

	Input: value and time of previous value and next value, time new_t to interpolate to
	Output: Interpolated value at new_t
	"""
	new_val = (prev_val*(next_t - new_t) + next_val*(new_t - prev_t))/(next_t-prev_t)
	return new_val


def closest_index(data_list, val):
	"""
	Calculate the index of the list value closest to given val 
	"""
	closest_val = take_closest(data_list, val)
	closest_index = data_list.index(closest_val)
	return closest_index


def take_closest(data_list, val):
    """
    Assumes data_list is sorted. Returns closest value lower than val.

    If two numbers are equally close, return the smallest number.
    (When looking both directions)
    """
    pos = bisect_left(data_list, val)
    if pos == 0:
        return data_list[0]
    if pos == len(data_list):
        return data_list[-1]
    before = data_list[pos - 1]
    after = data_list[pos]
    if after == val:
    	return after
    else:
    	return before
    
    # use if look for closest in both directions
    #if after - val < val - before:
    #   return after
    #else:
    #   return before