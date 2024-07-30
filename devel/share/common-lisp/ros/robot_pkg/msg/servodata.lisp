; Auto-generated. Do not edit!


(cl:in-package robot_pkg-msg)


;//! \htmlinclude servodata.msg.html

(cl:defclass <servodata> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (servo0
    :reader servo0
    :initarg :servo0
    :type cl:integer
    :initform 0)
   (servo1
    :reader servo1
    :initarg :servo1
    :type cl:integer
    :initform 0)
   (servo2
    :reader servo2
    :initarg :servo2
    :type cl:integer
    :initform 0)
   (servo3
    :reader servo3
    :initarg :servo3
    :type cl:integer
    :initform 0)
   (servo4
    :reader servo4
    :initarg :servo4
    :type cl:integer
    :initform 0)
   (servo5
    :reader servo5
    :initarg :servo5
    :type cl:integer
    :initform 0))
)

(cl:defclass servodata (<servodata>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <servodata>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'servodata)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name robot_pkg-msg:<servodata> is deprecated: use robot_pkg-msg:servodata instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <servodata>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_pkg-msg:header-val is deprecated.  Use robot_pkg-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'servo0-val :lambda-list '(m))
(cl:defmethod servo0-val ((m <servodata>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_pkg-msg:servo0-val is deprecated.  Use robot_pkg-msg:servo0 instead.")
  (servo0 m))

(cl:ensure-generic-function 'servo1-val :lambda-list '(m))
(cl:defmethod servo1-val ((m <servodata>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_pkg-msg:servo1-val is deprecated.  Use robot_pkg-msg:servo1 instead.")
  (servo1 m))

(cl:ensure-generic-function 'servo2-val :lambda-list '(m))
(cl:defmethod servo2-val ((m <servodata>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_pkg-msg:servo2-val is deprecated.  Use robot_pkg-msg:servo2 instead.")
  (servo2 m))

(cl:ensure-generic-function 'servo3-val :lambda-list '(m))
(cl:defmethod servo3-val ((m <servodata>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_pkg-msg:servo3-val is deprecated.  Use robot_pkg-msg:servo3 instead.")
  (servo3 m))

(cl:ensure-generic-function 'servo4-val :lambda-list '(m))
(cl:defmethod servo4-val ((m <servodata>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_pkg-msg:servo4-val is deprecated.  Use robot_pkg-msg:servo4 instead.")
  (servo4 m))

(cl:ensure-generic-function 'servo5-val :lambda-list '(m))
(cl:defmethod servo5-val ((m <servodata>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_pkg-msg:servo5-val is deprecated.  Use robot_pkg-msg:servo5 instead.")
  (servo5 m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <servodata>) ostream)
  "Serializes a message object of type '<servodata>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let* ((signed (cl:slot-value msg 'servo0)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'servo1)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'servo2)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'servo3)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'servo4)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'servo5)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <servodata>) istream)
  "Deserializes a message object of type '<servodata>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'servo0) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'servo1) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'servo2) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'servo3) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'servo4) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'servo5) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<servodata>)))
  "Returns string type for a message object of type '<servodata>"
  "robot_pkg/servodata")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'servodata)))
  "Returns string type for a message object of type 'servodata"
  "robot_pkg/servodata")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<servodata>)))
  "Returns md5sum for a message object of type '<servodata>"
  "976b722a95bbf1a80c00724ccfc64d4e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'servodata)))
  "Returns md5sum for a message object of type 'servodata"
  "976b722a95bbf1a80c00724ccfc64d4e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<servodata>)))
  "Returns full string definition for message of type '<servodata>"
  (cl:format cl:nil "Header header~%int32 servo0~%int32 servo1~%int32 servo2~%int32 servo3~%int32 servo4~%int32 servo5~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'servodata)))
  "Returns full string definition for message of type 'servodata"
  (cl:format cl:nil "Header header~%int32 servo0~%int32 servo1~%int32 servo2~%int32 servo3~%int32 servo4~%int32 servo5~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <servodata>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4
     4
     4
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <servodata>))
  "Converts a ROS message object to a list"
  (cl:list 'servodata
    (cl:cons ':header (header msg))
    (cl:cons ':servo0 (servo0 msg))
    (cl:cons ':servo1 (servo1 msg))
    (cl:cons ':servo2 (servo2 msg))
    (cl:cons ':servo3 (servo3 msg))
    (cl:cons ':servo4 (servo4 msg))
    (cl:cons ':servo5 (servo5 msg))
))
