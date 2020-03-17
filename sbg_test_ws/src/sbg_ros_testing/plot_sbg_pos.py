#!/usr/bin/env python

import rospy
from sensor_msgs.msg import NavSatFix
import matplotlib.pyplot as plt

class SBGPosPlotter:
    def __init__(self, start_time, end_time, plot_real_time):
        self.start_time = start_time
        self.end_time = end_time
        self.plot_real_time = plot_real_time
        self._longs = []
        self._lats = []

        self._plot_now = False

        rospy.Subscriber("/sbg_gps_fix", NavSatFix, self.lng_lat_callback)

    def lng_lat_callback(self, msg):
        if self._plot_now: 
            return

        sec = msg.header.stamp.to_sec()
        if sec > self.start_time:
            if sec < self.end_time:
                rospy.loginfo("Plotting long and lat at time: {}".format(sec))
                if self.plot_real_time:
                    plt.scatter(msg.longitude, msg.latitude)
                    plt.pause(0.000001)
                self._longs.append(msg.longitude)
                self._lats.append(msg.latitude)
            else:
                rospy.loginfo("Done, showing plot!")
                self._plot_now = True
                plt.figure()
                plt.plot(self._longs, self._lats)
                plt.show()
                
        
    def pos_callback(self, msg):
        if self._plot_now: 
            return

        sec = msg.header.stamp.to_sec()
        if sec > self.start_time:
            if sec < self.end_time:
                rospy.loginfo("Plotting long and lat at time: {}".format(sec))
                self._longs.append(msg.longitude)
                self._lats.append(msg.latitude)
            else:
                rospy.loginfo("Done, showing plot!")
                self._plot_now = True
                plt.plot(self._longs, self._lats)
                plt.show()

if __name__ == "__main__":
    rospy.init_node("sbg_pos_plotter")

    start_time = 1
    end_time = 566

    time_zero = 1584290023
    start_time += time_zero
    end_time += time_zero
    plotter = SBGPosPlotter(start_time=start_time, end_time=end_time, plot_real_time=True)
    rospy.spin()