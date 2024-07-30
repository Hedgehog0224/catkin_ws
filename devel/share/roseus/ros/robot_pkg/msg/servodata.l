;; Auto-generated. Do not edit!


(when (boundp 'robot_pkg::servodata)
  (if (not (find-package "ROBOT_PKG"))
    (make-package "ROBOT_PKG"))
  (shadow 'servodata (find-package "ROBOT_PKG")))
(unless (find-package "ROBOT_PKG::SERVODATA")
  (make-package "ROBOT_PKG::SERVODATA"))

(in-package "ROS")
;;//! \htmlinclude servodata.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass robot_pkg::servodata
  :super ros::object
  :slots (_header _servo0 _servo1 _servo2 _servo3 _servo4 _servo5 ))

(defmethod robot_pkg::servodata
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:servo0 __servo0) 0)
    ((:servo1 __servo1) 0)
    ((:servo2 __servo2) 0)
    ((:servo3 __servo3) 0)
    ((:servo4 __servo4) 0)
    ((:servo5 __servo5) 0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _servo0 (round __servo0))
   (setq _servo1 (round __servo1))
   (setq _servo2 (round __servo2))
   (setq _servo3 (round __servo3))
   (setq _servo4 (round __servo4))
   (setq _servo5 (round __servo5))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:servo0
   (&optional __servo0)
   (if __servo0 (setq _servo0 __servo0)) _servo0)
  (:servo1
   (&optional __servo1)
   (if __servo1 (setq _servo1 __servo1)) _servo1)
  (:servo2
   (&optional __servo2)
   (if __servo2 (setq _servo2 __servo2)) _servo2)
  (:servo3
   (&optional __servo3)
   (if __servo3 (setq _servo3 __servo3)) _servo3)
  (:servo4
   (&optional __servo4)
   (if __servo4 (setq _servo4 __servo4)) _servo4)
  (:servo5
   (&optional __servo5)
   (if __servo5 (setq _servo5 __servo5)) _servo5)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; int32 _servo0
    4
    ;; int32 _servo1
    4
    ;; int32 _servo2
    4
    ;; int32 _servo3
    4
    ;; int32 _servo4
    4
    ;; int32 _servo5
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; int32 _servo0
       (write-long _servo0 s)
     ;; int32 _servo1
       (write-long _servo1 s)
     ;; int32 _servo2
       (write-long _servo2 s)
     ;; int32 _servo3
       (write-long _servo3 s)
     ;; int32 _servo4
       (write-long _servo4 s)
     ;; int32 _servo5
       (write-long _servo5 s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; int32 _servo0
     (setq _servo0 (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _servo1
     (setq _servo1 (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _servo2
     (setq _servo2 (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _servo3
     (setq _servo3 (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _servo4
     (setq _servo4 (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _servo5
     (setq _servo5 (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get robot_pkg::servodata :md5sum-) "976b722a95bbf1a80c00724ccfc64d4e")
(setf (get robot_pkg::servodata :datatype-) "robot_pkg/servodata")
(setf (get robot_pkg::servodata :definition-)
      "Header header
int32 servo0
int32 servo1
int32 servo2
int32 servo3
int32 servo4
int32 servo5

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



(provide :robot_pkg/servodata "976b722a95bbf1a80c00724ccfc64d4e")


