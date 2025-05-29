cmake_minimum_required(VERSION 3.10)
project(Lab5)

set(CMAKE_CXX_STANDARD 17)

# Добавляем флаг -fPIC для всех библиотек
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

# Статическая библиотека
add_library(StaticLib STATIC src/static_lib/DB.cpp)
target_include_directories(StaticLib PUBLIC include)

# Динамическая библиотека 1 (неявное связывание)
add_library(DLL1 SHARED src/dynamic_lib1/DLL1.cpp)
target_include_directories(DLL1 PUBLIC include)
target_link_libraries(DLL1 StaticLib)

# Динамическая библиотека 2 (явное связывание)
add_library(DLL2 SHARED src/dynamic_lib2/DLL2.cpp)
target_include_directories(DLL2 PUBLIC include)
target_link_libraries(DLL2 StaticLib)

# Основная программа
add_executable(MainApp src/main.cpp)
target_include_directories(MainApp PUBLIC include)
target_link_libraries(MainApp StaticLib DLL1)