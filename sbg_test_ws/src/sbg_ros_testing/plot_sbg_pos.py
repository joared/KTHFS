#!/usr/bin/env python

import rospy
from sensor_msgs.msg import NavSatFix
from geometry_msgs.msg import PointStamped
import matplotlib.pyplot as plt

class SBGPosPlotter:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
        
        self._longs = []
        self._lats = []
        self._xpos = []
        self._ypos = []

        self._has_plotted = False
        self._lng_lat_done = False
        self._pos_done = False

        rospy.Subscriber("/sbg_gps_fix", NavSatFix, self.lng_lat_callback)
        rospy.Subscriber("/sbg_gps_position", PointStamped, self.pos_callback)

    def lng_lat_callback(self, msg):
        if self._lng_lat_done:
            self.plot()
            return

        sec = msg.header.stamp.to_sec()
        if sec > self.start_time:
            if sec < self.end_time:
                #rospy.loginfo("Plotting long and lat at time: {}".format(sec))
                self._longs.append(msg.longitude)
                self._lats.append(msg.latitude)
            else:
                rospy.loginfo("Done, showing plot!")
                self._lng_lat_done = True

                
        
    def pos_callback(self, msg):
        if self._pos_done: 
            self.plot()
            return
        print(rospy.Time.now())
        sec = msg.header.stamp.to_sec()
        if sec > self.start_time:
            if sec < self.end_time:
                #rospy.loginfo("Plotting pos x and pos y at time: {}".format(sec))
                self._xpos.append(msg.point.x)
                self._ypos.append(msg.point.y)
            else:
                rospy.loginfo("Done, showing plot!")
                self._pos_done = True
                

    def plot(self):
        if self._has_plotted:
            return
        if self._lng_lat_done and self._pos_done:
            self._has_plotted = True
            plt.plot(self._longs, self._lats)
            plt.figure()
            plt.plot(self._xpos, self._ypos)
            plt.show()
            

if __name__ == "__main__":
    rospy.init_node("sbg_pos_plotter")

    start_time = 1
    end_time = 566

    time_zero = 1584290023
    start_time += time_zero
    end_time += time_zero
    plotter = SBGPosPlotter(start_time=start_time, end_time=end_time)
    rospy.spin()