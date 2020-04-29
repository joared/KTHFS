#!/usr/bin/env python
import rospy

from geometry_msgs.msg import Quaternion
#from tf.transformations import quaternion_from_euler
from sensor_msgs.msg import Imu, NavSatFix
from nav_msgs.msg import Odometry


class Prefilter:
    def __init__(self,
                 gps_topic="gps", 
                 imu_topic="imu", 
                 wheel_topic="wheel_odom", 
                 odometry_topic="odometry"):

        rospy.Subscriber(imu_topic, Imu, self.imu_callback)
        self.imu_pub = rospy.Publisher(imu_topic + "/prefiltered", Imu, queue_size=1)
        self.imu_accel_cov = map(float, rospy.get_param("prefilter/imu_covariance/accel"))
        self.imu_ang_vel_cov = map(float, rospy.get_param("prefilter/imu_covariance/angular_velocity"))


        rospy.Subscriber(wheel_topic, Odometry, self.wheel_odom_callback)
        self.wheel_pub = rospy.Publisher(wheel_topic + "/prefiltered", Odometry, queue_size=1)
        self.wheel_twist_cov = map(float, rospy.get_param("prefilter/wheel_covariance/twist"))

    def imu_callback(self, msg):
        msg.linear_acceleration_covariance = self.imu_accel_cov
        msg.angular_velocity_covariance = self.imu_ang_vel_cov
        self.imu_pub.publish(msg)

    def wheel_odom_callback(self, msg):
        msg.twist.twist.linear.y = 0
        msg.twist.covariance = self.wheel_twist_cov
        self.wheel_pub.publish(msg)

if __name__ == "__main__":
    rospy.init_node("prefilter_node")
    Prefilter(wheel_topic="odometry")
    rospy.spin()
