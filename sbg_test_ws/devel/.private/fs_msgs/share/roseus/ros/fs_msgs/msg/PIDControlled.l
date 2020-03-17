;; Auto-generated. Do not edit!


(when (boundp 'fs_msgs::PIDControlled)
  (if (not (find-package "FS_MSGS"))
    (make-package "FS_MSGS"))
  (shadow 'PIDControlled (find-package "FS_MSGS")))
(unless (find-package "FS_MSGS::PIDCONTROLLED")
  (make-package "FS_MSGS::PIDCONTROLLED"))

(in-package "ROS")
;;//! \htmlinclude PIDControlled.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass fs_msgs::PIDControlled
  :super ros::object
  :slots (_header _torque _brake _steering ))

(defmethod fs_msgs::PIDControlled
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:torque __torque) 0.0)
    ((:brake __brake) 0.0)
    ((:steering __steering) 0.0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _torque (float __torque))
   (setq _brake (float __brake))
   (setq _steering (float __steering))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:torque
   (&optional __torque)
   (if __torque (setq _torque __torque)) _torque)
  (:brake
   (&optional __brake)
   (if __brake (setq _brake __brake)) _brake)
  (:steering
   (&optional __steering)
   (if __steering (setq _steering __steering)) _steering)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; float64 _torque
    8
    ;; float64 _brake
    8
    ;; float64 _steering
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; float64 _torque
       (sys::poke _torque (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _brake
       (sys::poke _brake (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _steering
       (sys::poke _steering (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; float64 _torque
     (setq _torque (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _brake
     (setq _brake (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _steering
     (setq _steering (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get fs_msgs::PIDControlled :md5sum-) "17fe00737ba0ab47d224bd15cc789c77")
(setf (get fs_msgs::PIDControlled :datatype-) "fs_msgs/PIDControlled")
(setf (get fs_msgs::PIDControlled :definition-)
      "Header header
float64 torque
float64 brake
float64 steering

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



(provide :fs_msgs/PIDControlled "17fe00737ba0ab47d224bd15cc789c77")


