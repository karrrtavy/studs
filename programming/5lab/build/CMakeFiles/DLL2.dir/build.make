# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.28

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/kartaviy/Desktop/studs/programming/5lab

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/kartaviy/Desktop/studs/programming/5lab/build

# Include any dependencies generated for this target.
include CMakeFiles/DLL2.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/DLL2.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/DLL2.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/DLL2.dir/flags.make

CMakeFiles/DLL2.dir/src/dynamic_lib2/DLL2.cpp.o: CMakeFiles/DLL2.dir/flags.make
CMakeFiles/DLL2.dir/src/dynamic_lib2/DLL2.cpp.o: /home/kartaviy/Desktop/studs/programming/5lab/src/dynamic_lib2/DLL2.cpp
CMakeFiles/DLL2.dir/src/dynamic_lib2/DLL2.cpp.o: CMakeFiles/DLL2.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/home/kartaviy/Desktop/studs/programming/5lab/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/DLL2.dir/src/dynamic_lib2/DLL2.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/DLL2.dir/src/dynamic_lib2/DLL2.cpp.o -MF CMakeFiles/DLL2.dir/src/dynamic_lib2/DLL2.cpp.o.d -o CMakeFiles/DLL2.dir/src/dynamic_lib2/DLL2.cpp.o -c /home/kartaviy/Desktop/studs/programming/5lab/src/dynamic_lib2/DLL2.cpp

CMakeFiles/DLL2.dir/src/dynamic_lib2/DLL2.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/DLL2.dir/src/dynamic_lib2/DLL2.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/kartaviy/Desktop/studs/programming/5lab/src/dynamic_lib2/DLL2.cpp > CMakeFiles/DLL2.dir/src/dynamic_lib2/DLL2.cpp.i

CMakeFiles/DLL2.dir/src/dynamic_lib2/DLL2.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/DLL2.dir/src/dynamic_lib2/DLL2.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/kartaviy/Desktop/studs/programming/5lab/src/dynamic_lib2/DLL2.cpp -o CMakeFiles/DLL2.dir/src/dynamic_lib2/DLL2.cpp.s

# Object files for target DLL2
DLL2_OBJECTS = \
"CMakeFiles/DLL2.dir/src/dynamic_lib2/DLL2.cpp.o"

# External object files for target DLL2
DLL2_EXTERNAL_OBJECTS =

libDLL2.so: CMakeFiles/DLL2.dir/src/dynamic_lib2/DLL2.cpp.o
libDLL2.so: CMakeFiles/DLL2.dir/build.make
libDLL2.so: libStaticLib.a
libDLL2.so: CMakeFiles/DLL2.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --bold --progress-dir=/home/kartaviy/Desktop/studs/programming/5lab/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX shared library libDLL2.so"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/DLL2.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/DLL2.dir/build: libDLL2.so
.PHONY : CMakeFiles/DLL2.dir/build

CMakeFiles/DLL2.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/DLL2.dir/cmake_clean.cmake
.PHONY : CMakeFiles/DLL2.dir/clean

CMakeFiles/DLL2.dir/depend:
	cd /home/kartaviy/Desktop/studs/programming/5lab/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/kartaviy/Desktop/studs/programming/5lab /home/kartaviy/Desktop/studs/programming/5lab /home/kartaviy/Desktop/studs/programming/5lab/build /home/kartaviy/Desktop/studs/programming/5lab/build /home/kartaviy/Desktop/studs/programming/5lab/build/CMakeFiles/DLL2.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : CMakeFiles/DLL2.dir/depend

