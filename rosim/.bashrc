source /opt/ros/$ROS_DISTRO/setup.bash
source $PROJECT_DIR/devel/setup.bash
export ROS_IP=$(hostname -i)
export ROS_HOSTNAME=localhost
export ROS_MASTER_URI=http://localhost:11311
export XAUTHORITY=/.Xauthority
cd /root/ && rm -r rpcam-apps && cd -

cd /root/ && git clone https://github.com/raspberrypi/rpicam-apps.git && cd -
#cd /root/ && git clone https://github.com/Hedgehog0224/catkin_ws.git && cd -
#cd /root/catkin_ws/ && catkin_make && cd -

#source /root/catkin_ws/devel/setup.bash

#cd /root/catkin_ws/scr/ && rosnode list
