#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <iomanip>

using namespace std;

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
            // index_pair.first - указывает на КЛЮЧ мапы индексов, в данном случае названия столбцов
            int col_index = getColumnIndex(col_name);
            if (col_index >= 0) indixes[col_name].insert({row[col_index], row_index});
            //эквивалентно indixes[col_name].insert(std::make_pair(row[col_index], row_index));
            //или indixes[col_name].insert(pair<string, size_t>(row[col_index], row_index));
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
            // it->second - указывает на ЗНАЧЕНИЕ mapы indixes, в данном случае значение column - его строк
            auto range = index.equal_range(value);  
            // equal_range - алгоритм, находит поддиапазон в диапазоне, в котором все элементы эквивалентны заданному значению
            /*
            при первом поиске: возвращает диапазон для всех пар с ключом D1, затем находит две пары D1 как 0 и 3
            */
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