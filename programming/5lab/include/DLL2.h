#ifndef DLL2_H
#define DLL2_H

#include "DB.h"
#include <vector>
#include <string>

extern "C" {
    __attribute__((visibility("default")))
    void fillTableSequential(Table* table, const std::vector<std::string>& columns, int start);
}

#endif