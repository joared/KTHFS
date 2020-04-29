#!/usr/bin/env python

import rospy
import os
import sys
from sensor_msgs.msg import NavSatFix, Imu
from geometry_msgs.msg import PointStamped
from nav_msgs.msg import Odometry
#from fs_msgs.msg import Sbg_ekf_status
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from tf.transformations import euler_from_quaternion

import numpy as np
import pickle
from imu_data_reader import ImuRecording
from imu_plotter import ImuPlotter

class ImuRosListener:
    def __init__(self, imu, update_freq=20,
                 gps_topic="gps", 
                 imu_topic="imu", 
                 wheel_topic="wheel_odom", 
                 odometry_topic="odometry"):

        #interval = 1.0/update_freq*1000
        self.imu = imu
        self.update_freq = update_freq

        self.gps_topic = gps_topic
        self.imu_topic = imu_topic
        self.odometry_topic = odometry_topic
        self.wheel_topic = wheel_topic

        self._imu_msgs = []
        self._gps_msgs = []
        self._odometry_msgs = []
        self._wheel_msgs = []

        rospy.Subscriber(self.gps_topic, NavSatFix, self.gps_callback)
        rospy.Subscriber(self.imu_topic, Imu, self.imu_callback)
        rospy.Subscriber(self.odometry_topic, Odometry, self.odometry_callback)
        rospy.Subscriber(self.wheel_topic, Odometry, self.wheel_callback)


    def imu_callback(self, msg):
        self._imu_msgs.append(msg)

    def gps_callback(self, msg):
        self._gps_msgs.append(msg)

    def odometry_callback(self, msg):
        self._odometry_msgs.append(msg)

    def wheel_callback(self, msg):
        self._wheel_msgs.append(msg)

    def add_data_from_imu(self, msg):
        t = msg.header.stamp.to_sec()
        self.imu.add_data("acc_x", msg.linear_acceleration.x, t)
        self.imu.add_data("acc_y", msg.linear_acceleration.y, t)
        self.imu.add_data("acc_z", msg.linear_acceleration.z, t)
        self.imu.add_data("gyr_x", msg.angular_velocity.x, t)
        self.imu.add_data("gyr_y", msg.angular_velocity.y, t)
        self.imu.add_data("gyr_z", msg.angular_velocity.z, t)

    def add_data_from_gps(self, msg):
        t = msg.header.stamp.to_sec()
        self.imu.add_data("long", msg.longitude, t)
        self.imu.add_data("lat", msg.latitude, t)

    def add_data_from_wheel(self, msg):
        pass

    def add_data_from_odometry(self, msg):
        t = msg.header.stamp.to_sec()
        # TODO: position
        r, p, y = euler_from_quaternion([msg.pose.pose.orientation.x,
                                         msg.pose.pose.orientation.y,
                                         msg.pose.pose.orientation.z,
                                         msg.pose.pose.orientation.w])

        vx = msg.twist.twist.linear.x
        vy = msg.twist.twist.linear.y
        vz = msg.twist.twist.linear.z
        self.imu.add_data("roll", r, t)
        self.imu.add_data("pitch", p, t)
        self.imu.add_data("yaw", y, t)
        self.imu.add_data("vel_x", vx, t)
        self.imu.add_data("vel_y", vy, t)
        self.imu.add_data("vel_z", vz, t)

    def add_data_from_messages(self):
        msgs = [(m, "imu") for m in self._imu_msgs]\
               + [(m, "gps") for m in self._gps_msgs]\
               + [(m, "odometry") for m in self._odometry_msgs]\
               + [(m, "wheel") for m in  self._wheel_msgs]

        msgs.sort(lambda x: x[0].header.stamp, reverse=True)

        msg_func = {"imu": self.add_data_from_imu,
                    "gps": self.add_data_from_gps,
                    "odometry": self.add_data_from_odometry,
                    "wheel": self.add_data_from_wheel}

        for m in msgs:
            msg_func[m[1]](m[0])

        self._imu_msgs = []
        self._gps_msgs = []
        self._odometry_msgs = []
        self._wheel_msgs = []

    def spin(self):
        rate = rospy.Rate(self.update_freq)
        while not rospy.is_shutdown():
            self.handle_messages()
            rate.sleep()

if __name__ == "__main__":
    rospy.init_node("imu_ros_listener")
    imu = ImuRecording()
    l = ImuRosListener(imu)
    plotter = ImuPlotter(imu)
    #rate = rospy.Rate(3)
    #plotter.plot_play()
    #plotter.show()