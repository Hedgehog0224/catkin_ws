
(cl:in-package :asdf)

(defsystem "robot-pkg-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "xy" :depends-on ("_package_xy"))
    (:file "_package_xy" :depends-on ("_package"))
  ))