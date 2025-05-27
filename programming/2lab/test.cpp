#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <iomanip>
#include <chrono>
#include <fstream>
#include <cstdlib>
#include <ctime>
#include <random>

using namespace std;
using namespace std::chrono;

/*
хранение данные и индексы
сначала проверяет индекс таблицы, если индекс есть - используется equal_range для быстрого поиска
если нет, то выполняется линейный поиск
индексы автоматически обновляются при добавлении новых данных
*/
class Table {
private:
    vector<string> header; //названия колонок
    vector<vector<string>> data; //данные таблицы (колонки и строки) 
    map<string, multimap<string, size_t>> indixes; //индексы (ключ-имя колонки, значение-мультимапа значений и индексов строк)

    /*
    возвращение индекса колонки по имени
    передаваемый параметр: column -имя искомой колонки
    int idx = getColumnIndex("C"); вернет '2'
    */
    int getColumnIndex(const string& column) const {
        for (size_t i = 0; i < header.size(); ++i)
            if (header[i] == column) return i;
        return -1;
    }

public:
    //конструктор 
    Table(const vector<string>& header) : header(header) {}
    
    /*
    добавление новую строку в таблицу
    передаваемые параметры: row -вектор значений
    вернет true, если размер строки соответствует заголовку, иначе false
    */
    bool addData(const vector<string>& row) {
        if (row.size() != header.size()) return false;
        
        data.push_back(row);
        size_t row_index = data.size() - 1;
    
        for (auto& index_pair : indixes) {
            const string& col_name = index_pair.first;
            int col_index = getColumnIndex(col_name);
            if (col_index >= 0) indixes[col_name].insert({row[col_index], row_index});
        }
        
        return true;
    }
    
    /*
    поиск строк по значению в указанной колонке
    если есть индекс для колонки - использует его для быстрого поиска, если индекса нет - выполняет линейный поиск
    передаваемые параметры: column -колонка для поиска, value -значение колонки
    возвращает указатель на новую таблицу
    */
    Table* select(const string& column, const string& value) const {
        int colIndex = getColumnIndex(column);
        if (colIndex == -1) return new Table(header);
        
        Table* resultTable = new Table(header);
        
        auto index_it = indixes.find(column);
        if (index_it != indixes.end()) {
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

    /*
    создание индекса для указанной колонки
    проверяет существование колонки. если индекс существует - выходит, также создает новый индекс(мультимапу) для всех значений в колонке
    передаваемые параметры: column -имя для индексации
    */
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

    size_t size() const {
        return data.size();
    }
};

//управление коллекцией таблиц
class DB {
private:
    map<string, Table*> tables; //мапа для таблиц (ключ-имя таблицы, значение-указатель на Table)
public:
    /*
    создание новой таблицы
    передаваемые параметры: name -имя таблицы, header -заголовок колонок
    вернет false, если таблица существует, иначе true
    */
    bool addTable(const string& name, const vector<string> header) {
        if (tables.find(name) != tables.end()) return false;
        tables[name] = new Table(header);
        return true;
    }
    /*
    возвращение таблицы по имени
    передаваемые параметры: name -имя таблицы
    возвращает указатель на Table или nullptr
    */
    Table* getTable(const string& name) {
        auto it = tables.find(name);
        if (it == tables.end()) return nullptr;
        return it->second;
    }
    
    /*
    деструктор
    удаляет все объекты Table, созданные через new
    */
    ~DB() {
        for (auto& pair : tables)
            delete pair.second;
    }
};

// Генерация случайных данных
vector<vector<string>> generateRandomData(size_t rows, size_t cols, size_t variety) {
    vector<vector<string>> data;
    data.reserve(rows);

    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(0, variety - 1);

    for (size_t i = 0; i < rows; ++i) {
        vector<string> row;
        row.reserve(cols);
        for (size_t j = 0; j < cols; ++j) {
            row.push_back("V" + to_string(dis(gen)));
        }
        data.push_back(row);
    }

    return data;
}

// Измерение времени поиска
pair<double, double> measureSearchTime(Table* table, const string& column, const string& value) {
    // Поиск без индекса
    auto start1 = high_resolution_clock::now();
    Table* result1 = table->select(column, value);
    auto end1 = high_resolution_clock::now();
    delete result1;
    double timeWithoutIndex = duration<double, nano>(end1 - start1).count() / 1'000'000.0;

    // Добавляем индекс
    table->addIndex(column);

    // Поиск с индексом
    auto start2 = high_resolution_clock::now();
    Table* result2 = table->select(column, value);
    auto end2 = high_resolution_clock::now();
    delete result2;
    double timeWithIndex = duration_cast<nanoseconds>(end2 - start2).count();

    return {timeWithoutIndex, timeWithIndex};
}

int main() {
    ofstream outFile("results.csv");
    outFile << "Rows,Variety,TimeWithoutIndex,TimeWithIndex,Speedup\n";

    vector<size_t> row_counts = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 
                                200, 300, 400, 500, 600, 700, 800, 900, 1000};
    vector<size_t> varieties = {10, 100, 1000};

    const string column = "D";
    const string value = "V5"; // Будем искать это значение

    for (size_t variety : varieties) {
        for (size_t rows : row_counts) {
            DB db;
            vector<string> header = {"A", "B", "C", "D"};
            db.addTable("Test", header);

            // Генерируем случайные данные
            auto randomData = generateRandomData(rows, header.size(), variety);
            Table* table = db.getTable("Test");
            for (const auto& row : randomData) {
                table->addData(row);
            }

            // Измеряем время поиска
            auto [timeWithoutIndex, timeWithIndex] = measureSearchTime(table, column, value);
            double speedup = timeWithoutIndex / timeWithIndex;

            // Записываем результаты
            outFile << rows << "," << variety << "," 
                   << fixed << setprecision(9) << timeWithoutIndex << "," 
                   << fixed << setprecision(9) << timeWithIndex << "," 
                   << fixed << setprecision(2) << speedup << "\n";

            cout << "Rows: " << rows << ", Variety: " << variety 
                 << ", Time without index: " << scientific << timeWithoutIndex 
                 << ", Time with index: " << timeWithIndex 
                 << ", Speedup: " << fixed << speedup << "x\n";
        }
    }

    outFile.close();
    cout << "Results saved to results.csv\n";

    return 0;
}