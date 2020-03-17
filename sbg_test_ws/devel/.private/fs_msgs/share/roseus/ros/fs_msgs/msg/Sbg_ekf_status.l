;; Auto-generated. Do not edit!


(when (boundp 'fs_msgs::Sbg_ekf_status)
  (if (not (find-package "FS_MSGS"))
    (make-package "FS_MSGS"))
  (shadow 'Sbg_ekf_status (find-package "FS_MSGS")))
(unless (find-package "FS_MSGS::SBG_EKF_STATUS")
  (make-package "FS_MSGS::SBG_EKF_STATUS"))

(in-package "ROS")
;;//! \htmlinclude Sbg_ekf_status.msg.html


(defclass fs_msgs::Sbg_ekf_status
  :super ros::object
  :slots (_COMPUTATION_MODE _ATTITUDE_VALID _HEADING_VALID _VELOCITY_VALID _POSITION_VALID _VERT_REF_USED _MAG_REF_USED _GPS1_VEL_USED _GPS1_POS_USED _GPS1_HDT_USED _GPS2_VEL_USED _GPS2_POS_USED _GPS2_HDT_USED _ODO_USED _DVL_BT_USED _DVL_WT_USED _USBL_USED _AIR_DATA_USED _ZUPT_USED _ALIGN_VALID _DEPTH_USED ))

(defmethod fs_msgs::Sbg_ekf_status
  (:init
   (&key
    ((:COMPUTATION_MODE __COMPUTATION_MODE) 0)
    ((:ATTITUDE_VALID __ATTITUDE_VALID) nil)
    ((:HEADING_VALID __HEADING_VALID) nil)
    ((:VELOCITY_VALID __VELOCITY_VALID) nil)
    ((:POSITION_VALID __POSITION_VALID) nil)
    ((:VERT_REF_USED __VERT_REF_USED) nil)
    ((:MAG_REF_USED __MAG_REF_USED) nil)
    ((:GPS1_VEL_USED __GPS1_VEL_USED) nil)
    ((:GPS1_POS_USED __GPS1_POS_USED) nil)
    ((:GPS1_HDT_USED __GPS1_HDT_USED) nil)
    ((:GPS2_VEL_USED __GPS2_VEL_USED) nil)
    ((:GPS2_POS_USED __GPS2_POS_USED) nil)
    ((:GPS2_HDT_USED __GPS2_HDT_USED) nil)
    ((:ODO_USED __ODO_USED) nil)
    ((:DVL_BT_USED __DVL_BT_USED) nil)
    ((:DVL_WT_USED __DVL_WT_USED) nil)
    ((:USBL_USED __USBL_USED) nil)
    ((:AIR_DATA_USED __AIR_DATA_USED) nil)
    ((:ZUPT_USED __ZUPT_USED) nil)
    ((:ALIGN_VALID __ALIGN_VALID) nil)
    ((:DEPTH_USED __DEPTH_USED) nil)
    )
   (send-super :init)
   (setq _COMPUTATION_MODE (round __COMPUTATION_MODE))
   (setq _ATTITUDE_VALID __ATTITUDE_VALID)
   (setq _HEADING_VALID __HEADING_VALID)
   (setq _VELOCITY_VALID __VELOCITY_VALID)
   (setq _POSITION_VALID __POSITION_VALID)
   (setq _VERT_REF_USED __VERT_REF_USED)
   (setq _MAG_REF_USED __MAG_REF_USED)
   (setq _GPS1_VEL_USED __GPS1_VEL_USED)
   (setq _GPS1_POS_USED __GPS1_POS_USED)
   (setq _GPS1_HDT_USED __GPS1_HDT_USED)
   (setq _GPS2_VEL_USED __GPS2_VEL_USED)
   (setq _GPS2_POS_USED __GPS2_POS_USED)
   (setq _GPS2_HDT_USED __GPS2_HDT_USED)
   (setq _ODO_USED __ODO_USED)
   (setq _DVL_BT_USED __DVL_BT_USED)
   (setq _DVL_WT_USED __DVL_WT_USED)
   (setq _USBL_USED __USBL_USED)
   (setq _AIR_DATA_USED __AIR_DATA_USED)
   (setq _ZUPT_USED __ZUPT_USED)
   (setq _ALIGN_VALID __ALIGN_VALID)
   (setq _DEPTH_USED __DEPTH_USED)
   self)
  (:COMPUTATION_MODE
   (&optional __COMPUTATION_MODE)
   (if __COMPUTATION_MODE (setq _COMPUTATION_MODE __COMPUTATION_MODE)) _COMPUTATION_MODE)
  (:ATTITUDE_VALID
   (&optional __ATTITUDE_VALID)
   (if __ATTITUDE_VALID (setq _ATTITUDE_VALID __ATTITUDE_VALID)) _ATTITUDE_VALID)
  (:HEADING_VALID
   (&optional __HEADING_VALID)
   (if __HEADING_VALID (setq _HEADING_VALID __HEADING_VALID)) _HEADING_VALID)
  (:VELOCITY_VALID
   (&optional __VELOCITY_VALID)
   (if __VELOCITY_VALID (setq _VELOCITY_VALID __VELOCITY_VALID)) _VELOCITY_VALID)
  (:POSITION_VALID
   (&optional __POSITION_VALID)
   (if __POSITION_VALID (setq _POSITION_VALID __POSITION_VALID)) _POSITION_VALID)
  (:VERT_REF_USED
   (&optional __VERT_REF_USED)
   (if __VERT_REF_USED (setq _VERT_REF_USED __VERT_REF_USED)) _VERT_REF_USED)
  (:MAG_REF_USED
   (&optional __MAG_REF_USED)
   (if __MAG_REF_USED (setq _MAG_REF_USED __MAG_REF_USED)) _MAG_REF_USED)
  (:GPS1_VEL_USED
   (&optional __GPS1_VEL_USED)
   (if __GPS1_VEL_USED (setq _GPS1_VEL_USED __GPS1_VEL_USED)) _GPS1_VEL_USED)
  (:GPS1_POS_USED
   (&optional __GPS1_POS_USED)
   (if __GPS1_POS_USED (setq _GPS1_POS_USED __GPS1_POS_USED)) _GPS1_POS_USED)
  (:GPS1_HDT_USED
   (&optional __GPS1_HDT_USED)
   (if __GPS1_HDT_USED (setq _GPS1_HDT_USED __GPS1_HDT_USED)) _GPS1_HDT_USED)
  (:GPS2_VEL_USED
   (&optional __GPS2_VEL_USED)
   (if __GPS2_VEL_USED (setq _GPS2_VEL_USED __GPS2_VEL_USED)) _GPS2_VEL_USED)
  (:GPS2_POS_USED
   (&optional __GPS2_POS_USED)
   (if __GPS2_POS_USED (setq _GPS2_POS_USED __GPS2_POS_USED)) _GPS2_POS_USED)
  (:GPS2_HDT_USED
   (&optional __GPS2_HDT_USED)
   (if __GPS2_HDT_USED (setq _GPS2_HDT_USED __GPS2_HDT_USED)) _GPS2_HDT_USED)
  (:ODO_USED
   (&optional __ODO_USED)
   (if __ODO_USED (setq _ODO_USED __ODO_USED)) _ODO_USED)
  (:DVL_BT_USED
   (&optional __DVL_BT_USED)
   (if __DVL_BT_USED (setq _DVL_BT_USED __DVL_BT_USED)) _DVL_BT_USED)
  (:DVL_WT_USED
   (&optional __DVL_WT_USED)
   (if __DVL_WT_USED (setq _DVL_WT_USED __DVL_WT_USED)) _DVL_WT_USED)
  (:USBL_USED
   (&optional __USBL_USED)
   (if __USBL_USED (setq _USBL_USED __USBL_USED)) _USBL_USED)
  (:AIR_DATA_USED
   (&optional __AIR_DATA_USED)
   (if __AIR_DATA_USED (setq _AIR_DATA_USED __AIR_DATA_USED)) _AIR_DATA_USED)
  (:ZUPT_USED
   (&optional __ZUPT_USED)
   (if __ZUPT_USED (setq _ZUPT_USED __ZUPT_USED)) _ZUPT_USED)
  (:ALIGN_VALID
   (&optional __ALIGN_VALID)
   (if __ALIGN_VALID (setq _ALIGN_VALID __ALIGN_VALID)) _ALIGN_VALID)
  (:DEPTH_USED
   (&optional __DEPTH_USED)
   (if __DEPTH_USED (setq _DEPTH_USED __DEPTH_USED)) _DEPTH_USED)
  (:serialization-length
   ()
   (+
    ;; uint8 _COMPUTATION_MODE
    1
    ;; bool _ATTITUDE_VALID
    1
    ;; bool _HEADING_VALID
    1
    ;; bool _VELOCITY_VALID
    1
    ;; bool _POSITION_VALID
    1
    ;; bool _VERT_REF_USED
    1
    ;; bool _MAG_REF_USED
    1
    ;; bool _GPS1_VEL_USED
    1
    ;; bool _GPS1_POS_USED
    1
    ;; bool _GPS1_HDT_USED
    1
    ;; bool _GPS2_VEL_USED
    1
    ;; bool _GPS2_POS_USED
    1
    ;; bool _GPS2_HDT_USED
    1
    ;; bool _ODO_USED
    1
    ;; bool _DVL_BT_USED
    1
    ;; bool _DVL_WT_USED
    1
    ;; bool _USBL_USED
    1
    ;; bool _AIR_DATA_USED
    1
    ;; bool _ZUPT_USED
    1
    ;; bool _ALIGN_VALID
    1
    ;; bool _DEPTH_USED
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint8 _COMPUTATION_MODE
       (write-byte _COMPUTATION_MODE s)
     ;; bool _ATTITUDE_VALID
       (if _ATTITUDE_VALID (write-byte -1 s) (write-byte 0 s))
     ;; bool _HEADING_VALID
       (if _HEADING_VALID (write-byte -1 s) (write-byte 0 s))
     ;; bool _VELOCITY_VALID
       (if _VELOCITY_VALID (write-byte -1 s) (write-byte 0 s))
     ;; bool _POSITION_VALID
       (if _POSITION_VALID (write-byte -1 s) (write-byte 0 s))
     ;; bool _VERT_REF_USED
       (if _VERT_REF_USED (write-byte -1 s) (write-byte 0 s))
     ;; bool _MAG_REF_USED
       (if _MAG_REF_USED (write-byte -1 s) (write-byte 0 s))
     ;; bool _GPS1_VEL_USED
       (if _GPS1_VEL_USED (write-byte -1 s) (write-byte 0 s))
     ;; bool _GPS1_POS_USED
       (if _GPS1_POS_USED (write-byte -1 s) (write-byte 0 s))
     ;; bool _GPS1_HDT_USED
       (if _GPS1_HDT_USED (write-byte -1 s) (write-byte 0 s))
     ;; bool _GPS2_VEL_USED
       (if _GPS2_VEL_USED (write-byte -1 s) (write-byte 0 s))
     ;; bool _GPS2_POS_USED
       (if _GPS2_POS_USED (write-byte -1 s) (write-byte 0 s))
     ;; bool _GPS2_HDT_USED
       (if _GPS2_HDT_USED (write-byte -1 s) (write-byte 0 s))
     ;; bool _ODO_USED
       (if _ODO_USED (write-byte -1 s) (write-byte 0 s))
     ;; bool _DVL_BT_USED
       (if _DVL_BT_USED (write-byte -1 s) (write-byte 0 s))
     ;; bool _DVL_WT_USED
       (if _DVL_WT_USED (write-byte -1 s) (write-byte 0 s))
     ;; bool _USBL_USED
       (if _USBL_USED (write-byte -1 s) (write-byte 0 s))
     ;; bool _AIR_DATA_USED
       (if _AIR_DATA_USED (write-byte -1 s) (write-byte 0 s))
     ;; bool _ZUPT_USED
       (if _ZUPT_USED (write-byte -1 s) (write-byte 0 s))
     ;; bool _ALIGN_VALID
       (if _ALIGN_VALID (write-byte -1 s) (write-byte 0 s))
     ;; bool _DEPTH_USED
       (if _DEPTH_USED (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint8 _COMPUTATION_MODE
     (setq _COMPUTATION_MODE (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; bool _ATTITUDE_VALID
     (setq _ATTITUDE_VALID (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _HEADING_VALID
     (setq _HEADING_VALID (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _VELOCITY_VALID
     (setq _VELOCITY_VALID (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _POSITION_VALID
     (setq _POSITION_VALID (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _VERT_REF_USED
     (setq _VERT_REF_USED (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _MAG_REF_USED
     (setq _MAG_REF_USED (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _GPS1_VEL_USED
     (setq _GPS1_VEL_USED (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _GPS1_POS_USED
     (setq _GPS1_POS_USED (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _GPS1_HDT_USED
     (setq _GPS1_HDT_USED (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _GPS2_VEL_USED
     (setq _GPS2_VEL_USED (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _GPS2_POS_USED
     (setq _GPS2_POS_USED (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _GPS2_HDT_USED
     (setq _GPS2_HDT_USED (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _ODO_USED
     (setq _ODO_USED (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _DVL_BT_USED
     (setq _DVL_BT_USED (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _DVL_WT_USED
     (setq _DVL_WT_USED (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _USBL_USED
     (setq _USBL_USED (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _AIR_DATA_USED
     (setq _AIR_DATA_USED (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _ZUPT_USED
     (setq _ZUPT_USED (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _ALIGN_VALID
     (setq _ALIGN_VALID (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _DEPTH_USED
     (setq _DEPTH_USED (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get fs_msgs::Sbg_ekf_status :md5sum-) "464794a3821aebe67baf95cbfb19fb69")
(setf (get fs_msgs::Sbg_ekf_status :datatype-) "fs_msgs/Sbg_ekf_status")
(setf (get fs_msgs::Sbg_ekf_status :definition-)
      "uint8 COMPUTATION_MODE
bool ATTITUDE_VALID
bool HEADING_VALID
bool VELOCITY_VALID
bool POSITION_VALID
bool VERT_REF_USED
bool MAG_REF_USED
bool GPS1_VEL_USED
bool GPS1_POS_USED
bool GPS1_HDT_USED
bool GPS2_VEL_USED
bool GPS2_POS_USED
bool GPS2_HDT_USED
bool ODO_USED
bool DVL_BT_USED
bool DVL_WT_USED
bool USBL_USED
bool AIR_DATA_USED
bool ZUPT_USED
bool ALIGN_VALID
bool DEPTH_USED


")



(provide :fs_msgs/Sbg_ekf_status "464794a3821aebe67baf95cbfb19fb69")


