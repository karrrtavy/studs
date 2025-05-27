CXX = g++
CXXFLAGS = -std=c++11 -Wall -I.
LDFLAGS = -LStaticLib -LDL_L1 -Wl,-rpath=.

all: TestApp

# Статическая библиотека
StaticLib/libSL.a: StaticLib/SLMain.o
	ar rcs StaticLib/libSL.a StaticLib/SLMain.o

StaticLib/SLMain.o: StaticLib/SLMain.cpp StaticLib/SLMain.h
	$(CXX) $(CXXFLAGS) -c StaticLib/SLMain.cpp -o StaticLib/SLMain.o

# Динамическая библиотека
DLL_1/libDL_1.so: DLL_1/DLL_1_Main.o
	$(CXX) -shared -o DLL_1/libDL_1.so DLL_1/DLL_1_Main.o

DLL_1/DLL_1_Main.o: DLL_1/DLL_1_Main.cpp DLL_1/DLL_1_Main.h
	$(CXX) $(CXXFLAGS) -fPIC -c DLL_1/DLL_1_Main.cpp -o DLL_1/DLL_1_Main.o

# Основная программа
TestApp: main.cpp StaticLib/libSL.a DLL_1/libDL_1.so
	$(CXX) $(CXXFLAGS) main.cpp -LStaticLib -lSL -LDLL_1 -lDL_1 -o TestApp $(LDFLAGS)

clean:
	rm -f TestApp StaticLib/*.o StaticLib/*.a DLL_1/*.o DLL_1/*.so

.PHONY: all clean