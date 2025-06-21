/*
Заполнить вектор случайный 
числами отсортировать его по возрастанию и убыванию с помощью multiset
*/

#include <iostream>
#include <vector>
#include <set>       // для multiset
#include <ctime>     // для time()
#include <cstdlib>   // для rand() и srand()
#include <algorithm> // для copy()

int main() {
    // Инициализация генератора случайных чисел
    std::srand(std::time(0));

    // Создаем вектор и заполняем его случайными числами (например, 10 чисел от 1 до 100)
    std::vector<int> vec;
    for (int i = 0; i < 10; ++i) {
        vec.push_back(1 + std::rand() % 100);
    }

    // Выводим исходный вектор
    std::cout << "Исходный вектор: ";
    for (int num : vec) {
        std::cout << num << " ";
    }
    std::cout << "\n";

    // Сортировка по возрастанию с помощью multiset
    std::multiset<int> ascending_set(vec.begin(), vec.end());
    std::vector<int> ascending_vec(ascending_set.begin(), ascending_set.end());

    // Выводим вектор, отсортированный по возрастанию
    std::cout << "По возрастанию:  ";
    for (int num : ascending_vec) {
        std::cout << num << " ";
    }
    std::cout << "\n";

    // Сортировка по убыванию с помощью multiset (с использованием std::greater)
    std::multiset<int, std::greater<int>> descending_set(vec.begin(), vec.end());
    std::vector<int> descending_vec(descending_set.begin(), descending_set.end());

    // Выводим вектор, отсортированный по убыванию
    std::cout << "По убыванию:     ";
    for (int num : descending_vec) {
        std::cout << num << " ";
    }
    std::cout << "\n";

    return 0;
}