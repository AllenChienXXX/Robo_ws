from launch import LaunchDescription
from launch_ros.actions import Node

import os

from ament_index_python.packages import get_package_share_directory

from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        # arguments=['/model/vehicle/chatter@std_msgs/String@ignition.msgs.StringMsg'],
        # please remember to match your output type
        arguments=['/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist'],
    )
    
    wheel_pub = Node(
        package='test',
        executable='wheel',
    )


    return LaunchDescription([
        bridge,
        wheel_pub,
    ])