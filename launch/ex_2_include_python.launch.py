from os import path
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    ros2_cpp_params_example_dir = get_package_share_directory('ros2_cpp_params_example')
    ex_1_argument_launch_file = path.join(ros2_cpp_params_example_dir, 'launch', 'ex_1_argument.launch.py')

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(ex_1_argument_launch_file),
            launch_arguments={'my_msg': 'Override my_msg!'}.items())
    ])
