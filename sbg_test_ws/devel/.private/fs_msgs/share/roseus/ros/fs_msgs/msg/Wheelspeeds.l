;; Auto-generated. Do not edit!


(when (boundp 'fs_msgs::Wheelspeeds)
  (if (not (find-package "FS_MSGS"))
    (make-package "FS_MSGS"))
  (shadow 'Wheelspeeds (find-package "FS_MSGS")))
(unless (find-package "FS_MSGS::WHEELSPEEDS")
  (make-package "FS_MSGS::WHEELSPEEDS"))

(in-package "ROS")
;;//! \htmlinclude Wheelspeeds.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass fs_msgs::Wheelspeeds
  :super ros::object
  :slots (_header _front_left _front_right _rear_left _rear_right _variance ))

(defmethod fs_msgs::Wheelspeeds
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:front_left __front_left) 0.0)
    ((:front_right __front_right) 0.0)
    ((:rear_left __rear_left) 0.0)
    ((:rear_right __rear_right) 0.0)
    ((:variance __variance) 0.0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _front_left (float __front_left))
   (setq _front_right (float __front_right))
   (setq _rear_left (float __rear_left))
   (setq _rear_right (float __rear_right))
   (setq _variance (float __variance))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:front_left
   (&optional __front_left)
   (if __front_left (setq _front_left __front_left)) _front_left)
  (:front_right
   (&optional __front_right)
   (if __front_right (setq _front_right __front_right)) _front_right)
  (:rear_left
   (&optional __rear_left)
   (if __rear_left (setq _rear_left __rear_left)) _rear_left)
  (:rear_right
   (&optional __rear_right)
   (if __rear_right (setq _rear_right __rear_right)) _rear_right)
  (:variance
   (&optional __variance)
   (if __variance (setq _variance __variance)) _variance)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; float64 _front_left
    8
    ;; float64 _front_right
    8
    ;; float64 _rear_left
    8
    ;; float64 _rear_right
    8
    ;; float64 _variance
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; float64 _front_left
       (sys::poke _front_left (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _front_right
       (sys::poke _front_right (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _rear_left
       (sys::poke _rear_left (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _rear_right
       (sys::poke _rear_right (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _variance
       (sys::poke _variance (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; float64 _front_left
     (setq _front_left (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _front_right
     (setq _front_right (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _rear_left
     (setq _rear_left (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _rear_right
     (setq _rear_right (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _variance
     (setq _variance (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get fs_msgs::Wheelspeeds :md5sum-) "981b415c45e4921582fc5e4dda54a1c9")
(setf (get fs_msgs::Wheelspeeds :datatype-) "fs_msgs/Wheelspeeds")
(setf (get fs_msgs::Wheelspeeds :definition-)
      "Header header
float64 front_left
float64 front_right
float64 rear_left
float64 rear_right
float64 variance

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

")



(provide :fs_msgs/Wheelspeeds "981b415c45e4921582fc5e4dda54a1c9")


