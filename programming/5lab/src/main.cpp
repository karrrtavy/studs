#include <iostream>
#include <vector>
#include <string>
#include <dlfcn.h>
#include "DB.h"
#include "DLL1.h"

typedef void (*FillTableFunc)(Table*, const std::vector<std::string>&, int);

int main() {
    DB db;
    std::vector<std::string> header {"ID", "Name", "Value"};
    db.addTable("TestTable", header);
    Table* table = db.getTable("TestTable");
    
    // 1. Заполнение таблицы напрямую
    table->addData({"ID1", "Name1", "Value1"});
    table->addData({"ID2", "Name2", "Value2"});
    
    // 2. Заполнение через динамическую библиотеку (неявное связывание)
    fillTableRandom(table, header);
    
    // 3. Заполнение через динамическую библиотеку (явное связывание)
    void* handle = dlopen("./libDLL2.so", RTLD_LAZY);
    if (!handle) {
        std::cerr << "Cannot load library: " << dlerror() << std::endl;
        return 1;
    }
    
    FillTableFunc fillFunc = (FillTableFunc)dlsym(handle, "fillTableSequential");
    if (!fillFunc) {
        std::cerr << "Cannot load symbol: " << dlerror() << std::endl;
        return 1;
    }
    
    fillFunc(table, header, 10);
    
    // Вывод результатов
    std::cout << "All data:" << std::endl;
    table->print();
    
    // Создание индекса и поиск
    table->addIndex("ID");
    std::cout << "\nSelected data (ID=ID1):" << std::endl;
    Table* selected = table->select("ID", "ID1");
    if (selected) {
        selected->print();
        delete selected;
    }
    
    dlclose(handle);
    return 0;
}