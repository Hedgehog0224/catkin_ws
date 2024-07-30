
(cl:in-package :asdf)

(defsystem "robot_pkg-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "servodata" :depends-on ("_package_servodata"))
    (:file "_package_servodata" :depends-on ("_package"))
    (:file "xy" :depends-on ("_package_xy"))
    (:file "_package_xy" :depends-on ("_package"))
  ))