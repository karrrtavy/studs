#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <iomanip>

using namespace std;

class Table {
private:
    vector<string> header;
    vector<vector<string>> data;
    map<string, multimap<string, size_t>> indixes;

    int getColumnIndex(const string& column) const {
        for (size_t i = 0; i < header.size(); ++i)
            if (header[i] == column) return i;
        return -1;
    }

public:
    Table(const vector<string>& header) : header(header) {}
    
    bool addData(const vector<string>& row) {
        if (row.size() != header.size()) return false;
        
        data.push_back(row);
        size_t row_index = data.size() - 1;
    
        for (auto& index_pair : indixes) {
            const string& col_name = index_pair.first;
            //index_pair.first - указывает на КЛЮЧ мапы индексов, в данном случае названия столбцов
            int col_index = getColumnIndex(col_name);
            if (col_index >= 0) indixes[col_name].insert({row[col_index], row_index});
        }
        
        return true;
    }
    
    Table* select(const string& column, const string& value) const {
        int colIndex = getColumnIndex(column);
        if (colIndex == -1) return new Table(header);
        
        Table* resultTable = new Table(header);
        
        auto index_it = indixes.find(column);
        if (index_it != indixes.end()) {
            const auto& index = index_it->second;
            // it->second - указывает на ЗНАЧЕНИЕ mapы indixes, в данном случае значение column (A, B, C, D)
            auto range = index.equal_range(value);  
            // equal_range - алгоритм, находит поддиапазон в диапазоне, в котором все элементы эквивалентны заданному значению
            /*
            при первом поиске: возвращает диапазон для всех пар с ключом D1, затем находит две пары D1 как 0 и 3
            при повторном поиске: возвращает три пары - 0, 3 и 4
            */
            for (auto it = range.first; it != range.second; ++it)
                resultTable->addData(data[it->second]);
        } else {
            for (const auto& row : data)
                if (row[colIndex] == value) resultTable->addData(row);
        }
        
        return resultTable;
    }

    void addIndex(const string& column) {
        int colIndex = getColumnIndex(column);
        if (colIndex == -1) return;
        
        if (indixes.find(column) != indixes.end()) return;
        
        multimap<string, size_t> new_index;
        for (size_t i = 0; i < data.size(); ++i)
            new_index.insert({data[i][colIndex], i});
        
        indixes[column] = new_index;
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
        return it->second;
    }
    
    ~DB() {
        for (auto& pair : tables)
            delete pair.second;
    }
};

int main() {
    DB db;

    vector<string> header_1 {"A", "B", "C", "D"};
    db.addTable("T_1", header_1);
    
    Table* t1 = db.getTable("T_1");
    t1->addData({"A1", "B1", "C1", "D1"});
    t1->addData({"A2", "B2", "C2", "D2"});
    t1->addData({"A3", "B3", "C3", "D3"});
    t1->addData({"A1", "B10", "C10", "D1"});
    
    t1->addIndex("D");
    
    Table* result_1 = t1->select("D", "D1"); 
    result_1->print();
    delete result_1;
    
    t1->addData({"D1", "E3", "F3", "D1"});

    Table* result_2 = t1->select("D", "D1");
    result_2->print();
    delete result_2;

    return 0;
}