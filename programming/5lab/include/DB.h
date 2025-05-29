#ifndef DB_H
#define DB_H

#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <iomanip>

class Table {
private:
    std::vector<std::string> header;
    std::vector<std::vector<std::string>> data;
    std::map<std::string, std::multimap<std::string, size_t>> indices;

    int getColumnIndex(const std::string& column) const;

public:
    Table(const std::vector<std::string>& header);
    bool addData(const std::vector<std::string>& row);
    Table* select(const std::string& column, const std::string& value) const;
    void addIndex(const std::string& column);
    void print() const;
};

class DB {
private:
    std::map<std::string, Table*> tables;
public:
    bool addTable(const std::string& name, const std::vector<std::string> header);
    Table* getTable(const std::string& name);
    ~DB();
};

#endif