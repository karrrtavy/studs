#include <iostream>
#include <string>
#include <vector>
#include <string>
#include <map>
#include <iomanip>

using namespace std;

class Table {
private:
    vector<string> header;
    vector<vector<string>> data;
    map<string, multimap<string, vector<string>>> mmTable;
    int getColumnIndex(const string& column) const {
        for (size_t i = 0; i < header.size(); ++i)
            if (header[i] == column) return i;
        return -1;
    }
    void updateIndex(const string& column, const vector<string>& row) {
        auto it = mmTable.find(column);
        if (it != mmTable.end()) {
            int colIndex = getColumnIndex(column);
            if (colIndex != -1) {
                it->second.insert({row[colIndex], row});
            }
        }
    }
public:
    Table(const vector<string>& header) : header(header) {}
    bool addData(const vector<string>& row) {
        if (row.size() != header.size()) return false;
        data.push_back(row);
        return true;
    }
    Table* select(const string& column, const string& value) const {
        int colIndex = getColumnIndex(column);
        Table* resultTable = new Table(header);
        auto it = mmTable.find(column);
        if (it != mmTable.end()) {
            auto range = it->second.equal_range(value);
            for (auto i = range.first; i != range.second; ++i) 
                resultTable->addData(i->second);
        }
        else {
            for (const auto& row : data) 
                if (row[colIndex] == value) resultTable->addData(row);
        }
        return resultTable;
    }
    void print() const {
        for (const auto& colName : header)
            cout << setw(5) << colName << " ";
        cout << "\n";
        for (const auto& row : data) {
            for (const auto& cell : row)
                cout << setw(5) << cell << " ";
            cout << "\n";
        }
    }
    Table* addIndex(const string& column) {
        int colIndex = getColumnIndex(column);
        multimap<string, vector<string>> indexTable;
        for (const auto& row : data)
            indexTable.insert({row[colIndex], row});
        mmTable[column] = indexTable;
    }
};

class DB {
private:
    map<string, Table*> tables;
public:
    bool addTable(const string& name, const vector<string> header) {
        if (tables.find(name) != tables.end()) return false;
        tables[name] = new Table(header);
        return true;
    }
    Table* getTable(const string& name) {
        auto it = tables.find(name);
        if (it == tables.end()) return nullptr;
        return it -> second;
    }
};

int main() {
    DB db;

    // Добавление таблицы. Вариант 1. На основе std::initalizer_list
    vector<string> header_1 {"A", "B", "C"};
    db.addTable("T_1", header_1);
    
    Table* t1 = db.getTable("T_1");
    t1->addData({"A1", "B1", "C1"}); // Добавление данных
    t1->addData({"A2", "B2", "C2"}); // Добавление данных
    t1->addData({"A3", "B3", "C3"}); // Добавление данных
    t1->addData({"A1", "B10", "C10"}); // Добавление данных
    // Выбор данных
    Table* result_1 = t1->select("A", "A1"); 
    result_1->print();
    delete result_1;
    // Пример вывода
    // A    B   C
    // A1   B1  C1
    // A1   B10 C10
    
    // Добавление таблицы. Вариант 2. На основе std::vector
    vector<string> header_2;
    header_2.push_back("D");
    header_2.push_back("E");
    header_2.push_back("F");
    db.addTable("T_2", header_2);
    
    Table* t2 = db.getTable("T_2");
    vector<string> data;
    
    data.push_back("D1");
    data.push_back("E1");
    data.push_back("F1");
    t2->addData(data); // Добавление данных
    
    data.clear();
    data.push_back("D2");
    data.push_back("E2");
    data.push_back("F2");
    t2->addData(data); // Добавление данных
    
    // Выбор данных
    Table* result_2 = t2->select("D", "D1");
    result_2->print();
    delete result_2;
    // // Пример вывода
    // // D    E   F
    // // D1   E1  F1

    // Построение индекса для столбца D
    t2->addIndex("D");
    // Выбор данных
    Table* result_2 = t2->select("D", "D1");
    result_2->print();
    delete result_2;
    // Добавление данных. Индекс должен обновиться
    data.clear();
    data.push_back("D1");
    data.push_back("E3");
    data.push_back("F3");
    t2->addData(data); // Добавление данных

    // Выбор данных. В ответе должна появиться новая строка.
    Table* result_3 = t2->select("D", "D1");
    result_3->print();
    delete result_3;

    return 0;
}