cmake_minimum_required(VERSION 3.8)
project(tb3_autonomy)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclcpp_action REQUIRED)
find_package(nav2_msgs REQUIRED)
find_package(behaviortree_cpp_v3 REQUIRED)
find_package(yaml-cpp REQUIRED)
find_package(tf2 REQUIRED)
find_package(tf2_geometry_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)

# Install launch, config, and BT XML directories
install(DIRECTORY
  launch
  config
  bt_xml
  DESTINATION share/${PROJECT_NAME}
)

# Source files
set(BEHAVIOR_SOURCES
  src/navigation_behaviors.cpp
)

# Dependencies
set(TARGET_DEPENDS
  rclcpp
  rclcpp_action
  nav2_msgs
  behaviortree_cpp_v3
  yaml-cpp
  tf2
  tf2_geometry_msgs
)

include_directories(include)
add_executable(autonomy_node src/autonomy_node.cpp ${BEHAVIOR_SOURCES})
ament_target_dependencies(autonomy_node ${TARGET_DEPENDS})
target_link_libraries(autonomy_node ${YAML_CPP_LIBRARIES})

# Install built binary
install(TARGETS
  autonomy_node
  DESTINATION lib/${PROJECT_NAME}
)

# Tests (optional)
if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  set(ament_cmake_copyright_FOUND TRUE)
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
