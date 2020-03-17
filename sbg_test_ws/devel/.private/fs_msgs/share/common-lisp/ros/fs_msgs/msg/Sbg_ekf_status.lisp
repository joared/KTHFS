; Auto-generated. Do not edit!


(cl:in-package fs_msgs-msg)


;//! \htmlinclude Sbg_ekf_status.msg.html

(cl:defclass <Sbg_ekf_status> (roslisp-msg-protocol:ros-message)
  ((COMPUTATION_MODE
    :reader COMPUTATION_MODE
    :initarg :COMPUTATION_MODE
    :type cl:fixnum
    :initform 0)
   (ATTITUDE_VALID
    :reader ATTITUDE_VALID
    :initarg :ATTITUDE_VALID
    :type cl:boolean
    :initform cl:nil)
   (HEADING_VALID
    :reader HEADING_VALID
    :initarg :HEADING_VALID
    :type cl:boolean
    :initform cl:nil)
   (VELOCITY_VALID
    :reader VELOCITY_VALID
    :initarg :VELOCITY_VALID
    :type cl:boolean
    :initform cl:nil)
   (POSITION_VALID
    :reader POSITION_VALID
    :initarg :POSITION_VALID
    :type cl:boolean
    :initform cl:nil)
   (VERT_REF_USED
    :reader VERT_REF_USED
    :initarg :VERT_REF_USED
    :type cl:boolean
    :initform cl:nil)
   (MAG_REF_USED
    :reader MAG_REF_USED
    :initarg :MAG_REF_USED
    :type cl:boolean
    :initform cl:nil)
   (GPS1_VEL_USED
    :reader GPS1_VEL_USED
    :initarg :GPS1_VEL_USED
    :type cl:boolean
    :initform cl:nil)
   (GPS1_POS_USED
    :reader GPS1_POS_USED
    :initarg :GPS1_POS_USED
    :type cl:boolean
    :initform cl:nil)
   (GPS1_HDT_USED
    :reader GPS1_HDT_USED
    :initarg :GPS1_HDT_USED
    :type cl:boolean
    :initform cl:nil)
   (GPS2_VEL_USED
    :reader GPS2_VEL_USED
    :initarg :GPS2_VEL_USED
    :type cl:boolean
    :initform cl:nil)
   (GPS2_POS_USED
    :reader GPS2_POS_USED
    :initarg :GPS2_POS_USED
    :type cl:boolean
    :initform cl:nil)
   (GPS2_HDT_USED
    :reader GPS2_HDT_USED
    :initarg :GPS2_HDT_USED
    :type cl:boolean
    :initform cl:nil)
   (ODO_USED
    :reader ODO_USED
    :initarg :ODO_USED
    :type cl:boolean
    :initform cl:nil)
   (DVL_BT_USED
    :reader DVL_BT_USED
    :initarg :DVL_BT_USED
    :type cl:boolean
    :initform cl:nil)
   (DVL_WT_USED
    :reader DVL_WT_USED
    :initarg :DVL_WT_USED
    :type cl:boolean
    :initform cl:nil)
   (USBL_USED
    :reader USBL_USED
    :initarg :USBL_USED
    :type cl:boolean
    :initform cl:nil)
   (AIR_DATA_USED
    :reader AIR_DATA_USED
    :initarg :AIR_DATA_USED
    :type cl:boolean
    :initform cl:nil)
   (ZUPT_USED
    :reader ZUPT_USED
    :initarg :ZUPT_USED
    :type cl:boolean
    :initform cl:nil)
   (ALIGN_VALID
    :reader ALIGN_VALID
    :initarg :ALIGN_VALID
    :type cl:boolean
    :initform cl:nil)
   (DEPTH_USED
    :reader DEPTH_USED
    :initarg :DEPTH_USED
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass Sbg_ekf_status (<Sbg_ekf_status>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Sbg_ekf_status>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Sbg_ekf_status)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name fs_msgs-msg:<Sbg_ekf_status> is deprecated: use fs_msgs-msg:Sbg_ekf_status instead.")))

(cl:ensure-generic-function 'COMPUTATION_MODE-val :lambda-list '(m))
(cl:defmethod COMPUTATION_MODE-val ((m <Sbg_ekf_status>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader fs_msgs-msg:COMPUTATION_MODE-val is deprecated.  Use fs_msgs-msg:COMPUTATION_MODE instead.")
  (COMPUTATION_MODE m))

(cl:ensure-generic-function 'ATTITUDE_VALID-val :lambda-list '(m))
(cl:defmethod ATTITUDE_VALID-val ((m <Sbg_ekf_status>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader fs_msgs-msg:ATTITUDE_VALID-val is deprecated.  Use fs_msgs-msg:ATTITUDE_VALID instead.")
  (ATTITUDE_VALID m))

(cl:ensure-generic-function 'HEADING_VALID-val :lambda-list '(m))
(cl:defmethod HEADING_VALID-val ((m <Sbg_ekf_status>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader fs_msgs-msg:HEADING_VALID-val is deprecated.  Use fs_msgs-msg:HEADING_VALID instead.")
  (HEADING_VALID m))

(cl:ensure-generic-function 'VELOCITY_VALID-val :lambda-list '(m))
(cl:defmethod VELOCITY_VALID-val ((m <Sbg_ekf_status>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader fs_msgs-msg:VELOCITY_VALID-val is deprecated.  Use fs_msgs-msg:VELOCITY_VALID instead.")
  (VELOCITY_VALID m))

(cl:ensure-generic-function 'POSITION_VALID-val :lambda-list '(m))
(cl:defmethod POSITION_VALID-val ((m <Sbg_ekf_status>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader fs_msgs-msg:POSITION_VALID-val is deprecated.  Use fs_msgs-msg:POSITION_VALID instead.")
  (POSITION_VALID m))

(cl:ensure-generic-function 'VERT_REF_USED-val :lambda-list '(m))
(cl:defmethod VERT_REF_USED-val ((m <Sbg_ekf_status>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader fs_msgs-msg:VERT_REF_USED-val is deprecated.  Use fs_msgs-msg:VERT_REF_USED instead.")
  (VERT_REF_USED m))

(cl:ensure-generic-function 'MAG_REF_USED-val :lambda-list '(m))
(cl:defmethod MAG_REF_USED-val ((m <Sbg_ekf_status>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader fs_msgs-msg:MAG_REF_USED-val is deprecated.  Use fs_msgs-msg:MAG_REF_USED instead.")
  (MAG_REF_USED m))

(cl:ensure-generic-function 'GPS1_VEL_USED-val :lambda-list '(m))
(cl:defmethod GPS1_VEL_USED-val ((m <Sbg_ekf_status>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader fs_msgs-msg:GPS1_VEL_USED-val is deprecated.  Use fs_msgs-msg:GPS1_VEL_USED instead.")
  (GPS1_VEL_USED m))

(cl:ensure-generic-function 'GPS1_POS_USED-val :lambda-list '(m))
(cl:defmethod GPS1_POS_USED-val ((m <Sbg_ekf_status>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader fs_msgs-msg:GPS1_POS_USED-val is deprecated.  Use fs_msgs-msg:GPS1_POS_USED instead.")
  (GPS1_POS_USED m))

(cl:ensure-generic-function 'GPS1_HDT_USED-val :lambda-list '(m))
(cl:defmethod GPS1_HDT_USED-val ((m <Sbg_ekf_status>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader fs_msgs-msg:GPS1_HDT_USED-val is deprecated.  Use fs_msgs-msg:GPS1_HDT_USED instead.")
  (GPS1_HDT_USED m))

(cl:ensure-generic-function 'GPS2_VEL_USED-val :lambda-list '(m))
(cl:defmethod GPS2_VEL_USED-val ((m <Sbg_ekf_status>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader fs_msgs-msg:GPS2_VEL_USED-val is deprecated.  Use fs_msgs-msg:GPS2_VEL_USED instead.")
  (GPS2_VEL_USED m))

(cl:ensure-generic-function 'GPS2_POS_USED-val :lambda-list '(m))
(cl:defmethod GPS2_POS_USED-val ((m <Sbg_ekf_status>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader fs_msgs-msg:GPS2_POS_USED-val is deprecated.  Use fs_msgs-msg:GPS2_POS_USED instead.")
  (GPS2_POS_USED m))

(cl:ensure-generic-function 'GPS2_HDT_USED-val :lambda-list '(m))
(cl:defmethod GPS2_HDT_USED-val ((m <Sbg_ekf_status>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader fs_msgs-msg:GPS2_HDT_USED-val is deprecated.  Use fs_msgs-msg:GPS2_HDT_USED instead.")
  (GPS2_HDT_USED m))

(cl:ensure-generic-function 'ODO_USED-val :lambda-list '(m))
(cl:defmethod ODO_USED-val ((m <Sbg_ekf_status>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader fs_msgs-msg:ODO_USED-val is deprecated.  Use fs_msgs-msg:ODO_USED instead.")
  (ODO_USED m))

(cl:ensure-generic-function 'DVL_BT_USED-val :lambda-list '(m))
(cl:defmethod DVL_BT_USED-val ((m <Sbg_ekf_status>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader fs_msgs-msg:DVL_BT_USED-val is deprecated.  Use fs_msgs-msg:DVL_BT_USED instead.")
  (DVL_BT_USED m))

(cl:ensure-generic-function 'DVL_WT_USED-val :lambda-list '(m))
(cl:defmethod DVL_WT_USED-val ((m <Sbg_ekf_status>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader fs_msgs-msg:DVL_WT_USED-val is deprecated.  Use fs_msgs-msg:DVL_WT_USED instead.")
  (DVL_WT_USED m))

(cl:ensure-generic-function 'USBL_USED-val :lambda-list '(m))
(cl:defmethod USBL_USED-val ((m <Sbg_ekf_status>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader fs_msgs-msg:USBL_USED-val is deprecated.  Use fs_msgs-msg:USBL_USED instead.")
  (USBL_USED m))

(cl:ensure-generic-function 'AIR_DATA_USED-val :lambda-list '(m))
(cl:defmethod AIR_DATA_USED-val ((m <Sbg_ekf_status>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader fs_msgs-msg:AIR_DATA_USED-val is deprecated.  Use fs_msgs-msg:AIR_DATA_USED instead.")
  (AIR_DATA_USED m))

(cl:ensure-generic-function 'ZUPT_USED-val :lambda-list '(m))
(cl:defmethod ZUPT_USED-val ((m <Sbg_ekf_status>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader fs_msgs-msg:ZUPT_USED-val is deprecated.  Use fs_msgs-msg:ZUPT_USED instead.")
  (ZUPT_USED m))

(cl:ensure-generic-function 'ALIGN_VALID-val :lambda-list '(m))
(cl:defmethod ALIGN_VALID-val ((m <Sbg_ekf_status>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader fs_msgs-msg:ALIGN_VALID-val is deprecated.  Use fs_msgs-msg:ALIGN_VALID instead.")
  (ALIGN_VALID m))

(cl:ensure-generic-function 'DEPTH_USED-val :lambda-list '(m))
(cl:defmethod DEPTH_USED-val ((m <Sbg_ekf_status>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader fs_msgs-msg:DEPTH_USED-val is deprecated.  Use fs_msgs-msg:DEPTH_USED instead.")
  (DEPTH_USED m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Sbg_ekf_status>) ostream)
  "Serializes a message object of type '<Sbg_ekf_status>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'COMPUTATION_MODE)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'ATTITUDE_VALID) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'HEADING_VALID) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'VELOCITY_VALID) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'POSITION_VALID) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'VERT_REF_USED) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'MAG_REF_USED) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'GPS1_VEL_USED) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'GPS1_POS_USED) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'GPS1_HDT_USED) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'GPS2_VEL_USED) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'GPS2_POS_USED) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'GPS2_HDT_USED) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'ODO_USED) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'DVL_BT_USED) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'DVL_WT_USED) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'USBL_USED) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'AIR_DATA_USED) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'ZUPT_USED) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'ALIGN_VALID) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'DEPTH_USED) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Sbg_ekf_status>) istream)
  "Deserializes a message object of type '<Sbg_ekf_status>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'COMPUTATION_MODE)) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'ATTITUDE_VALID) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'HEADING_VALID) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'VELOCITY_VALID) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'POSITION_VALID) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'VERT_REF_USED) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'MAG_REF_USED) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'GPS1_VEL_USED) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'GPS1_POS_USED) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'GPS1_HDT_USED) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'GPS2_VEL_USED) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'GPS2_POS_USED) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'GPS2_HDT_USED) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'ODO_USED) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'DVL_BT_USED) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'DVL_WT_USED) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'USBL_USED) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'AIR_DATA_USED) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'ZUPT_USED) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'ALIGN_VALID) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'DEPTH_USED) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Sbg_ekf_status>)))
  "Returns string type for a message object of type '<Sbg_ekf_status>"
  "fs_msgs/Sbg_ekf_status")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Sbg_ekf_status)))
  "Returns string type for a message object of type 'Sbg_ekf_status"
  "fs_msgs/Sbg_ekf_status")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Sbg_ekf_status>)))
  "Returns md5sum for a message object of type '<Sbg_ekf_status>"
  "464794a3821aebe67baf95cbfb19fb69")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Sbg_ekf_status)))
  "Returns md5sum for a message object of type 'Sbg_ekf_status"
  "464794a3821aebe67baf95cbfb19fb69")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Sbg_ekf_status>)))
  "Returns full string definition for message of type '<Sbg_ekf_status>"
  (cl:format cl:nil "uint8 COMPUTATION_MODE~%bool ATTITUDE_VALID~%bool HEADING_VALID~%bool VELOCITY_VALID~%bool POSITION_VALID~%bool VERT_REF_USED~%bool MAG_REF_USED~%bool GPS1_VEL_USED~%bool GPS1_POS_USED~%bool GPS1_HDT_USED~%bool GPS2_VEL_USED~%bool GPS2_POS_USED~%bool GPS2_HDT_USED~%bool ODO_USED~%bool DVL_BT_USED~%bool DVL_WT_USED~%bool USBL_USED~%bool AIR_DATA_USED~%bool ZUPT_USED~%bool ALIGN_VALID~%bool DEPTH_USED~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Sbg_ekf_status)))
  "Returns full string definition for message of type 'Sbg_ekf_status"
  (cl:format cl:nil "uint8 COMPUTATION_MODE~%bool ATTITUDE_VALID~%bool HEADING_VALID~%bool VELOCITY_VALID~%bool POSITION_VALID~%bool VERT_REF_USED~%bool MAG_REF_USED~%bool GPS1_VEL_USED~%bool GPS1_POS_USED~%bool GPS1_HDT_USED~%bool GPS2_VEL_USED~%bool GPS2_POS_USED~%bool GPS2_HDT_USED~%bool ODO_USED~%bool DVL_BT_USED~%bool DVL_WT_USED~%bool USBL_USED~%bool AIR_DATA_USED~%bool ZUPT_USED~%bool ALIGN_VALID~%bool DEPTH_USED~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Sbg_ekf_status>))
  (cl:+ 0
     1
     1
     1
     1
     1
     1
     1
     1
     1
     1
     1
     1
     1
     1
     1
     1
     1
     1
     1
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Sbg_ekf_status>))
  "Converts a ROS message object to a list"
  (cl:list 'Sbg_ekf_status
    (cl:cons ':COMPUTATION_MODE (COMPUTATION_MODE msg))
    (cl:cons ':ATTITUDE_VALID (ATTITUDE_VALID msg))
    (cl:cons ':HEADING_VALID (HEADING_VALID msg))
    (cl:cons ':VELOCITY_VALID (VELOCITY_VALID msg))
    (cl:cons ':POSITION_VALID (POSITION_VALID msg))
    (cl:cons ':VERT_REF_USED (VERT_REF_USED msg))
    (cl:cons ':MAG_REF_USED (MAG_REF_USED msg))
    (cl:cons ':GPS1_VEL_USED (GPS1_VEL_USED msg))
    (cl:cons ':GPS1_POS_USED (GPS1_POS_USED msg))
    (cl:cons ':GPS1_HDT_USED (GPS1_HDT_USED msg))
    (cl:cons ':GPS2_VEL_USED (GPS2_VEL_USED msg))
    (cl:cons ':GPS2_POS_USED (GPS2_POS_USED msg))
    (cl:cons ':GPS2_HDT_USED (GPS2_HDT_USED msg))
    (cl:cons ':ODO_USED (ODO_USED msg))
    (cl:cons ':DVL_BT_USED (DVL_BT_USED msg))
    (cl:cons ':DVL_WT_USED (DVL_WT_USED msg))
    (cl:cons ':USBL_USED (USBL_USED msg))
    (cl:cons ':AIR_DATA_USED (AIR_DATA_USED msg))
    (cl:cons ':ZUPT_USED (ZUPT_USED msg))
    (cl:cons ':ALIGN_VALID (ALIGN_VALID msg))
    (cl:cons ':DEPTH_USED (DEPTH_USED msg))
))
