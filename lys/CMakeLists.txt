add_library(lys)

target_sources(lys PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}/character.hpp
)

target_include_directories(lys PUBLIC
    $<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}>
)
