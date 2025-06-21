/*
Задача:
заполнить дек случайными числами, отсортировать по возрастанию и убыванию с помощью map
*/

#include <iostream>
#include <deque>
#include <map>
#include <ctime>
#include <cstdlib>
#include <algorithm>

int main() {
    // Инициализация генератора случайных чисел
    std::srand(std::time(nullptr));

    // 1. Создаем и заполняем deque случайными числами
    std::deque<int> dq(10);
    std::generate(dq.begin(), dq.end(), []() { return std::rand() % 100; });

    // 2. Выводим исходный deque
    std::cout << "Исходный deque:\t";
    for (int n : dq) std::cout << n << " ";
    std::cout << "\n";

    // 3. Сортировка по возрастанию с помощью map
    std::map<int, int> asc_map;
    for (int n : dq) asc_map[n]++;  // ключи в map автоматически сортируются
    
    std::cout << "По возрастанию:\t";
    for (auto& [key, val] : asc_map)
        for (int i = 0; i < val; ++i)
            std::cout << key << " ";
    std::cout << "\n";

    // 4. Сортировка по убыванию с помощью multimap
    std::multimap<int, int, std::greater<int>> desc_map;
    for (int n : dq) desc_map.insert({n, 0});
    
    std::cout << "По убыванию:\t";
    for (auto& [key, val] : desc_map)
        std::cout << key << " ";
    std::cout << "\n";

    return 0;
}