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
include CMakeFiles/DLL1.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/DLL1.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/DLL1.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/DLL1.dir/flags.make

CMakeFiles/DLL1.dir/src/dynamic_lib1/DLL1.cpp.o: CMakeFiles/DLL1.dir/flags.make
CMakeFiles/DLL1.dir/src/dynamic_lib1/DLL1.cpp.o: /home/kartaviy/Desktop/studs/programming/5lab/src/dynamic_lib1/DLL1.cpp
CMakeFiles/DLL1.dir/src/dynamic_lib1/DLL1.cpp.o: CMakeFiles/DLL1.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --progress-dir=/home/kartaviy/Desktop/studs/programming/5lab/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/DLL1.dir/src/dynamic_lib1/DLL1.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/DLL1.dir/src/dynamic_lib1/DLL1.cpp.o -MF CMakeFiles/DLL1.dir/src/dynamic_lib1/DLL1.cpp.o.d -o CMakeFiles/DLL1.dir/src/dynamic_lib1/DLL1.cpp.o -c /home/kartaviy/Desktop/studs/programming/5lab/src/dynamic_lib1/DLL1.cpp

CMakeFiles/DLL1.dir/src/dynamic_lib1/DLL1.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Preprocessing CXX source to CMakeFiles/DLL1.dir/src/dynamic_lib1/DLL1.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/kartaviy/Desktop/studs/programming/5lab/src/dynamic_lib1/DLL1.cpp > CMakeFiles/DLL1.dir/src/dynamic_lib1/DLL1.cpp.i

CMakeFiles/DLL1.dir/src/dynamic_lib1/DLL1.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green "Compiling CXX source to assembly CMakeFiles/DLL1.dir/src/dynamic_lib1/DLL1.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/kartaviy/Desktop/studs/programming/5lab/src/dynamic_lib1/DLL1.cpp -o CMakeFiles/DLL1.dir/src/dynamic_lib1/DLL1.cpp.s

# Object files for target DLL1
DLL1_OBJECTS = \
"CMakeFiles/DLL1.dir/src/dynamic_lib1/DLL1.cpp.o"

# External object files for target DLL1
DLL1_EXTERNAL_OBJECTS =

libDLL1.so: CMakeFiles/DLL1.dir/src/dynamic_lib1/DLL1.cpp.o
libDLL1.so: CMakeFiles/DLL1.dir/build.make
libDLL1.so: libStaticLib.a
libDLL1.so: CMakeFiles/DLL1.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color "--switch=$(COLOR)" --green --bold --progress-dir=/home/kartaviy/Desktop/studs/programming/5lab/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX shared library libDLL1.so"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/DLL1.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/DLL1.dir/build: libDLL1.so
.PHONY : CMakeFiles/DLL1.dir/build

CMakeFiles/DLL1.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/DLL1.dir/cmake_clean.cmake
.PHONY : CMakeFiles/DLL1.dir/clean

CMakeFiles/DLL1.dir/depend:
	cd /home/kartaviy/Desktop/studs/programming/5lab/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/kartaviy/Desktop/studs/programming/5lab /home/kartaviy/Desktop/studs/programming/5lab /home/kartaviy/Desktop/studs/programming/5lab/build /home/kartaviy/Desktop/studs/programming/5lab/build /home/kartaviy/Desktop/studs/programming/5lab/build/CMakeFiles/DLL1.dir/DependInfo.cmake "--color=$(COLOR)"
.PHONY : CMakeFiles/DLL1.dir/depend

