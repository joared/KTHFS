; Auto-generated. Do not edit!


(cl:in-package fs_msgs-msg)


;//! \htmlinclude SlamState.msg.html

(cl:defclass <SlamState> (roslisp-msg-protocol:ros-message)
  ((lap_counter
    :reader lap_counter
    :initarg :lap_counter
    :type cl:fixnum
    :initform 0)
   (cones_count_actual
    :reader cones_count_actual
    :initarg :cones_count_actual
    :type cl:integer
    :initform 0)
   (cones_count_all
    :reader cones_count_all
    :initarg :cones_count_all
    :type cl:integer
    :initform 0))
)

(cl:defclass SlamState (<SlamState>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SlamState>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SlamState)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name fs_msgs-msg:<SlamState> is deprecated: use fs_msgs-msg:SlamState instead.")))

(cl:ensure-generic-function 'lap_counter-val :lambda-list '(m))
(cl:defmethod lap_counter-val ((m <SlamState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader fs_msgs-msg:lap_counter-val is deprecated.  Use fs_msgs-msg:lap_counter instead.")
  (lap_counter m))

(cl:ensure-generic-function 'cones_count_actual-val :lambda-list '(m))
(cl:defmethod cones_count_actual-val ((m <SlamState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader fs_msgs-msg:cones_count_actual-val is deprecated.  Use fs_msgs-msg:cones_count_actual instead.")
  (cones_count_actual m))

(cl:ensure-generic-function 'cones_count_all-val :lambda-list '(m))
(cl:defmethod cones_count_all-val ((m <SlamState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader fs_msgs-msg:cones_count_all-val is deprecated.  Use fs_msgs-msg:cones_count_all instead.")
  (cones_count_all m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SlamState>) ostream)
  "Serializes a message object of type '<SlamState>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'lap_counter)) ostream)
  (cl:let* ((signed (cl:slot-value msg 'cones_count_actual)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'cones_count_all)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SlamState>) istream)
  "Deserializes a message object of type '<SlamState>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'lap_counter)) (cl:read-byte istream))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'cones_count_actual) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'cones_count_all) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SlamState>)))
  "Returns string type for a message object of type '<SlamState>"
  "fs_msgs/SlamState")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SlamState)))
  "Returns string type for a message object of type 'SlamState"
  "fs_msgs/SlamState")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SlamState>)))
  "Returns md5sum for a message object of type '<SlamState>"
  "a77c00628d1b607092740dc262c21142")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SlamState)))
  "Returns md5sum for a message object of type 'SlamState"
  "a77c00628d1b607092740dc262c21142")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SlamState>)))
  "Returns full string definition for message of type '<SlamState>"
  (cl:format cl:nil "#~%# Give the lap count and number of cones~%#~%~%uint8 lap_counter~%int32 cones_count_actual~%int32 cones_count_all~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SlamState)))
  "Returns full string definition for message of type 'SlamState"
  (cl:format cl:nil "#~%# Give the lap count and number of cones~%#~%~%uint8 lap_counter~%int32 cones_count_actual~%int32 cones_count_all~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SlamState>))
  (cl:+ 0
     1
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SlamState>))
  "Converts a ROS message object to a list"
  (cl:list 'SlamState
    (cl:cons ':lap_counter (lap_counter msg))
    (cl:cons ':cones_count_actual (cones_count_actual msg))
    (cl:cons ':cones_count_all (cones_count_all msg))
))
