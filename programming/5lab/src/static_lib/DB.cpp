#include "../../include/DB.h"

Table::Table(const std::vector<std::string>& header) : header(header) {}

bool Table::addData(const std::vector<std::string>& row) {
    if (row.size() != header.size()) return false;
    
    data.push_back(row);
    size_t row_index = data.size() - 1;

    for (auto& index_pair : indices) {
        const std::string& col_name = index_pair.first;
        int col_index = getColumnIndex(col_name);
        if (col_index >= 0) indices[col_name].insert({row[col_index], row_index});
    }
    
    return true;
}

int Table::getColumnIndex(const std::string& column) const {
    for (size_t i = 0; i < header.size(); ++i)
        if (header[i] == column) return i;
    return -1;
}

Table* Table::select(const std::string& column, const std::string& value) const {
    int colIndex = getColumnIndex(column);
    if (colIndex == -1) return new Table(header);
    
    Table* resultTable = new Table(header);
    
    auto index_it = indices.find(column);
    if (index_it != indices.end()) {
        const auto& index = index_it->second;
        auto range = index.equal_range(value);
        for (auto it = range.first; it != range.second; ++it)
            resultTable->addData(data[it->second]);
    } else {
        for (const auto& row : data)
            if (row[colIndex] == value) resultTable->addData(row);
    }
    
    return resultTable;
}

void Table::addIndex(const std::string& column) {
    int colIndex = getColumnIndex(column);
    if (colIndex == -1) return;
    
    if (indices.find(column) != indices.end()) return;
    
    std::multimap<std::string, size_t> new_index;
    for (size_t i = 0; i < data.size(); ++i)
        new_index.insert({data[i][colIndex], i});
    
    indices[column] = new_index;
}

void Table::print() const {
    for (const auto& colName : header)
        std::cout << std::setw(5) << colName << " ";
    std::cout << "\n";
    for (const auto& row : data) {
        for (const auto& cell : row)
            std::cout << std::setw(5) << cell << " ";
        std::cout << "\n";
    }
}

bool DB::addTable(const std::string& name, const std::vector<std::string> header) {
    if (tables.find(name) != tables.end()) return false;
    tables[name] = new Table(header);
    return true;
}

Table* DB::getTable(const std::string& name) {
    auto it = tables.find(name);
    return it == tables.end() ? nullptr : it->second;
}

DB::~DB() {
    for (auto& pair : tables)
        delete pair.second;
}