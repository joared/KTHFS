; Auto-generated. Do not edit!


(cl:in-package fs_msgs-msg)


;//! \htmlinclude ConesWithStats.msg.html

(cl:defclass <ConesWithStats> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (cones
    :reader cones
    :initarg :cones
    :type (cl:vector fs_msgs-msg:ConeWithStats)
   :initform (cl:make-array 0 :element-type 'fs_msgs-msg:ConeWithStats :initial-element (cl:make-instance 'fs_msgs-msg:ConeWithStats))))
)

(cl:defclass ConesWithStats (<ConesWithStats>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ConesWithStats>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ConesWithStats)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name fs_msgs-msg:<ConesWithStats> is deprecated: use fs_msgs-msg:ConesWithStats instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <ConesWithStats>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader fs_msgs-msg:header-val is deprecated.  Use fs_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'cones-val :lambda-list '(m))
(cl:defmethod cones-val ((m <ConesWithStats>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader fs_msgs-msg:cones-val is deprecated.  Use fs_msgs-msg:cones instead.")
  (cones m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ConesWithStats>) ostream)
  "Serializes a message object of type '<ConesWithStats>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'cones))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'cones))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ConesWithStats>) istream)
  "Deserializes a message object of type '<ConesWithStats>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'cones) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'cones)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'fs_msgs-msg:ConeWithStats))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ConesWithStats>)))
  "Returns string type for a message object of type '<ConesWithStats>"
  "fs_msgs/ConesWithStats")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ConesWithStats)))
  "Returns string type for a message object of type 'ConesWithStats"
  "fs_msgs/ConesWithStats")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ConesWithStats>)))
  "Returns md5sum for a message object of type '<ConesWithStats>"
  "6718c9a6b3d40b0468a363f35c8b1688")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ConesWithStats)))
  "Returns md5sum for a message object of type 'ConesWithStats"
  "6718c9a6b3d40b0468a363f35c8b1688")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ConesWithStats>)))
  "Returns full string definition for message of type '<ConesWithStats>"
  (cl:format cl:nil "#~%# Array of cones with statistics~%#~%~%# Extra information on the message~%# header.stamp: time of the message~%# header.frame_id: frame in which the cones are given~%Header header~%~%# Array of cones~%ConeWithStats[] cones~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: fs_msgs/ConeWithStats~%#~%# Description of a cone with statistics~%#~%~%Cone cone~%ConeStats stats~%~%================================================================================~%MSG: fs_msgs/Cone~%#~%# Description of a cone~%#~%~%# 2D-position of the cone~%float64 x~%float64 y~%~%# Color of the cone~%uint8 UNDEFINED = 0~%uint8 YELLOW = 1~%uint8 BLUE = 2~%uint8 SMALL_ORANGE = 3~%uint8 BIG_ORANGE = 4~%~%uint8 color~%~%# Covariance on the position [m^2] (2x2 matrix in row-major order)~%float64[4] covariance~%~%# Confidence in the detection~%float64 probability~%~%================================================================================~%MSG: fs_msgs/ConeStats~%#~%# Statistics of a cone~%#~%~%# Number of times the cone has been seen~%int32 nbr_detections~%~%# Color counters~%int32 yellow_counter~%int32 blue_counter~%~%# Average innovation (innovation = mapped position - detected position)~%float32 avg_innovation_x~%float32 avg_innovation_y~%~%# Standard deviation of innovation norms~%float32 std_innovation~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ConesWithStats)))
  "Returns full string definition for message of type 'ConesWithStats"
  (cl:format cl:nil "#~%# Array of cones with statistics~%#~%~%# Extra information on the message~%# header.stamp: time of the message~%# header.frame_id: frame in which the cones are given~%Header header~%~%# Array of cones~%ConeWithStats[] cones~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: fs_msgs/ConeWithStats~%#~%# Description of a cone with statistics~%#~%~%Cone cone~%ConeStats stats~%~%================================================================================~%MSG: fs_msgs/Cone~%#~%# Description of a cone~%#~%~%# 2D-position of the cone~%float64 x~%float64 y~%~%# Color of the cone~%uint8 UNDEFINED = 0~%uint8 YELLOW = 1~%uint8 BLUE = 2~%uint8 SMALL_ORANGE = 3~%uint8 BIG_ORANGE = 4~%~%uint8 color~%~%# Covariance on the position [m^2] (2x2 matrix in row-major order)~%float64[4] covariance~%~%# Confidence in the detection~%float64 probability~%~%================================================================================~%MSG: fs_msgs/ConeStats~%#~%# Statistics of a cone~%#~%~%# Number of times the cone has been seen~%int32 nbr_detections~%~%# Color counters~%int32 yellow_counter~%int32 blue_counter~%~%# Average innovation (innovation = mapped position - detected position)~%float32 avg_innovation_x~%float32 avg_innovation_y~%~%# Standard deviation of innovation norms~%float32 std_innovation~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ConesWithStats>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'cones) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ConesWithStats>))
  "Converts a ROS message object to a list"
  (cl:list 'ConesWithStats
    (cl:cons ':header (header msg))
    (cl:cons ':cones (cones msg))
))
