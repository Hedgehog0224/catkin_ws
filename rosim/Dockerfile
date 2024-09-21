# This is an auto generatedDockerfile for ros:ros-base
# generated from docker_images/create_ros_image.Dockerfile.em
FROM ros:noetic-ros-core-focal
COPY /.Xauthority /
# install bootstrap tools
RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    python3-rosdep \
    python3-rosinstall \
    python3-vcstools \
    firefox \
    xauth \
    && rm -rf /var/lib/apt/lists/*

# bootstrap rosdep
RUN rosdep init && \
  rosdep fix-permissions --rosdistro  $ROS_DISTRO

#RUN rosdep init && 
#  rosdep update -f --rosdistro $ROS_DISTRO

# install ros packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    ros-noetic-ros-base=1.5.0-1* \
    nano\
    git\
    python3-pip\
    ros-noetic-joy\
    ros-noetic-rplidar-ros\
    rviz\
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install evdev
RUN python3 -m pip install RPi.GPIO
RUN python3 -m pip install pyserial
RUN python3 -m pip install board
RUN python3 -m pip install opencv-contrib-python
RUN pip3 install adafruit-circuitpython-pca9685
RUN pip3 install adafruit-circuitpython-motor
RUN pip3 install visual-kinematics
EXPOSE 8887
# CMD firefox
# CMD rviz

COPY .bashrc /root/
