cmake_minimum_required(VERSION 3.8)
project(rok3_study_pkgs)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang") 
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(gazebo REQUIRED)
find_package(gazebo_dev REQUIRED)
find_package(gazebo_ros REQUIRED)
find_package(Boost REQUIRED)
find_package(Eigen3 3.3 REQUIRED)
find_package(RBDL REQUIRED)

install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

install(DIRECTORY worlds
  DESTINATION share/${PROJECT_NAME}
)

add_library(rok3 SHARED
  src/rok3_plugin.cc
)

target_include_directories(rok3 PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>

  ${GAZEBO_INCLUDE_DIRS}
  ${Boost_INCLUDE_DIRS}
)

target_link_libraries(rok3
    ${GAZEBO_LIBRARIES}
    ${gazebo_ros_LIBRARIES}
    ${Boost_LIBRARIES}
    Eigen3::Eigen
    /usr/local/lib/librbdl.so
    /usr/local/lib/librbdl_urdfreader.so
)

ament_target_dependencies(rok3
  rclcpp
  std_msgs
  sensor_msgs
  geometry_msgs
  gazebo
  gazebo_ros
  gazebo_dev
  Boost
  Eigen3
  RBDL
)

install(TARGETS rok3
  LIBRARY DESTINATION lib
)

ament_export_include_directories(include)
ament_export_libraries(rok3)
ament_export_dependencies(
  rclcpp
  std_msgs
  sensor_msgs
  geometry_msgs
  gazebo
  gazebo_ros
  gazebo_dev
  Boost
  Eigen3
  RBDL
)

ament_package()
