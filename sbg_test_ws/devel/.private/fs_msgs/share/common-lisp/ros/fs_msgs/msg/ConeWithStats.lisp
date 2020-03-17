; Auto-generated. Do not edit!


(cl:in-package fs_msgs-msg)


;//! \htmlinclude ConeWithStats.msg.html

(cl:defclass <ConeWithStats> (roslisp-msg-protocol:ros-message)
  ((cone
    :reader cone
    :initarg :cone
    :type fs_msgs-msg:Cone
    :initform (cl:make-instance 'fs_msgs-msg:Cone))
   (stats
    :reader stats
    :initarg :stats
    :type fs_msgs-msg:ConeStats
    :initform (cl:make-instance 'fs_msgs-msg:ConeStats)))
)

(cl:defclass ConeWithStats (<ConeWithStats>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ConeWithStats>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ConeWithStats)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name fs_msgs-msg:<ConeWithStats> is deprecated: use fs_msgs-msg:ConeWithStats instead.")))

(cl:ensure-generic-function 'cone-val :lambda-list '(m))
(cl:defmethod cone-val ((m <ConeWithStats>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader fs_msgs-msg:cone-val is deprecated.  Use fs_msgs-msg:cone instead.")
  (cone m))

(cl:ensure-generic-function 'stats-val :lambda-list '(m))
(cl:defmethod stats-val ((m <ConeWithStats>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader fs_msgs-msg:stats-val is deprecated.  Use fs_msgs-msg:stats instead.")
  (stats m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ConeWithStats>) ostream)
  "Serializes a message object of type '<ConeWithStats>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'cone) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'stats) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ConeWithStats>) istream)
  "Deserializes a message object of type '<ConeWithStats>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'cone) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'stats) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ConeWithStats>)))
  "Returns string type for a message object of type '<ConeWithStats>"
  "fs_msgs/ConeWithStats")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ConeWithStats)))
  "Returns string type for a message object of type 'ConeWithStats"
  "fs_msgs/ConeWithStats")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ConeWithStats>)))
  "Returns md5sum for a message object of type '<ConeWithStats>"
  "bc6abd39812a69dee6e5d6c6dbebf194")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ConeWithStats)))
  "Returns md5sum for a message object of type 'ConeWithStats"
  "bc6abd39812a69dee6e5d6c6dbebf194")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ConeWithStats>)))
  "Returns full string definition for message of type '<ConeWithStats>"
  (cl:format cl:nil "#~%# Description of a cone with statistics~%#~%~%Cone cone~%ConeStats stats~%~%================================================================================~%MSG: fs_msgs/Cone~%#~%# Description of a cone~%#~%~%# 2D-position of the cone~%float64 x~%float64 y~%~%# Color of the cone~%uint8 UNDEFINED = 0~%uint8 YELLOW = 1~%uint8 BLUE = 2~%uint8 SMALL_ORANGE = 3~%uint8 BIG_ORANGE = 4~%~%uint8 color~%~%# Covariance on the position [m^2] (2x2 matrix in row-major order)~%float64[4] covariance~%~%# Confidence in the detection~%float64 probability~%~%================================================================================~%MSG: fs_msgs/ConeStats~%#~%# Statistics of a cone~%#~%~%# Number of times the cone has been seen~%int32 nbr_detections~%~%# Color counters~%int32 yellow_counter~%int32 blue_counter~%~%# Average innovation (innovation = mapped position - detected position)~%float32 avg_innovation_x~%float32 avg_innovation_y~%~%# Standard deviation of innovation norms~%float32 std_innovation~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ConeWithStats)))
  "Returns full string definition for message of type 'ConeWithStats"
  (cl:format cl:nil "#~%# Description of a cone with statistics~%#~%~%Cone cone~%ConeStats stats~%~%================================================================================~%MSG: fs_msgs/Cone~%#~%# Description of a cone~%#~%~%# 2D-position of the cone~%float64 x~%float64 y~%~%# Color of the cone~%uint8 UNDEFINED = 0~%uint8 YELLOW = 1~%uint8 BLUE = 2~%uint8 SMALL_ORANGE = 3~%uint8 BIG_ORANGE = 4~%~%uint8 color~%~%# Covariance on the position [m^2] (2x2 matrix in row-major order)~%float64[4] covariance~%~%# Confidence in the detection~%float64 probability~%~%================================================================================~%MSG: fs_msgs/ConeStats~%#~%# Statistics of a cone~%#~%~%# Number of times the cone has been seen~%int32 nbr_detections~%~%# Color counters~%int32 yellow_counter~%int32 blue_counter~%~%# Average innovation (innovation = mapped position - detected position)~%float32 avg_innovation_x~%float32 avg_innovation_y~%~%# Standard deviation of innovation norms~%float32 std_innovation~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ConeWithStats>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'cone))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'stats))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ConeWithStats>))
  "Converts a ROS message object to a list"
  (cl:list 'ConeWithStats
    (cl:cons ':cone (cone msg))
    (cl:cons ':stats (stats msg))
))
