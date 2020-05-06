#!/usr/bin/env python

# Template for rewriting rosbags
#with rosbag.Bag('output.bag', 'w') as outbag:
#	for topic, msg, t in rosbag.Bag('input.bag').read_messages():
#		# This also replaces tf timestamps under the assumption 
#		# that all transforms in the message share the same timestamp
#		if topic == "/tf" and msg.transforms:
#			outbag.write(topic, msg, msg.transforms[0].header.stamp)
#		else:
#			outbag.write(topic, msg, msg.header.stamp if msg._has_header else t)


import os
import numpy as np
from imu_recording import ImuRecording
import rosbag
from tf.transformations import euler_from_quaternion

class RosbagToRecording:
	def __init__(self,
				 gps_topic="gps",
				 imu_topic="imu",
				 wheel_topic="wheel_odom",
				 odometry_topic="odometry"):

		self.imu = ImuRecording()

		self.gps_topic = gps_topic
		self.imu_topic = imu_topic
		self.odometry_topic = odometry_topic
		self.wheel_topic = wheel_topic

	def _read_imu_msg(self, m, t):
		self.imu.add_data("gyr_x", m.angular_velocity.x, t)
		self.imu.add_data("gyr_y", m.angular_velocity.y, t)
		self.imu.add_data("gyr_z", m.angular_velocity.z, t)
		self.imu.add_data("acc_x", m.linear_acceleration.x, t)
		self.imu.add_data("acc_y", m.linear_acceleration.y, t)
		self.imu.add_data("acc_z", m.linear_acceleration.z, t)


	def _read_navsat_msg(self, m, t):
		self.imu.add_data("gps_lat", m.latitude, t)
		self.imu.add_data("gps_long", m.longitude, t)

	def _read_odometry_msg(self, m, t):
		self.imu.add_data("pos_x", m.pose.pose.position.x, t)
		self.imu.add_data("pos_y", m.pose.pose.position.y, t)

		r, p, y = euler_from_quaternion([m.pose.pose.orientation.x, m.pose.pose.orientation.y,
										 m.pose.pose.orientation.z, m.pose.pose.orientation.w])

		r, p, y = np.rad2deg(r), np.rad2deg(p), np.rad2deg(y)
		self.imu.add_data("roll", r, t)
		self.imu.add_data("pitch", p, t)
		self.imu.add_data("yaw", y, t)

		self.imu.add_data("vel_x", m.twist.twist.linear.x, t)
		self.imu.add_data("vel_y", m.twist.twist.linear.y, t)
		self.imu.add_data("vel_z", m.twist.twist.linear.z, t)


	def _read_wheel_msg(self, time, i):
		# TODO: not implemented
		raise Exception("Not implemented")

	def rosbag_to_recording(self, file_path):
		bag = rosbag.Bag(file_path)

		for topic, msg, t in bag.read_messages():
			t = t.to_sec()
			if topic == self.gps_topic:
				self._read_navsat_msg(msg, t)
			elif topic == self.odometry_topic:
				self._read_odometry_msg(msg, t)
			elif topic == self.imu_topic:
				self._read_imu_msg(msg, t)
			elif topic == self.wheel_topic:
				self._read_wheel_msg(msg, t)
		#self.imu.save(os.path.splitext(file_path)[0] + "_from_bag")
		return self.imu

if __name__ == '__main__':
	#converter = RosbagToRecording()
	#converter.rosbag_to_recording("SBG_general_000.bag")
	imu = ImuRecording.__subclasses__()[2]()
	imu.read("SBG_general_000.processed")
	imu.plot_all()
	#imu.save("SBG_general_000.txt")

	