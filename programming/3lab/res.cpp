#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <unordered_map>
#include <algorithm>
#include <chrono>
#include <cstdlib>
#include <iomanip>
#include <fstream>
#include <random>

using namespace std;
using namespace std::chrono;

class Table {
private:
    vector<string> header;
    vector<vector<string>> data;
    unordered_map<string, multimap<string, int>> indexes;

public:
    Table(const vector<string>& header) : header(header) {}

    void addRow(const vector<string>& row) {
        if (row.size() != header.size()) {
            cout << "Error: column count mismatch" << endl;
            return;
        }
        data.push_back(row);

        int rowIndex = data.size() - 1;
        for (auto& index : indexes) {
            string colName = index.first;
            int colIndex = getColumnIndex(colName);
            if (colIndex != -1) {
                index.second.insert({ row[colIndex], rowIndex });
            }
        }
    }

    int getColumnIndex(const string& column) {
        auto it = find(header.begin(), header.end(), column);
        if (it == header.end()) {
            cout << "Error: column not found" << endl;
            return -1;
        }
        return distance(header.begin(), it);
    }

    void createIndex(const string& column) {
        int colIndex = getColumnIndex(column);
        if (colIndex == -1) return;

        multimap<string, int> newIndex;
        for (int i = 0; i < data.size(); ++i) {
            newIndex.insert({ data[i][colIndex], i });
        }
        indexes[column] = newIndex;
    }

    pair<double, double> searchWithTiming(const string& column, const string& value) {
    int colIndex = getColumnIndex(column);
    if (colIndex == -1) return make_pair(0, 0);

    for (int i = 0; i < 3; ++i) {
        for (const auto& row : data) {
            if (row[colIndex] == value) {}
        }
    }

    double timeNoIndex = 0;
    for (int i = 0; i < 10; ++i) {
        auto start = high_resolution_clock::now();
        
        volatile int count = 0;
        for (const auto& row : data) {
            if (row[colIndex] == value) count++;
        }
        
        auto end = high_resolution_clock::now();
        timeNoIndex += duration_cast<nanoseconds>(end - start).count();
    }

    double timeWithIndex = 0;
    if (indexes.count(column)) {
        for (int i = 0; i < 3; ++i) {
            auto range = indexes[column].equal_range(value);
            for (auto it = range.first; it != range.second; ++it) {}
        }

        for (int i = 0; i < 10; ++i) {
            auto start = high_resolution_clock::now();
            
            volatile int count = 0;
            auto range = indexes[column].equal_range(value);
            for (auto it = range.first; it != range.second; ++it) {
                count++;
            }
            
            auto end = high_resolution_clock::now();
            timeWithIndex += duration_cast<nanoseconds>(end - start).count();
        }
    }

    return make_pair(timeNoIndex / 10 / 1e9, timeWithIndex / 10 / 1e9);
}

    int rowCount() const { return data.size(); }
};

class Database {
private:
    map<string, Table*> tables;

public:
    void createTable(const string& name, const vector<string>& columns) {
        tables[name] = new Table(columns);
    }

    Table* getTable(const string& name) {
        if (tables.count(name)) {
            return tables[name];
        }
        cout << "Error: table not found" << endl;
        return nullptr;
    }

    ~Database() {
        for (auto& table : tables) {
            delete table.second;
        }
    }
};

vector<string> generateRandomValues(int count, int maxValue) {
    vector<string> result;
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dist(0, maxValue - 1);

    for (int i = 0; i < count; ++i) {
        result.push_back(to_string(dist(gen)));
    }
    return result;
}

void runExperiment(int rows, int variety, ofstream& resultsFile) {
    Database db;
    db.createTable("Test", { "ID", "Value" });
    Table* table = db.getTable("Test");

    auto values = generateRandomValues(rows, variety);
    for (int i = 0; i < rows; ++i) {
        table->addRow({ to_string(i), values[i] });
    }

    table->createIndex("Value");

    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dist(0, variety - 1);
    string searchValue = to_string(dist(gen));

    auto times = table->searchWithTiming("Value", searchValue);

    resultsFile << rows << ","
        << variety << ","
        << fixed << setprecision(9) << times.first << ","
        << times.second << ","
        << setprecision(2) << (times.first / times.second) << endl;

    cout << "| " << setw(12) << rows
        << " | " << setw(12) << variety
        << " | " << setw(18) << fixed << setprecision(9) << times.first
        << " | " << setw(18) << times.second
        << " | " << setw(12) << setprecision(2) << (times.first / times.second)
        << " |" << endl;
}

int main() {
    ofstream resultsFile("results.csv");
    resultsFile << "Rows,Variety,TimeNoIndex,TimeWithIndex,Speedup\n";

    cout << "| Rows Count   | Val Variety  | T1 (s)  | T2 (s)  | Speedup (x)  |" << endl;
    cout << "+--------------+--------------+--------------------+--------------------+--------------+" << endl;

    vector<int> testRows = { 10, 20, 30, 40, 50, 60, 70, 80, 90, 100,
                          200, 300, 400, 500, 600, 700, 800, 900, 1000,
                          2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000 };

    vector<int> testVarieties = { 10, 100, 1000 };

    for (int variety : testVarieties) {
        for (int rows : testRows) {
            runExperiment(rows, variety, resultsFile);
        }
    }

    resultsFile.close();
    cout << "\nResults saved to results.csv" << endl;

    system("python3 pfi.py -f results.csv");

    return 0;
}