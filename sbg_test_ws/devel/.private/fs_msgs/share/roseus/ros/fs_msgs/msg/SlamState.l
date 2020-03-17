;; Auto-generated. Do not edit!


(when (boundp 'fs_msgs::SlamState)
  (if (not (find-package "FS_MSGS"))
    (make-package "FS_MSGS"))
  (shadow 'SlamState (find-package "FS_MSGS")))
(unless (find-package "FS_MSGS::SLAMSTATE")
  (make-package "FS_MSGS::SLAMSTATE"))

(in-package "ROS")
;;//! \htmlinclude SlamState.msg.html


(defclass fs_msgs::SlamState
  :super ros::object
  :slots (_lap_counter _cones_count_actual _cones_count_all ))

(defmethod fs_msgs::SlamState
  (:init
   (&key
    ((:lap_counter __lap_counter) 0)
    ((:cones_count_actual __cones_count_actual) 0)
    ((:cones_count_all __cones_count_all) 0)
    )
   (send-super :init)
   (setq _lap_counter (round __lap_counter))
   (setq _cones_count_actual (round __cones_count_actual))
   (setq _cones_count_all (round __cones_count_all))
   self)
  (:lap_counter
   (&optional __lap_counter)
   (if __lap_counter (setq _lap_counter __lap_counter)) _lap_counter)
  (:cones_count_actual
   (&optional __cones_count_actual)
   (if __cones_count_actual (setq _cones_count_actual __cones_count_actual)) _cones_count_actual)
  (:cones_count_all
   (&optional __cones_count_all)
   (if __cones_count_all (setq _cones_count_all __cones_count_all)) _cones_count_all)
  (:serialization-length
   ()
   (+
    ;; uint8 _lap_counter
    1
    ;; int32 _cones_count_actual
    4
    ;; int32 _cones_count_all
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint8 _lap_counter
       (write-byte _lap_counter s)
     ;; int32 _cones_count_actual
       (write-long _cones_count_actual s)
     ;; int32 _cones_count_all
       (write-long _cones_count_all s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint8 _lap_counter
     (setq _lap_counter (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; int32 _cones_count_actual
     (setq _cones_count_actual (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _cones_count_all
     (setq _cones_count_all (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get fs_msgs::SlamState :md5sum-) "a77c00628d1b607092740dc262c21142")
(setf (get fs_msgs::SlamState :datatype-) "fs_msgs/SlamState")
(setf (get fs_msgs::SlamState :definition-)
      "#
# Give the lap count and number of cones
#

uint8 lap_counter
int32 cones_count_actual
int32 cones_count_all

")



(provide :fs_msgs/SlamState "a77c00628d1b607092740dc262c21142")


