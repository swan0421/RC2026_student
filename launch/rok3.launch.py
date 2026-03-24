import os

from ament_index_python.packages import get_package_share_directory


from launch import LaunchDescription
from launch.actions import ExecuteProcess, IncludeLaunchDescription, RegisterEventHandler
from launch.event_handlers import OnProcessExit
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node

import xacro

def generate_launch_description():
    RobotControl2025_path = os.path.join(
        get_package_share_directory('rok3_study_pkgs'))
                              
    world_file = os.path.join(RobotControl2025_path,
                              'worlds',
                              'rok3.world')
                              
    gazebo = IncludeLaunchDescription(
            PythonLaunchDescriptionSource([os.path.join(
                get_package_share_directory('gazebo_ros'), 'launch'), '/gazebo.launch.py']),
            launch_arguments={'world': world_file, 'pause': 'true'}.items()
         )


    return LaunchDescription([
        gazebo
    ])
