cmake_minimum_required(VERSION 3.7)
project(pointers_on_c)

set(CMAKE_C_STANDARD 99)

set(SOURCE_FILES main.c start/demo.c)
add_executable(pointers_on_c ${SOURCE_FILES})