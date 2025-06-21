/*
заполнить дек случ. значениями, 
отсортировать его по возрастанию и по убыванию через мульти мэп
*/

#include <iostream>
#include <deque>
#include <map>
#include <cstdlib>
#include <ctime>
#include <algorithm>

using namespace std;

int main() {
    srand(time(0));

    // заполнение дека случайными числами
    deque<int> d(10); // дек из 10 элементов
    generate(d.begin(), d.end(), 
        []() { return rand() % 100 + 1; }
    );

    for (int num : d) {
        cout << num << " ";
    }
    cout << "\n\n";

    // сортировка по возрастанию с использованием multimap
    multimap<int, int> asc_map;
    for (int num : d) {
        asc_map.insert({num, num});
    }

    cout << "По возрастанию: ";
    for (const auto& pair : asc_map) {
        cout << pair.first << " ";
    }
    cout << "\n";

    // cортировка по убыванию с использованием multimap
    multimap<int, int, greater<int>> desc_map;
    for (int num : d) {
        desc_map.insert({num, num});
    }    multimap<int, int, greater<int>> desc_map;
    for (int num : d) {
        desc_map.insert({num, num});
    }

    cout << "По убыванию:    ";
    for (const auto& pair : desc_map) {
        cout << pair.first << " ";
    }
    cout << "\n";

    return 0;
}