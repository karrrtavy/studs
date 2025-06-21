/*
Заполнить вектор рандомными числами с помощью for по коллекции, 
найти макс, минимум и среднее значение элементов
*/

#include <iostream>
#include <vector>
#include <cstdlib> // для rand() и srand()
#include <ctime>   // для time()
#include <numeric>  // для accumulate()

int main() {
    // Инициализация генератора случайных чисел
    std::srand(std::time(nullptr));

    // Создаем вектор из 10 элементов
    std::vector<int> vec(10);

    // Заполняем вектор случайными числами от 1 до 100 с помощью range-based for
    for (int& num : vec) {
        num = 1 + std::rand() % 100;
    }

    // Выводим вектор
    std::cout << "Сгенерированный вектор: ";
    for (int num : vec) {
        std::cout << num << " ";
    }
    std::cout << "\n";

    // Находим максимальный элемент
    int max = vec[0];
    for (int num : vec) {
        if (num > max) {
            max = num;
        }
    }

    // Находим минимальный элемент
    int min = vec[0];
    for (int num : vec) {
        if (num < min) {
            min = num;
        }
    }

    // Находим среднее значение
    double average = static_cast<double>(std::accumulate(vec.begin(), vec.end(), 0)) / vec.size();

    // Выводим результаты
    std::cout << "Максимальный элемент: " << max << "\n";
    std::cout << "Минимальный элемент: " << min << "\n";
    std::cout << "Среднее значение: " << average << "\n";

    return 0;
}