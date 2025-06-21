/*
Написать 4 функции max min sum avg, 
параметры передаются через список инициализации
*/

#include <iostream>
#include <initializer_list>
#include <numeric> // для std::accumulate
#include <climits> // для INT_MIN и INT_MAX
#include <stdexcept> // для std::invalid_argument

using namespace std;

// Функция для нахождения максимального значения
int max(std::initializer_list<int> list) {
    if (list.size() == 0) {
        throw std::invalid_argument("Empty list in max()");
    }
    int max_val = INT_MIN;
    for (int num : list) {
        if (num > max_val) {
            max_val = num;
        }
    }
    return max_val;
}

// Функция для нахождения минимального значения
int min(std::initializer_list<int> list) {
    if (list.size() == 0) {
        throw std::invalid_argument("Empty list in min()");
    }
    int min_val = INT_MAX;
    for (int num : list) {
        if (num < min_val) {
            min_val = num;
        }
    }
    return min_val;
}

// Функция для вычисления суммы всех элементов
int sum(std::initializer_list<int> list) {
    return std::accumulate(list.begin(), list.end(), 0);
}

// Функция для вычисления среднего значения
double avg(std::initializer_list<int> list) {
    if (list.size() == 0) {
        throw std::invalid_argument("Empty list in avg()");
    }
    double total = std::accumulate(list.begin(), list.end(), 0.0);
    return total / list.size();
}

int main() {
    // Примеры использования функций
    std::cout << "max: " << max({1, 5, 3, 9, 2}) << std::endl;
    std::cout << "min: " << min({1, 5, 3, 9, 2}) << std::endl;
    std::cout << "sum: " << sum({1, 5, 3, 9, 2}) << std::endl;
    std::cout << "avg: " << avg({1, 5, 3, 9, 2}) << std::endl;

    return 0;
}