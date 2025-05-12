#include <iostream>
#include <string>
#include <vector>
#include <iomanip>
#include <algorithm>
#include <map>

using namespace std;

class Table {
private:
    vector<vector<string>> data;
    vector<string> header;
    u_int8_t getIndex(const string& column)const {
        for (u_int8_t it = 0; it <= header.size(); ++it)
            if (header[it] == column) return it;
        return -1; 
    }
public:
    Table(const vector<string>& header) : header(header){}
    // Добавить данные в таблицу
    void addData(const vector<string>& row) {
        if (row.size() == header.size()) data.push_back(row); 
    }
    // Получение новой таблицы с результатами запроса.
    // Выбрать все строки в которых в столбце column стоит значение value
    Table* select(const string& column, const string& value)const {
        u_int8_t cIndex = getIndex(column);
        if (column[cIndex] == -1) return nullptr;
        Table* resultTable = new Table(header);
        for (const auto& row : data)
            if (row[cIndex] == value) resultTable->addData(row);
        return resultTable;
    }
    Table* addIndex(const string& column)const {

    }
    // Вывести таблицу на экран
    void print()const {
        for (const auto& hName : header)
            cout << setw(5) << hName;
        cout << endl;
        for (const auto& row : data) {
            for (const auto& cell : row)
                cout << setw(5) << cell;
            cout << endl;
        }
    }
};

class DB {
private:
    map<string, Table*> tables;
public:
    // Добавить таблицу
    void addTable(const string& name, const vector<string> header) {
        if (tables.find(name) == tables.end()) tables[name] = new Table(header);
    }
    // Получить таблицу
    Table* getTable(const string& name) {
        auto it = tables.find(name);
        if (it == tables.end()) return nullptr;
        return it->second;
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
    if (result_2) result_2->print();
    delete result_2;
    // // Пример вывода
    // // D    E   F
    // // D1   E1  F1

    // Построение индекса для столбца D
    t2->addIndex("D");
    // Выбор данных
    Table* result_2 = t2->select("D", "D1");
    result_2->print();

    // Добавление данных. Индекс должен обновиться
    data.clear();
    data.push_back("D1");
    data.push_back("E3");
    data.push_back("F3");
    t2->addData(data); // Добавление данных

    // Выбор данных. В ответе должна появиться новая строка.
    Table* result_3 = t2->select("D", "D1");
    result_3->print();
    

    return 0;
}