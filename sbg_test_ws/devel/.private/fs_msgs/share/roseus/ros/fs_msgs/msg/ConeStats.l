;; Auto-generated. Do not edit!


(when (boundp 'fs_msgs::ConeStats)
  (if (not (find-package "FS_MSGS"))
    (make-package "FS_MSGS"))
  (shadow 'ConeStats (find-package "FS_MSGS")))
(unless (find-package "FS_MSGS::CONESTATS")
  (make-package "FS_MSGS::CONESTATS"))

(in-package "ROS")
;;//! \htmlinclude ConeStats.msg.html


(defclass fs_msgs::ConeStats
  :super ros::object
  :slots (_nbr_detections _yellow_counter _blue_counter _avg_innovation_x _avg_innovation_y _std_innovation ))

(defmethod fs_msgs::ConeStats
  (:init
   (&key
    ((:nbr_detections __nbr_detections) 0)
    ((:yellow_counter __yellow_counter) 0)
    ((:blue_counter __blue_counter) 0)
    ((:avg_innovation_x __avg_innovation_x) 0.0)
    ((:avg_innovation_y __avg_innovation_y) 0.0)
    ((:std_innovation __std_innovation) 0.0)
    )
   (send-super :init)
   (setq _nbr_detections (round __nbr_detections))
   (setq _yellow_counter (round __yellow_counter))
   (setq _blue_counter (round __blue_counter))
   (setq _avg_innovation_x (float __avg_innovation_x))
   (setq _avg_innovation_y (float __avg_innovation_y))
   (setq _std_innovation (float __std_innovation))
   self)
  (:nbr_detections
   (&optional __nbr_detections)
   (if __nbr_detections (setq _nbr_detections __nbr_detections)) _nbr_detections)
  (:yellow_counter
   (&optional __yellow_counter)
   (if __yellow_counter (setq _yellow_counter __yellow_counter)) _yellow_counter)
  (:blue_counter
   (&optional __blue_counter)
   (if __blue_counter (setq _blue_counter __blue_counter)) _blue_counter)
  (:avg_innovation_x
   (&optional __avg_innovation_x)
   (if __avg_innovation_x (setq _avg_innovation_x __avg_innovation_x)) _avg_innovation_x)
  (:avg_innovation_y
   (&optional __avg_innovation_y)
   (if __avg_innovation_y (setq _avg_innovation_y __avg_innovation_y)) _avg_innovation_y)
  (:std_innovation
   (&optional __std_innovation)
   (if __std_innovation (setq _std_innovation __std_innovation)) _std_innovation)
  (:serialization-length
   ()
   (+
    ;; int32 _nbr_detections
    4
    ;; int32 _yellow_counter
    4
    ;; int32 _blue_counter
    4
    ;; float32 _avg_innovation_x
    4
    ;; float32 _avg_innovation_y
    4
    ;; float32 _std_innovation
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _nbr_detections
       (write-long _nbr_detections s)
     ;; int32 _yellow_counter
       (write-long _yellow_counter s)
     ;; int32 _blue_counter
       (write-long _blue_counter s)
     ;; float32 _avg_innovation_x
       (sys::poke _avg_innovation_x (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _avg_innovation_y
       (sys::poke _avg_innovation_y (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _std_innovation
       (sys::poke _std_innovation (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _nbr_detections
     (setq _nbr_detections (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _yellow_counter
     (setq _yellow_counter (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _blue_counter
     (setq _blue_counter (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; float32 _avg_innovation_x
     (setq _avg_innovation_x (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _avg_innovation_y
     (setq _avg_innovation_y (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _std_innovation
     (setq _std_innovation (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get fs_msgs::ConeStats :md5sum-) "e29d797ff713ceaa2ace1ff34729c17e")
(setf (get fs_msgs::ConeStats :datatype-) "fs_msgs/ConeStats")
(setf (get fs_msgs::ConeStats :definition-)
      "#
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



(provide :fs_msgs/ConeStats "e29d797ff713ceaa2ace1ff34729c17e")


