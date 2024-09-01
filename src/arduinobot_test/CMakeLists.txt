cmake_minimum_required(VERSION 3.0.2)
project(arduinobot_test)


find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
)




add_service_files(
  FILES
  AddTwoInts.srv

)




generate_messages(
  DEPENDENCIES
  std_msgs
)


catkin_package(

)


include_directories(

  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(
  PROGRAMS
  #location in package here
  scripts/simple_service.py
  scripts/simple_client.py

  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

