from os import path
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.actions import DeclareLaunchArgument, LogInfo
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('my_msg', default_value='Hello World!', description='This is a description!'),
        LogInfo(msg=LaunchConfiguration('my_msg'))
    ])
