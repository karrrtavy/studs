#include "../../include/DLL2.h"

extern "C" {
    void fillTableSequential(Table* table, const std::vector<std::string>& columns, int start) {
        for (int i = 0; i < 5; ++i) {
            std::vector<std::string> row;
            for (const auto& col : columns) {
                row.push_back(col + std::to_string(start + i));
            }
            table->addData(row);
        }
    }
}