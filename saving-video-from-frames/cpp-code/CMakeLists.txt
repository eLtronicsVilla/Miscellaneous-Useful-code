cmake_minimum_required(VERSION 2.6)
project( save_video )
find_package( OpenCV REQUIRED )
add_executable( save_video saving-video-from-frame.cpp )
target_link_libraries( save_video ${OpenCV_LIBS} )
