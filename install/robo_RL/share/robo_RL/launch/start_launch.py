from launch import LaunchDescription
from launch_ros.actions import Node

import os

from ament_index_python.packages import get_package_share_directory

from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    camera_info_bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        # arguments=['/model/vehicle/chatter@std_msgs/String@ignition.msgs.StringMsg'],
        # please remember to match your output type
        arguments=['/world/worlds/model/X1/link/base_link/sensor/camera_front_left/camera_info@sensor_msgs/msg/CameraInfo@gz.msgs.CameraInfo']
    )

    camera_image_bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=['/world/worlds/model/X1/link/base_link/sensor/camera_front_left/image@sensor_msgs/msg/Image@gz.msgs.Image']
    )

    imu_bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=['/imu_topic@sensor_msgs/msg/Imu@gz.msgs.IMU']
    )

    wheel_bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=['/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist'], 
    )
    
    wheel_pub = Node(
        package='robo_RL',
        executable='wheel',
    )


    return LaunchDescription([
        camera_info_bridge,
        camera_image_bridge,
        imu_bridge,
        wheel_bridge,
        wheel_pub,
    ])