#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <ctime>
#include <cstdlib>
#include <chrono>

using namespace std;
using namespace std::chrono;

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
            int col_index = getColumnIndex(col_name);
            if (col_index >= 0) {
                indixes[col_name].insert({row[col_index], row_index});
            }
        }
        
        return true;
    }
    
    pair<double, double> measureSearchTime(const string& column, const string& value) {
        int colIndex = getColumnIndex(column);
        if (colIndex == -1) return {0, 0};
        
        // измерение времени без индекса
        auto start1 = high_resolution_clock::now();
        vector<vector<string>> resultWithoutIndex;
        for (const auto& row : data) {
            if (row[colIndex] == value) {
                resultWithoutIndex.push_back(row);
            }
        }
        auto end1 = high_resolution_clock::now();
        double timeWithoutIndex = duration_cast<microseconds>(end1 - start1).count();
        
        // измерение времени с индексом
        double timeWithIndex = 0;
        auto index_it = indixes.find(column);
        if (index_it != indixes.end()) {
            auto start2 = high_resolution_clock::now();
            vector<vector<string>> resultWithIndex;
            const auto& index = index_it->second;
            auto range = index.equal_range(value);
            for (auto it = range.first; it != range.second; ++it) {
                resultWithIndex.push_back(data[it->second]);
            }
            auto end2 = high_resolution_clock::now();
            timeWithIndex = duration_cast<microseconds>(end2 - start2).count();
        }
        
        return {timeWithoutIndex, timeWithIndex};
    }

    void addIndex(const string& column) {
        int colIndex = getColumnIndex(column);
        if (colIndex == -1) return;
        
        if (indixes.find(column) != indixes.end()) return;
        
        multimap<string, size_t> new_index;
        for (size_t i = 0; i < data.size(); ++i) {
            new_index.insert({data[i][colIndex], i});
        }
        
        indixes[column] = new_index;
    }

    void generateRandomData(int count, int variety) {
        srand(time(nullptr));
        for (int i = 0; i < count; ++i) {
            vector<string> row;
            for (size_t j = 0; j < header.size(); ++j) {
                row.push_back(to_string(rand() % variety));
            }
            addData(row);
        }
    }
};

void runExperiment(int rowCount, int valueVariety) {
    vector<string> header = {"A", "B", "C", "D"};
    Table table(header);
    
    table.generateRandomData(rowCount, valueVariety);
    
    string searchValue = to_string(rand() % valueVariety);
    
    auto times1 = table.measureSearchTime("A", searchValue);
    
    table.addIndex("A");
    
    auto times2 = table.measureSearchTime("A", searchValue);
    
    cout << rowCount << "\t" 
         << valueVariety << "\t" 
         << times1.first << "\t" 
         << times2.second << "\t" 
         << times1.first / max(1.0, times2.second) << endl;
}

int main() {
    vector<int> rowCounts = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100,
                            200, 300, 400, 500, 600, 700, 800, 900, 1000,
                            2000, 3000, 4000, 5000, 10000};
    
    vector<int> varieties = {10, 100, 1000};
    
    cout << "Rows\tVariety\tT1 (µs)\tT2 (µs)\tSpeedup" << endl;
    
    for (int variety : varieties) {
        for (int rows : rowCounts) {
            runExperiment(rows, variety);
        }
        cout << "__________" << endl;
    }
    
    return 0;
}