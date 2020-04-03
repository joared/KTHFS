roslaunch sbg_ros_testing plot_sbg_pos_real_time freq:=10
rostopic echo sbg_ekf_status
rosbag play <rosbag>