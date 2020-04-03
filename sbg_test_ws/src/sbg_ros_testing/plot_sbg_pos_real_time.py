#!/usr/bin/env python

import rospy
import os
import sys
from sensor_msgs.msg import NavSatFix
from geometry_msgs.msg import PointStamped
from nav_msgs.msg import Odometry
from fs_msgs.msg import Sbg_ekf_status
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import pickle

class SBGPosPlotter:
    def __init__(self, update_freq=1):
        interval = 1.0/update_freq*1000

        # ekf solution status
        self.ekf_status_msg = None
        rospy.Subscriber("/sbg_ekf_status", Sbg_ekf_status, self.ekf_status_callback)

        # OBS: the FuncAnimation objects needs to be stored in a variable, 
        # otherwise it's garbage collected (?) and doesn't work
        # long lat 
        self.long_lat_fig = plt.figure()
        self.long_lat_fig.suptitle("EKF Coordinates")
        #self.long_lat_fig_ax = self.long_lat_fig_ax.add_subplot(111)
        self.long_lat_artists = {}
        self.a1 = FuncAnimation(self.long_lat_fig, self.animate_long_lat, interval=interval)
        self._long = []
        self._lat = []
        rospy.Subscriber("/sbg_gps_fix", NavSatFix, self.long_lat_callback)

        # position converted from long lat
        self.pos_fig = plt.figure()
        self.pos_fig.suptitle("EKF Position")
        #self.pos_fig_ax = self.pos_fig.add_subplot(111)
        self.pos_artists = {}
        self.a2 = FuncAnimation(self.pos_fig, self.animate_pos, interval=interval)
        self._x_pos = []
        self._y_pos = []
        rospy.Subscriber("/sbg_gps_position", PointStamped, self.pos_callback)

        # visual odometry
        self.pos_vis_fig = plt.figure()
        self.pos_vis_fig.suptitle("Visual Odometry")
        #self.pos_vis_fig_ax = self.pos_vis_fig.add_subplot(111)
        self.pos_vis_artists = {}
        self.a3 = FuncAnimation(self.pos_vis_fig, self.animate_visual_odometry, interval=interval)
        self._x_vis_odom = []
        self._y_vis_odom = []
        rospy.Subscriber("/zed/speed", Odometry, self.visual_odometry_callback)
        
        """
        for fig, artists in zip([self.long_lat_fig, self.pos_fig, self.pos_vis_fig],
                                [self.long_lat_artists, self.pos_artists, self.pos_vis_artists]):
            ax = fig.add_subplot(111)
            color = {True: "green", False:"red", "1":"red", "2":"orange", "3":"yellow", "4":"green"}
            status = {"Computation Mode": "1",
                    "Attitude Valid": False,
                    "Heading Valid": False,
                    "Velocity Valid": False,
                    "Position Valid": False,
                    "GPS Position Used": False,
                    "GPS Velocity Used": False,
                    "Alignment Valid": False,
                    "Odometry Used": False}
            fontsize = 10
            vert_align = "bottom"
            horiz_align = "right"
            for text in status:
                a = ax.text(0.95, 0.01, 
                            text,
                            verticalalignment=vert_align, 
                            horizontalalignment=horiz_align,
                            transform=ax.transAxes,
                            color=color[status[text]], 
                            fontsize=fontsize)
                artists[text] = a
        
        ax = self.pos_fig.add_subplot(111)
        fontsize = 10
        vert_align = "bottom"
        horiz_align = "right"
        self.a = ax.text(0.95, 0.01, 
                            "hej",
                            verticalalignment=vert_align, 
                            horizontalalignment=horiz_align,
                            transform=ax.transAxes,
                            color="green", 
                            fontsize=fontsize)
        """
        plt.show()

    def ekf_status_callback(self, msg):
        self.ekf_status_msg = msg

    def long_lat_callback(self, msg):
        print("update long lat")
        self._long.append(msg.longitude)
        self._lat.append(msg.latitude)
                
        
    def pos_callback(self, msg):
        print("update pos")
        self._x_pos.append(msg.point.x)
        self._y_pos.append(msg.point.y)


    def visual_odometry_callback(self, msg):
        print("update vis odom")
        self._x_vis_odom.append(msg.pose.pose.position.x)
        self._y_vis_odom.append(msg.pose.pose.position.y)
                

    def animate_long_lat(self, i):
        self.animate(self.long_lat_fig, self.long_lat_artists, self._long, self._lat)
            

    def animate_pos(self, i):
        self.animate(self.pos_fig, self.pos_artists, self._x_pos, self._y_pos)


    def animate_visual_odometry(self, i):
        self.animate(self.pos_vis_fig, self.pos_vis_artists, self._x_vis_odom, self._y_vis_odom)


    def animate(self, fig, artists, x_ls, y_ls):
        fig = plt.figure(fig.number)
        plt.cla()

        self.plot_ekf_status(fig, artists)

        plt.plot(x_ls, y_ls)
        #plt.draw()

    def plot_ekf_status(self, fig, artists):
        if not self.ekf_status_msg: return
        """
        color = {True: "green", False:"red", "1":"red", "2":"orange", "3":"yellow", "4":"green"}
        status = {"Computation Mode {}".format(self.ekf_status_msg.COMPUTATION_MODE): self.ekf_status_msg.COMPUTATION_MODE,
                "Attitude Valid": self.ekf_status_msg.ATTITUDE_VALID,
                "Heading Valid": self.ekf_status_msg.HEADING_VALID,
                "Velocity Valid": self.ekf_status_msg.VELOCITY_VALID,
                "Position Valid": self.ekf_status_msg.POSITION_VALID,
                "GPS Position Used": self.ekf_status_msg.GPS1_POS_USED,
                "GPS Velocity Used": self.ekf_status_msg.GPS1_VEL_USED,
                "Alignment Valid": self.ekf_status_msg.ALIGN_VALID,
                "Odometry Used": self.ekf_status_msg.ODO_USED}

        for text in artists:
            a = artists[text]
            a.set_color(color[status[text]])
        
        
        self.a.set_color("red")
        plt.draw()
        """

if __name__ == "__main__":
    rospy.init_node("sbg_pos_plotter")
    update_freq = float(rospy.get_param(rospy.get_name() + "/freq"))
    plotter = SBGPosPlotter(update_freq=update_freq)
    rospy.spin()