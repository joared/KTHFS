; Auto-generated. Do not edit!


(cl:in-package fs_msgs-msg)


;//! \htmlinclude Cones.msg.html

(cl:defclass <Cones> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (cones
    :reader cones
    :initarg :cones
    :type (cl:vector fs_msgs-msg:Cone)
   :initform (cl:make-array 0 :element-type 'fs_msgs-msg:Cone :initial-element (cl:make-instance 'fs_msgs-msg:Cone))))
)

(cl:defclass Cones (<Cones>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Cones>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Cones)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name fs_msgs-msg:<Cones> is deprecated: use fs_msgs-msg:Cones instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <Cones>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader fs_msgs-msg:header-val is deprecated.  Use fs_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'cones-val :lambda-list '(m))
(cl:defmethod cones-val ((m <Cones>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader fs_msgs-msg:cones-val is deprecated.  Use fs_msgs-msg:cones instead.")
  (cones m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Cones>) ostream)
  "Serializes a message object of type '<Cones>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'cones))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'cones))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Cones>) istream)
  "Deserializes a message object of type '<Cones>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'cones) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'cones)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'fs_msgs-msg:Cone))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Cones>)))
  "Returns string type for a message object of type '<Cones>"
  "fs_msgs/Cones")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Cones)))
  "Returns string type for a message object of type 'Cones"
  "fs_msgs/Cones")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Cones>)))
  "Returns md5sum for a message object of type '<Cones>"
  "c1c021b091fd72e734d7120dfc8ab7c2")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Cones)))
  "Returns md5sum for a message object of type 'Cones"
  "c1c021b091fd72e734d7120dfc8ab7c2")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Cones>)))
  "Returns full string definition for message of type '<Cones>"
  (cl:format cl:nil "#~%# Array of cones~%#~%~%# Extra information on the message~%# header.stamp: time of the message~%# header.frame_id: frame in which the cones are given~%Header header~%~%# Array of cones~%Cone[] cones~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: fs_msgs/Cone~%#~%# Description of a cone~%#~%~%# 2D-position of the cone~%float64 x~%float64 y~%~%# Color of the cone~%uint8 UNDEFINED = 0~%uint8 YELLOW = 1~%uint8 BLUE = 2~%uint8 SMALL_ORANGE = 3~%uint8 BIG_ORANGE = 4~%~%uint8 color~%~%# Covariance on the position [m^2] (2x2 matrix in row-major order)~%float64[4] covariance~%~%# Confidence in the detection~%float64 probability~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Cones)))
  "Returns full string definition for message of type 'Cones"
  (cl:format cl:nil "#~%# Array of cones~%#~%~%# Extra information on the message~%# header.stamp: time of the message~%# header.frame_id: frame in which the cones are given~%Header header~%~%# Array of cones~%Cone[] cones~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: fs_msgs/Cone~%#~%# Description of a cone~%#~%~%# 2D-position of the cone~%float64 x~%float64 y~%~%# Color of the cone~%uint8 UNDEFINED = 0~%uint8 YELLOW = 1~%uint8 BLUE = 2~%uint8 SMALL_ORANGE = 3~%uint8 BIG_ORANGE = 4~%~%uint8 color~%~%# Covariance on the position [m^2] (2x2 matrix in row-major order)~%float64[4] covariance~%~%# Confidence in the detection~%float64 probability~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Cones>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'cones) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Cones>))
  "Converts a ROS message object to a list"
  (cl:list 'Cones
    (cl:cons ':header (header msg))
    (cl:cons ':cones (cones msg))
))
