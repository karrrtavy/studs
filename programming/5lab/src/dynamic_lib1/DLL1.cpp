#include "../../include/DLL1.h"
#include <random>
#include <ctime>

void fillTableRandom(Table* table, const std::vector<std::string>& columns) {
    std::srand(std::time(0));
    
    for (int i = 0; i < 5; ++i) {
        std::vector<std::string> row;
        for (const auto& col : columns) {
            int value = 1 + (std::rand() % 100);
            row.push_back(col + std::to_string(value));
        }
        table->addData(row);
    }
}