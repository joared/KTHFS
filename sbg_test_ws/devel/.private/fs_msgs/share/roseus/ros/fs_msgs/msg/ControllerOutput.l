;; Auto-generated. Do not edit!


(when (boundp 'fs_msgs::ControllerOutput)
  (if (not (find-package "FS_MSGS"))
    (make-package "FS_MSGS"))
  (shadow 'ControllerOutput (find-package "FS_MSGS")))
(unless (find-package "FS_MSGS::CONTROLLEROUTPUT")
  (make-package "FS_MSGS::CONTROLLEROUTPUT"))

(in-package "ROS")
;;//! \htmlinclude ControllerOutput.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass fs_msgs::ControllerOutput
  :super ros::object
  :slots (_header _steering _torque _velocity ))

(defmethod fs_msgs::ControllerOutput
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:steering __steering) 0.0)
    ((:torque __torque) 0.0)
    ((:velocity __velocity) 0.0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _steering (float __steering))
   (setq _torque (float __torque))
   (setq _velocity (float __velocity))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:steering
   (&optional __steering)
   (if __steering (setq _steering __steering)) _steering)
  (:torque
   (&optional __torque)
   (if __torque (setq _torque __torque)) _torque)
  (:velocity
   (&optional __velocity)
   (if __velocity (setq _velocity __velocity)) _velocity)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; float64 _steering
    8
    ;; float64 _torque
    8
    ;; float64 _velocity
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; float64 _steering
       (sys::poke _steering (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _torque
       (sys::poke _torque (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _velocity
       (sys::poke _velocity (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; float64 _steering
     (setq _steering (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _torque
     (setq _torque (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _velocity
     (setq _velocity (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get fs_msgs::ControllerOutput :md5sum-) "54e8a5e2d902d5c9c3fb89ad8e3f99e8")
(setf (get fs_msgs::ControllerOutput :datatype-) "fs_msgs/ControllerOutput")
(setf (get fs_msgs::ControllerOutput :definition-)
      "Header header
float64 steering
float64 torque
float64 velocity

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



(provide :fs_msgs/ControllerOutput "54e8a5e2d902d5c9c3fb89ad8e3f99e8")


