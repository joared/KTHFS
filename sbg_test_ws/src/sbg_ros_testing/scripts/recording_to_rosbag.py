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
	def __init__(self, imu):
		self.imu = imu
		assert self.imu.time, "IMU data 'time' is needed to save the recording as a rosbag"
		#self.prefix = self.imu.name
		#self.imu_pub = rospy.Publisher("/imu", Imu, queue_size=1)


	def _generate_imu_msg(self, time, i):
		m = Imu()
		m.header.stamp = time
		m.header.frame_id = "imu_frame"
		m.angular_velocity.x = self.imu.gyr_x[i]
		m.angular_velocity.y = self.imu.gyr_y[i]
		m.angular_velocity.z = self.imu.gyr_z[i]
		m.linear_acceleration.x = self.imu.acc_x[i]
		m.linear_acceleration.y = self.imu.acc_y[i]
		m.linear_acceleration.z = self.imu.acc_z[i]
		return m

	def _generate_navsat_msg(self, time, i):
		m = NavSatFix()
		m.header.stamp = time
		m.header.frame_id = "gps_frame"
		m.latitude = self.imu.lat[i]
		m.longitude = self.imu.long[i]
		return m

	def _generate_odom_msg(self, time, i):
		# TODO: position
		m = Odometry()
		m.header.stamp = time
		m.header.frame_id = "base_link"
		q = quaternion_from_euler(self.imu.roll[i], self.imu.pitch[i], self.imu.yaw[i], "sxyz")
		m.pose.pose.orientation = Quaternion(*q)
		# m.pose.position = 
		return m

	def create_rosbag(self, name):
		name = os.path.splitext(name)[0] + ".bag"
		with rosbag.Bag(name, "w") as bag:
			for i, t in enumerate(self.imu.time):
				time = rospy.Time(t)

				imu_msg = self._generate_imu_msg(time, i)
				bag.write("imu", imu_msg, time)

				gps_msg = self._generate_navsat_msg(time, i)
				bag.write("gps", gps_msg, time)

				odom_msg = self._generate_odom_msg(time, i)
				bag.write("odometry", odom_msg, time)

	
if __name__ == '__main__':
	reader_classes = ImuReader.__subclasses__()
	reader_names = [cls.__name__ for cls in ImuReader.__subclasses__()]
	parser = argparse.ArgumentParser(description="Converts an IMU ASCII recording into a rosbag.")
	parser.add_argument('reader', type=str, choices=reader_names, help="The class which will be used for reading the file.")
	parser.add_argument('file', type=str, help="ASCII file recording containing the recorded IMU values.")
	parser.add_argument("-d", '--delimiter', default="", choices=["tab", "space", ""], type=str, help="Delimiter used in the recording.")
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
	if args.save: imu_reader.save_processed_data(args.file)
	bagger = RecordingToBag(imu_reader)
	bagger.create_rosbag(args.file)

	