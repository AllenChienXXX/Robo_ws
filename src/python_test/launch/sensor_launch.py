from launch import LaunchDescription
from launch_ros.actions import Node

import os

from ament_index_python.packages import get_package_share_directory

from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    chassis = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        # arguments=['/model/vehicle/chatter@std_msgs/String@ignition.msgs.StringMsg'],
        # please remember to match your output type
        arguments=['/sen_vel@geometry_msgs/msg/Twist@gz.msgs.Twist'],
    )

    sensor = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        #lidar bridge
        arguments=['/lidar@sensor_msgs/msg/LaserScan@gz.msgs.LaserScan'],
        #IMU bridge
        # arguments=['/imu@sensor_msgs/msg/Imu@ignition.msgs.IMU'],
    )
    
    wheel_pub = Node(
        package='python_test',
        executable='wheel',
    )

    # imu_process = Node(
    #     package='test',
    #     executable='imu_sensor',
    # )

    lidar_process = Node(
        package='python_test',
        executable='sensor',
    )    


    return LaunchDescription([
        chassis,
        sensor,
        # wheel_pub,
        lidar_process,
    ])