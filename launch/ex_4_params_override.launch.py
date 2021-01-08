from os import path
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory

from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from nav2_common.launch import RewrittenYaml

def generate_launch_description():
    ros2_cpp_params_example_dir = get_package_share_directory('ros2_cpp_params_example')

    original_params_file = path.join(
        ros2_cpp_params_example_dir, 'params', 'params.yaml')

    param_substitutions = {'my_parameter': 'Parameter overridden with RewrittenYaml!'}

    configured_params = RewrittenYaml(
        source_file=original_params_file,
        param_rewrites=param_substitutions,
        convert_types=True)

    ros2_cpp_params_example_launch_file = path.join(
        get_package_share_directory('ros2_cpp_params_example'),
        'launch', 'ex_3_params_file.launch.py')

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(ros2_cpp_params_example_launch_file),
            launch_arguments={'params_file': configured_params}.items())
    ])
