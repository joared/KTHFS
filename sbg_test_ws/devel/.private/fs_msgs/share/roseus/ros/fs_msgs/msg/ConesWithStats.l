;; Auto-generated. Do not edit!


(when (boundp 'fs_msgs::ConesWithStats)
  (if (not (find-package "FS_MSGS"))
    (make-package "FS_MSGS"))
  (shadow 'ConesWithStats (find-package "FS_MSGS")))
(unless (find-package "FS_MSGS::CONESWITHSTATS")
  (make-package "FS_MSGS::CONESWITHSTATS"))

(in-package "ROS")
;;//! \htmlinclude ConesWithStats.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass fs_msgs::ConesWithStats
  :super ros::object
  :slots (_header _cones ))

(defmethod fs_msgs::ConesWithStats
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:cones __cones) (let (r) (dotimes (i 0) (push (instance fs_msgs::ConeWithStats :init) r)) r))
    )
   (send-super :init)
   (setq _header __header)
   (setq _cones __cones)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:cones
   (&rest __cones)
   (if (keywordp (car __cones))
       (send* _cones __cones)
     (progn
       (if __cones (setq _cones (car __cones)))
       _cones)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; fs_msgs/ConeWithStats[] _cones
    (apply #'+ (send-all _cones :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; fs_msgs/ConeWithStats[] _cones
     (write-long (length _cones) s)
     (dolist (elem _cones)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; fs_msgs/ConeWithStats[] _cones
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _cones (let (r) (dotimes (i n) (push (instance fs_msgs::ConeWithStats :init) r)) r))
     (dolist (elem- _cones)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get fs_msgs::ConesWithStats :md5sum-) "6718c9a6b3d40b0468a363f35c8b1688")
(setf (get fs_msgs::ConesWithStats :datatype-) "fs_msgs/ConesWithStats")
(setf (get fs_msgs::ConesWithStats :definition-)
      "#
# Array of cones with statistics
#

# Extra information on the message
# header.stamp: time of the message
# header.frame_id: frame in which the cones are given
Header header

# Array of cones
ConeWithStats[] cones

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: fs_msgs/ConeWithStats
#
# Description of a cone with statistics
#

Cone cone
ConeStats stats

================================================================================
MSG: fs_msgs/Cone
#
# Description of a cone
#

# 2D-position of the cone
float64 x
float64 y

# Color of the cone
uint8 UNDEFINED = 0
uint8 YELLOW = 1
uint8 BLUE = 2
uint8 SMALL_ORANGE = 3
uint8 BIG_ORANGE = 4

uint8 color

# Covariance on the position [m^2] (2x2 matrix in row-major order)
float64[4] covariance

# Confidence in the detection
float64 probability

================================================================================
MSG: fs_msgs/ConeStats
#
# Statistics of a cone
#

# Number of times the cone has been seen
int32 nbr_detections

# Color counters
int32 yellow_counter
int32 blue_counter

# Average innovation (innovation = mapped position - detected position)
float32 avg_innovation_x
float32 avg_innovation_y

# Standard deviation of innovation norms
float32 std_innovation

")



(provide :fs_msgs/ConesWithStats "6718c9a6b3d40b0468a363f35c8b1688")


