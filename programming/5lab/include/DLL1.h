#ifndef DLL1_H
#define DLL1_H

#include "DB.h"
#include <vector>
#include <string>

__attribute__((visibility("default")))
void fillTableRandom(Table* table, const std::vector<std::string>& columns);

#endif