#include <iostream>
#include "StaticLib/SLMain.h"
#include "DLL_1/DLL_1_Main.h"

int main() {
    std::cout << "Hello\n";
    SL_Hello();
    DLL_1_Hello();
    return 0;
}