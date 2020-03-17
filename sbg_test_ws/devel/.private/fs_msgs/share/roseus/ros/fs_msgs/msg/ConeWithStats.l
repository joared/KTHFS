;; Auto-generated. Do not edit!


(when (boundp 'fs_msgs::ConeWithStats)
  (if (not (find-package "FS_MSGS"))
    (make-package "FS_MSGS"))
  (shadow 'ConeWithStats (find-package "FS_MSGS")))
(unless (find-package "FS_MSGS::CONEWITHSTATS")
  (make-package "FS_MSGS::CONEWITHSTATS"))

(in-package "ROS")
;;//! \htmlinclude ConeWithStats.msg.html


(defclass fs_msgs::ConeWithStats
  :super ros::object
  :slots (_cone _stats ))

(defmethod fs_msgs::ConeWithStats
  (:init
   (&key
    ((:cone __cone) (instance fs_msgs::Cone :init))
    ((:stats __stats) (instance fs_msgs::ConeStats :init))
    )
   (send-super :init)
   (setq _cone __cone)
   (setq _stats __stats)
   self)
  (:cone
   (&rest __cone)
   (if (keywordp (car __cone))
       (send* _cone __cone)
     (progn
       (if __cone (setq _cone (car __cone)))
       _cone)))
  (:stats
   (&rest __stats)
   (if (keywordp (car __stats))
       (send* _stats __stats)
     (progn
       (if __stats (setq _stats (car __stats)))
       _stats)))
  (:serialization-length
   ()
   (+
    ;; fs_msgs/Cone _cone
    (send _cone :serialization-length)
    ;; fs_msgs/ConeStats _stats
    (send _stats :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; fs_msgs/Cone _cone
       (send _cone :serialize s)
     ;; fs_msgs/ConeStats _stats
       (send _stats :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; fs_msgs/Cone _cone
     (send _cone :deserialize buf ptr-) (incf ptr- (send _cone :serialization-length))
   ;; fs_msgs/ConeStats _stats
     (send _stats :deserialize buf ptr-) (incf ptr- (send _stats :serialization-length))
   ;;
   self)
  )

(setf (get fs_msgs::ConeWithStats :md5sum-) "bc6abd39812a69dee6e5d6c6dbebf194")
(setf (get fs_msgs::ConeWithStats :datatype-) "fs_msgs/ConeWithStats")
(setf (get fs_msgs::ConeWithStats :definition-)
      "#
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



(provide :fs_msgs/ConeWithStats "bc6abd39812a69dee6e5d6c6dbebf194")


