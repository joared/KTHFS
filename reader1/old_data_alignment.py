import numpy as np
from bisect import bisect_left


def convert_angle_in_range(max_angle, min_angle, val):
	angle_range = max_angle-min_angle
	if val > max_angle:
		return val-angle_range
	elif val < min_angle:
		return val+angle_range
	else:
		return val

def min_angle_diff(max_angle, min_angle, a1, a2):
	diff1 = max_angle-a1 + a2-min_angle
	diff2 = -(max_angle-a2 + a1-min_angle)
	diff3 = a2-a1
	diffs = [diff1, diff2, diff3]
	abs_diffs = [abs(v) for v in diffs]
	return diffs[abs_diffs.index(min(abs_diffs))]

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

	return imus


def interpolate_linear(prev_val, next_val, prev_t, next_t, new_t):
	"""
	Linear interpolation

	Input: value and time of previous value and next value, time new_t to interpolate to
	Output: Interpolated value at new_t
	"""
	new_val = (prev_val*(next_t - new_t) + next_val*(new_t - prev_t))/(next_t-prev_t)
	#new_val = (next_val-prev_val)/(next_t-prev_t)*(new_t-prev_t) + prev_val
	#if new_val != new_val_jack: 
	#	raise Exception("Wrong calculation!: {} != {}".format(new_val_jack, new_val))
	return new_val

def interpolate_linear_angle(prev_val, next_val, prev_t, next_t, new_t):
	max_angle = 180
	min_angle = -180
	next_val = prev_val + min_angle_diff(max_angle, min_angle, prev_val, next_val)
	new_val = interpolate_linear(prev_val, next_val, prev_t, next_t, new_t)
	new_val = convert_angle_in_range(max_angle, min_angle, new_val)
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