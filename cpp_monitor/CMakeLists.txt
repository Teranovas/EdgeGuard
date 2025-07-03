cmake_minimum_required(VERSION 3.10)
project(cpp_monitor)          # ← 이 줄이 중요합니다

set(CMAKE_CXX_STANDARD 17)

add_executable(monitor monitor.cpp)

