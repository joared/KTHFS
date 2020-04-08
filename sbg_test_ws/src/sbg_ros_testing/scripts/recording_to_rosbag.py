#!/usr/bin/env python
import argparse
import os
from imu_reader.imu_data_reader import ImuReader, XsensReader, VBOXReader, SBGReader

import rospy
import rosbag
from geometry_msgs.msg import Quaternion
from tf.transformations import quaternion_from_euler
from sensor_msgs.msg import Imu, NavSatFix
from nav_msgs.msg import Odometry


class RecordingToBag:
	def __init__(self, imu,
				 gps_topic="gps", gps_frame="gps_frame",
				 imu_topic="imu", imu_frame="imu_frame",
				 wheel_topic="odom", wheel_frame="odom", wheel_child_frame="rear_axle",
				 odometry_topic="odometry", odometry_frame="map", odometry_child_frame="base_link"):
		self.imu = imu
		assert self.imu.time, "IMU data 'time' is needed to save the recording as a rosbag"
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
		m.linear_acceleration_covariance[0] = 0.11**2
		m.linear_acceleration_covariance[4] = 0.11**2
		m.angular_velocity_covariance[8] = 0.01**2
		return m

	def _generate_navsat_msg(self, time, i):
		m = NavSatFix()
		m.header.stamp = time
		m.header.frame_id = self.gps_frame
		m.latitude = self.imu.lat[i]
		m.longitude = self.imu.long[i]
		return m

	def _generate_odometry_msg(self, time, i):
		# TODO: position
		m = Odometry()
		m.header.stamp = time
		m.header.frame_id = self.odometry_frame
		m.child_frame_id = self.odometry_child_frame
		q = quaternion_from_euler(self.imu.roll[i], self.imu.pitch[i], self.imu.yaw[i], "sxyz")
		m.pose.pose.orientation = Quaternion(*q)
		# m.pose.position =
		return m

	def _generate_wheel_msg(self, time, i):
		# TODO: position
		m = Odometry()
		m.header.stamp = time
		m.header.frame_id = self.wheel_frame
		m.child_frame_id = self.wheel_child_frame
		q = [0,0,0,1]
		m.pose.pose.orientation = Quaternion(*q)
		m.twist.covariance[7] = 1e-2
		return m



	def create_rosbag(self, name):
		name = os.path.splitext(name)[0] + ".bag"
		with rosbag.Bag(name, "w") as bag:
			for i, t in enumerate(self.imu.time):
				time = rospy.Time(t)

				imu_msg = self._generate_imu_msg(time, i)
				bag.write(self.imu_topic, imu_msg, time)

				gps_msg = self._generate_navsat_msg(time, i)
				bag.write(self.gps_topic, gps_msg, time)

				odom_msg = self._generate_odometry_msg(time, i)
				bag.write(self.odometry_topic, odom_msg, time)

				wheel_msg = self._generate_wheel_msg(time, i)
				bag.write(self.wheel_topic, wheel_msg, time)


if __name__ == '__main__':
	reader_classes = ImuReader.__subclasses__()
	reader_classes.append(ImuReader)
	reader_names = [cls.__name__ for cls in reader_classes]
	parser = argparse.ArgumentParser(description="Converts an IMU ASCII/.processed recording into a rosbag.")
	parser.add_argument('reader', type=str, choices=reader_names, help="The class which will be used for reading the file.")
	parser.add_argument('file', type=str, help="ASCII/.processed file recording containing the recorded IMU values.")
	parser.add_argument("-d", '--delimiter', default="tab", choices=["tab", "space", ""], type=str, help="Delimiter used in the recording.")
	parser.add_argument("-s", "--save", action="store_true", help="Save .processed file")
	args = parser.parse_args()

	if args.delimiter == "tab": args.delimiter = "\t"
	if args.delimiter == "space": args.delimiter = " "
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
