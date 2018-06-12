cmake_minimum_required (VERSION 3.9)

project(lys CXX)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_subdirectory(lys)
