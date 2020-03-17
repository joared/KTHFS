;; Auto-generated. Do not edit!


(when (boundp 'fs_msgs::Cone)
  (if (not (find-package "FS_MSGS"))
    (make-package "FS_MSGS"))
  (shadow 'Cone (find-package "FS_MSGS")))
(unless (find-package "FS_MSGS::CONE")
  (make-package "FS_MSGS::CONE"))

(in-package "ROS")
;;//! \htmlinclude Cone.msg.html


(intern "*UNDEFINED*" (find-package "FS_MSGS::CONE"))
(shadow '*UNDEFINED* (find-package "FS_MSGS::CONE"))
(defconstant fs_msgs::Cone::*UNDEFINED* 0)
(intern "*YELLOW*" (find-package "FS_MSGS::CONE"))
(shadow '*YELLOW* (find-package "FS_MSGS::CONE"))
(defconstant fs_msgs::Cone::*YELLOW* 1)
(intern "*BLUE*" (find-package "FS_MSGS::CONE"))
(shadow '*BLUE* (find-package "FS_MSGS::CONE"))
(defconstant fs_msgs::Cone::*BLUE* 2)
(intern "*SMALL_ORANGE*" (find-package "FS_MSGS::CONE"))
(shadow '*SMALL_ORANGE* (find-package "FS_MSGS::CONE"))
(defconstant fs_msgs::Cone::*SMALL_ORANGE* 3)
(intern "*BIG_ORANGE*" (find-package "FS_MSGS::CONE"))
(shadow '*BIG_ORANGE* (find-package "FS_MSGS::CONE"))
(defconstant fs_msgs::Cone::*BIG_ORANGE* 4)
(defclass fs_msgs::Cone
  :super ros::object
  :slots (_x _y _color _covariance _probability ))

(defmethod fs_msgs::Cone
  (:init
   (&key
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    ((:color __color) 0)
    ((:covariance __covariance) (make-array 4 :initial-element 0.0 :element-type :float))
    ((:probability __probability) 0.0)
    )
   (send-super :init)
   (setq _x (float __x))
   (setq _y (float __y))
   (setq _color (round __color))
   (setq _covariance __covariance)
   (setq _probability (float __probability))
   self)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:color
   (&optional __color)
   (if __color (setq _color __color)) _color)
  (:covariance
   (&optional __covariance)
   (if __covariance (setq _covariance __covariance)) _covariance)
  (:probability
   (&optional __probability)
   (if __probability (setq _probability __probability)) _probability)
  (:serialization-length
   ()
   (+
    ;; float64 _x
    8
    ;; float64 _y
    8
    ;; uint8 _color
    1
    ;; float64[4] _covariance
    (* 8    4)
    ;; float64 _probability
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _x
       (sys::poke _x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _y
       (sys::poke _y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; uint8 _color
       (write-byte _color s)
     ;; float64[4] _covariance
     (dotimes (i 4)
       (sys::poke (elt _covariance i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64 _probability
       (sys::poke _probability (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _x
     (setq _x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _y
     (setq _y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; uint8 _color
     (setq _color (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; float64[4] _covariance
   (dotimes (i (length _covariance))
     (setf (elt _covariance i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     )
   ;; float64 _probability
     (setq _probability (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get fs_msgs::Cone :md5sum-) "7c4e8c6cb0ce4d9bafe06a39d73f0f9e")
(setf (get fs_msgs::Cone :datatype-) "fs_msgs/Cone")
(setf (get fs_msgs::Cone :definition-)
      "#
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

")



(provide :fs_msgs/Cone "7c4e8c6cb0ce4d9bafe06a39d73f0f9e")


