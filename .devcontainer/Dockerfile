ARG ROS_DISTRO=jazzy
FROM ros:$ROS_DISTRO

# Create a non-root user for the container
# This is necessary to avoid permission issues between the host and the container
# See https://code.visualstudio.com/remote/advancedcontainers/add-nonroot-user#_creating-a-nonroot-user
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Delete user if its exists in container
RUN if id -u $USER_UID; then userdel `id -un $USER_UID`; fi

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
  && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

# Update package lists and upgrade installed packages
RUN apt-get update && apt-get upgrade -y

# Setup sudo with no password
RUN apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# Install OpenSSH
RUN apt-get install -y openssh-client

# Install rmw_zenoh
RUN apt-get install -y ros-$ROS_DISTRO-rmw-zenoh-cpp

# Install pip
RUN apt-get install -y python3-pip

# Set the default user
USER $USERNAME

# Source ROS environment automatically
RUN echo "source /opt/ros/$ROS_DISTRO/setup.bash" >> $HOME/.bashrc

# Update local rosdep database
RUN rosdep update

# Enable rmw_zenoh by default
ENV RMW_IMPLEMENTATION=rmw_zenoh_cpp

CMD ["/bin/bash"]
