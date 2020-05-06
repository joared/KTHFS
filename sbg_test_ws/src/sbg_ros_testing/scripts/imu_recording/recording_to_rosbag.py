#!/usr/bin/env python
import argparse
import os
import numpy as np

import rospy
import rosbag
from geometry_msgs.msg import Quaternion
from tf.transformations import quaternion_from_euler
from sensor_msgs.msg import Imu, NavSatFix
from nav_msgs.msg import Odometry


class RecordingToBag:
	def __init__(self, imu,
				 gps_topic="gps", gps_frame="gps_frame",
				 imu_topic="imu", imu_frame="imu_base_link",
				 wheel_topic="wheel_odom", wheel_frame="wheel_odom", wheel_child_frame="rear_axle",
				 odometry_topic="odometry", odometry_frame="map", odometry_child_frame="base_link"):
		self.imu = imu
		assert self.imu.time, "IMU data 'time' is needed to save the recording as a rosbag"
		self.freq_dict = None

		self.gps_topic = gps_topic
		self.gps_frame = gps_frame
		self.imu_topic = imu_topic
		self.imu_frame = imu_frame
		self.odometry_topic = odometry_topic
		self.odometry_frame = odometry_frame
		self.odometry_child_frame = odometry_child_frame
		self.wheel_topic = wheel_topic
		self.wheel_frame = wheel_frame
		self.wheel_child_frame = wheel_child_frame


	def _generate_imu_msg(self, time, i):
		m = Imu()
		m.header.stamp = time
		m.header.frame_id = self.imu_frame
		m.angular_velocity.x = self.imu.gyr_x[i]
		m.angular_velocity.y = self.imu.gyr_y[i]
		m.angular_velocity.z = self.imu.gyr_z[i]
		m.linear_acceleration.x = self.imu.acc_x[i]
		m.linear_acceleration.y = self.imu.acc_y[i]
		m.linear_acceleration.z = self.imu.acc_z[i]
		m.orientation.w = 1
		return m


	def _generate_navsat_msg(self, time, i):
		m = NavSatFix()
		m.header.stamp = time
		m.header.frame_id = self.gps_frame
		m.latitude = self.imu.gps_lat[i]
		m.longitude = self.imu.gps_long[i]
		return m


	def _generate_odometry_msg(self, time, i):
		m = Odometry()
		m.header.stamp = time
		m.header.frame_id = self.odometry_frame
		m.child_frame_id = self.odometry_child_frame
		m.pose.pose.position.x = self.imu.pos_x[i]
		m.pose.pose.position.y = self.imu.pos_y[i]
		q = quaternion_from_euler(np.deg2rad(self.imu.roll[i]), 
								  np.deg2rad(self.imu.pitch[i]), 
								  np.deg2rad(self.imu.yaw[i]), 
								  "sxyz")
		m.pose.pose.orientation = Quaternion(*q)
		m.twist.twist.linear.x = self.imu.vel_x[i]
		m.twist.twist.linear.y = self.imu.vel_y[i]
		m.twist.twist.linear.z = self.imu.vel_z[i]

		return m


	def _generate_wheel_msg(self, time, i):
		# TODO: not implemented
		m = Odometry()
		m.header.stamp = time
		m.header.frame_id = self.wheel_frame
		m.child_frame_id = self.wheel_child_frame
		q = [0,0,0,1]
		m.pose.pose.orientation = Quaternion(*q)
		return m


	def create_rosbag(self, name, on_new_data=False, freq_dict=None):
		# TODO: use freq_dict to set frequency of each signal,
		# None means on new data
		self.freq_dict = None

		name = os.path.splitext(name)[0] + ".bag"
		with rosbag.Bag(name, "w") as bag:
			for i, t in enumerate(self.imu.time):
				time = rospy.Time(t)
			
				write_imu = bool(self.imu.acc_x)
				write_gps = bool(self.imu.gps_long)
				write_odom = bool(self.imu.pos_x)
				#write_wheel = True
				if i > 0 and on_new_data:
					write_imu = write_imu and self.imu.acc_x[i] != self.imu.acc_x[i-1]
					write_gps = write_gps and self.imu.gps_long[i] != self.imu.gps_long[i-1]
					write_odom = write_odom and self.imu.pos_x[i] != self.imu.pos_x[i-1]
					#write_wheel = write_wheel and True

				# acceleration, gyroscope and magnetometer
				if write_imu:
					imu_msg = self._generate_imu_msg(time, i)
					bag.write(self.imu_topic, imu_msg, time)

				# gps longitude and latitude
				if write_gps:
					gps_msg = self._generate_navsat_msg(time, i)
					bag.write(self.gps_topic, gps_msg, time)

				# position, orientation and velocity
				if write_odom:
					odom_msg = self._generate_odometry_msg(time, i)
					bag.write(self.odometry_topic, odom_msg, time)

				# wheel encoder, currently not implemented
				#wheel_msg = self._generate_wheel_msg(time, i)
				#bag.write(self.wheel_topic, wheel_msg, time)
		print("Created rosbag '{}'".format(name))


if __name__ == '__main__':
	from imu_recording import ImuRecording
	reader_classes = ImuRecording.__subclasses__()
	reader_classes.append(ImuRecording)
	reader_names = [cls.__name__ for cls in reader_classes]
	parser = argparse.ArgumentParser(description="Converts an IMU ASCII/.processed recording into a rosbag.")
	parser.add_argument('reader', type=str, choices=reader_names, help="The class which will be used for reading the file.")
	parser.add_argument('file', type=str, help="ASCII/.processed file recording containing the recorded IMU values.")
	parser.add_argument("-d", '--delimiter', default="t", choices=["t", "s", ""], type=str, help="Delimiter used in the recording.")
	parser.add_argument("-s", "--save", action="store_true", help="Save .processed file")

	args = parser.parse_args()

	if args.delimiter == "t": args.delimiter = "\t"
	if args.delimiter == "s": args.delimiter = " "
	if args.delimiter == "": args.delimiter = None

	try:
		reader_idx = reader_names.index(args.reader)
	except ValueError:
		print("Reader '{}' does not exist. Choose from: {}".format(args.reader, reader_names))
	else:
		imu_reader = reader_classes[reader_idx]()


	imu_reader.read(args.file, delimiter=args.delimiter)
	if args.save: imu_reader.save(args.file)
	bagger = RecordingToBag(imu_reader)
	bagger.create_rosbag(args.file)
