from os import path
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    params_file = LaunchConfiguration('params_file')

    ros2_cpp_params_example_dir = get_package_share_directory('ros2_cpp_params_example')
    default_params_file = path.join(get_package_share_directory("ros2_cpp_params_example"), 'params', 'params.yaml')

    return LaunchDescription([
        DeclareLaunchArgument('params_file', default_value=default_params_file),

        Node(
            package="ros2_cpp_params_example",
            executable="parameter_node",
            name="custom_parameter_node",
            output="screen",
            emulate_tty=True,
            parameters=[params_file]
        )
    ])
