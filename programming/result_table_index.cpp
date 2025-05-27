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
    vector<string> header; //названия колонок
    vector<vector<string>> data; //данные таблицы (колонки и строки) 
    map<string, multimap<string, size_t>> indixes; //индексы (ключ-имя колонки, значение-мультимапа значений и индексов строк)

    /**
     * Получает индекс столбца по его имени
     * @param column Имя столбца
     * @return Индекс столбца или -1 если не найден
     */
    int getColumnIndex(const string& column) const {
        for (size_t i = 0; i < header.size(); ++i)
            if (header[i] == column) return i;
        return -1;
    }

public:
    /**
     * Конструктор таблицы
     * @param header Вектор с именами столбцов
     */
    Table(const vector<string>& header) : header(header) {}
    
    /**
     * Добавляет строку данных в таблицу
     * @param row Вектор значений строки
     * @return true если успешно, false если размер строки не соответствует заголовку
     */
    bool addData(const vector<string>& row) {
        if (row.size() != header.size()) return false;
        
        data.push_back(row);
        size_t row_index = data.size() - 1;
        
        // Обновляем все существующие индексы
        for (auto& index_pair : indixes) {
            const string& col_name = index_pair.first;
            int col_index = getColumnIndex(col_name);
            if (col_index >= 0) indixes[col_name].insert({row[col_index], row_index});
        }
        
        return true;
    }
    
    /**
     * Измеряет время поиска с индексом и без
     * @param column Столбец для поиска
     * @param value Искомое значение
     * @return Пара значений: время без индекса и время с индексом (в микросекундах)
     */
    pair<double, double> measureSearchTime(const string& column, const string& value) {
        int colIndex = getColumnIndex(column);
        if (colIndex == -1) return {0, 0};
        
        // Измерение времени линейного поиска (без индекса)
        auto start1 = high_resolution_clock::now();
        vector<vector<string>> resultWithoutIndex;
        for (const auto& row : data) {
            if (row[colIndex] == value) resultWithoutIndex.push_back(row);
        }
        auto end1 = high_resolution_clock::now();
        double timeWithoutIndex = duration_cast<nanoseconds>(end1 - start1).count();
        
        // Измерение времени поиска по индексу
        double timeWithIndex = 0;
        auto index_it = indixes.find(column);
        if (index_it != indixes.end()) {
            auto start2 = high_resolution_clock::now();
            vector<vector<string>> resultWithIndex;
            const auto& index = index_it->second;
            // Используем equal_range для поиска всех совпадений
            auto range = index.equal_range(value);
            for (auto it = range.first; it != range.second; ++it)
                resultWithIndex.push_back(data[it->second]);
            auto end2 = high_resolution_clock::now();
            timeWithIndex = duration_cast<nanoseconds>(end2 - start2).count();
        }
        
        return {timeWithoutIndex, timeWithIndex};
    }

    /**
     * Создает индекс для указанного столбца
     * @param column Имя столбца для индексации
     */
    void addIndex(const string& column) {
        int colIndex = getColumnIndex(column);
        if (colIndex == -1) return;

        // Если индекс уже существует, ничего не делаем
        if (indixes.find(column) != indixes.end()) return;
        
        // Создаем новый индекс
        multimap<string, size_t> new_index;
        for (size_t i = 0; i < data.size(); ++i)
            new_index.insert({data[i][colIndex], i}); // Заполняем индекс парами (значение, номер строки)
        
        indixes[column] = new_index;
    }

    /**
     * Генерирует случайные данные для таблицы
     * @param count Количество строк для генерации
     * @param variety Количество уникальных значений в данных
     */
    void generateRandomData(int count, int variety) {
        srand(time(nullptr)); // Инициализация генератора случайных чисел
        for (int i = 0; i < count; ++i) {
            vector<string> row;
            // Генерируем случайные значения для каждого столбца
            for (size_t j = 0; j < header.size(); ++j)
                row.push_back(to_string(rand() % variety));
            addData(row); // Добавляем сгенерированную строку
        }
    }
};

/**
 * Функция для проведения одного эксперимента
 * @param rowCount Количество строк в таблице
 * @param valueVariety Количество уникальных значений
 */
void runExperiment(int rowCount, int valueVariety) {
    vector<string> header = {"A", "B", "C", "D"};
    Table table(header);
    
    // Заполняем таблицу случайными данными
    table.generateRandomData(rowCount, valueVariety);
    
    // Выбираем случайное значение для поиска
    string searchValue = to_string(rand() % valueVariety);
    
    // Измеряем время поиска без индекса
    auto times1 = table.measureSearchTime("A", searchValue);
    
    table.addIndex("A");
    
    // Измеряем время поиска с индексом
    auto times2 = table.measureSearchTime("A", searchValue);
    
    cout << rowCount << "\t" 
         << valueVariety << "\t" 
         << times1.first
          << "\t" 
         << times2.second << "\t" 
         << times1.first / max(1.0, times2.second) << endl;
}

int main() {
    vector<int> rowCounts = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100,
                            200, 300, 400, 500, 600, 700, 800, 900, 1000,
                            2000, 3000, 4000, 5000, 10000, 10000};
    
    // Различные уровни разнообразия данных
    vector<int> varieties = {10, 100, 1000};
    
    cout << "Rows\tVariety\tT1 (µs)\tT2 (µs)\tSpeedup" << endl;
    
    for (int variety : varieties) {
        for (int rows : rowCounts)
            runExperiment(rows, variety);
        cout << "__________" << endl;
    }
    
    return 0;
}