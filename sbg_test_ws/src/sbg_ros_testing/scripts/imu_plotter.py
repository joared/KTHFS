#!/usr/bin/env python

import rospy
import os
import sys
from sensor_msgs.msg import NavSatFix
from geometry_msgs.msg import PointStamped
from nav_msgs.msg import Odometry
import matplotlib.pyplot as plt

import pickle

class SBGPosPlotter:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
        
        self._longs = []
        self._lats = []
        self._xpos = []
        self._ypos = []
        self._xpos_vis = []
        self._ypos_vis = []

        self._has_plotted = False

        self._lng_lat_done = False
        self._pos_done = False
        self._vis_odom_done = False

        rospy.Subscriber("/sbg_gps_fix", NavSatFix, self.lng_lat_callback)
        rospy.Subscriber("/sbg_gps_position", PointStamped, self.pos_callback)
        rospy.Subscriber("/zed/speed", Odometry, self.visual_odometry_callback)
        
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
                rospy.loginfo("Done: lng lat")
                self._lng_lat_done = True
                
        
    def pos_callback(self, msg):
        if self._pos_done: 
            self.plot()
            return

        sec = msg.header.stamp.to_sec()
        if sec > self.start_time:
            if sec < self.end_time:
                #rospy.loginfo("Plotting pos x and pos y at time: {}".format(sec))
                self._xpos.append(msg.point.x)
                self._ypos.append(msg.point.y)
            else:
                rospy.loginfo("Done: position")
                self._pos_done = True
                

    def visual_odometry_callback(self, msg):
        if self._vis_odom_done: 
            self.plot()
            return

        sec = msg.header.stamp.to_sec()
        if sec > self.start_time:
            if sec < self.end_time:
                rospy.loginfo("Visual odometry at time: {}".format(sec))
                self._xpos_vis.append(msg.pose.pose.position.x)
                self._ypos_vis.append(msg.pose.pose.position.y)
            else:
                rospy.loginfo("Done: visual odometry")
                self._vis_odom_done = True
                

    def plot(self):
        if self._has_plotted:
            return
        if self._pos_done and self._vis_odom_done and self._lng_lat_done:
            self._has_plotted = True
            fig1 = plt.figure()
            plt.plot(self._xpos, self._ypos)
            plt.plot(self._xpos_vis, self._ypos_vis)
            plt.scatter(self._xpos, self._ypos)
            plt.scatter(self._xpos_vis, self._ypos_vis)
            fig2 = plt.figure()
            plt.plot(self._longs, self._lats)
            plt.scatter(self._longs, self._lats)
            
            d = "/home/joar/KTHFS/"
            #rosbag_2020-03-15-17-33-25
            with open(d + "sbg_pos_and_vis.pickle", "w") as f:
                print("saving")
                pickle.dump(fig1, f)
                print("done")
            with open(d + "sbg_lng_lat.pickle", "w") as f:
                print("saving")
                pickle.dump(fig2, f)
                print("done")
            plt.show()

            
            

if __name__ == "__main__":
    rospy.init_node("sbg_pos_plotter")

    start_time = 1
    end_time = 500

    time_zero = 1584290005
    start_time += time_zero
    end_time += time_zero
    plotter = SBGPosPlotter(start_time=start_time, end_time=end_time)
    rospy.spin()