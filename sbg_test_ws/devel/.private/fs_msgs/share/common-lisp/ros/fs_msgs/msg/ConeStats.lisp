; Auto-generated. Do not edit!


(cl:in-package fs_msgs-msg)


;//! \htmlinclude ConeStats.msg.html

(cl:defclass <ConeStats> (roslisp-msg-protocol:ros-message)
  ((nbr_detections
    :reader nbr_detections
    :initarg :nbr_detections
    :type cl:integer
    :initform 0)
   (yellow_counter
    :reader yellow_counter
    :initarg :yellow_counter
    :type cl:integer
    :initform 0)
   (blue_counter
    :reader blue_counter
    :initarg :blue_counter
    :type cl:integer
    :initform 0)
   (avg_innovation_x
    :reader avg_innovation_x
    :initarg :avg_innovation_x
    :type cl:float
    :initform 0.0)
   (avg_innovation_y
    :reader avg_innovation_y
    :initarg :avg_innovation_y
    :type cl:float
    :initform 0.0)
   (std_innovation
    :reader std_innovation
    :initarg :std_innovation
    :type cl:float
    :initform 0.0))
)

(cl:defclass ConeStats (<ConeStats>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ConeStats>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ConeStats)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name fs_msgs-msg:<ConeStats> is deprecated: use fs_msgs-msg:ConeStats instead.")))

(cl:ensure-generic-function 'nbr_detections-val :lambda-list '(m))
(cl:defmethod nbr_detections-val ((m <ConeStats>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader fs_msgs-msg:nbr_detections-val is deprecated.  Use fs_msgs-msg:nbr_detections instead.")
  (nbr_detections m))

(cl:ensure-generic-function 'yellow_counter-val :lambda-list '(m))
(cl:defmethod yellow_counter-val ((m <ConeStats>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader fs_msgs-msg:yellow_counter-val is deprecated.  Use fs_msgs-msg:yellow_counter instead.")
  (yellow_counter m))

(cl:ensure-generic-function 'blue_counter-val :lambda-list '(m))
(cl:defmethod blue_counter-val ((m <ConeStats>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader fs_msgs-msg:blue_counter-val is deprecated.  Use fs_msgs-msg:blue_counter instead.")
  (blue_counter m))

(cl:ensure-generic-function 'avg_innovation_x-val :lambda-list '(m))
(cl:defmethod avg_innovation_x-val ((m <ConeStats>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader fs_msgs-msg:avg_innovation_x-val is deprecated.  Use fs_msgs-msg:avg_innovation_x instead.")
  (avg_innovation_x m))

(cl:ensure-generic-function 'avg_innovation_y-val :lambda-list '(m))
(cl:defmethod avg_innovation_y-val ((m <ConeStats>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader fs_msgs-msg:avg_innovation_y-val is deprecated.  Use fs_msgs-msg:avg_innovation_y instead.")
  (avg_innovation_y m))

(cl:ensure-generic-function 'std_innovation-val :lambda-list '(m))
(cl:defmethod std_innovation-val ((m <ConeStats>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader fs_msgs-msg:std_innovation-val is deprecated.  Use fs_msgs-msg:std_innovation instead.")
  (std_innovation m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ConeStats>) ostream)
  "Serializes a message object of type '<ConeStats>"
  (cl:let* ((signed (cl:slot-value msg 'nbr_detections)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'yellow_counter)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'blue_counter)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'avg_innovation_x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'avg_innovation_y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'std_innovation))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ConeStats>) istream)
  "Deserializes a message object of type '<ConeStats>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'nbr_detections) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'yellow_counter) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'blue_counter) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'avg_innovation_x) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'avg_innovation_y) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'std_innovation) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ConeStats>)))
  "Returns string type for a message object of type '<ConeStats>"
  "fs_msgs/ConeStats")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ConeStats)))
  "Returns string type for a message object of type 'ConeStats"
  "fs_msgs/ConeStats")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ConeStats>)))
  "Returns md5sum for a message object of type '<ConeStats>"
  "e29d797ff713ceaa2ace1ff34729c17e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ConeStats)))
  "Returns md5sum for a message object of type 'ConeStats"
  "e29d797ff713ceaa2ace1ff34729c17e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ConeStats>)))
  "Returns full string definition for message of type '<ConeStats>"
  (cl:format cl:nil "#~%# Statistics of a cone~%#~%~%# Number of times the cone has been seen~%int32 nbr_detections~%~%# Color counters~%int32 yellow_counter~%int32 blue_counter~%~%# Average innovation (innovation = mapped position - detected position)~%float32 avg_innovation_x~%float32 avg_innovation_y~%~%# Standard deviation of innovation norms~%float32 std_innovation~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ConeStats)))
  "Returns full string definition for message of type 'ConeStats"
  (cl:format cl:nil "#~%# Statistics of a cone~%#~%~%# Number of times the cone has been seen~%int32 nbr_detections~%~%# Color counters~%int32 yellow_counter~%int32 blue_counter~%~%# Average innovation (innovation = mapped position - detected position)~%float32 avg_innovation_x~%float32 avg_innovation_y~%~%# Standard deviation of innovation norms~%float32 std_innovation~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ConeStats>))
  (cl:+ 0
     4
     4
     4
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ConeStats>))
  "Converts a ROS message object to a list"
  (cl:list 'ConeStats
    (cl:cons ':nbr_detections (nbr_detections msg))
    (cl:cons ':yellow_counter (yellow_counter msg))
    (cl:cons ':blue_counter (blue_counter msg))
    (cl:cons ':avg_innovation_x (avg_innovation_x msg))
    (cl:cons ':avg_innovation_y (avg_innovation_y msg))
    (cl:cons ':std_innovation (std_innovation msg))
))
