/*
Заполнить вектор рандом числами, найти min, max, avg, sum. Все делать через for по коллекции.
*/

#include <iostream>
#include <vector>
#include <cstdlib> // для rand() и srand()
#include <ctime>   // для time()
#include <numeric>  // для accumulate()
#include <algorithm> // для min_element/max_element

int main() {
    // Инициализация генератора случайных чисел
    std::srand(std::time(nullptr));

    // Создаем вектор из 15 элементов
    const size_t SIZE = 15;
    std::vector<int> vec(SIZE);

    // 1. Заполняем вектор случайными числами (от 10 до 99)
    for (int& num : vec) {
        num = 10 + std::rand() % 90; // диапазон 10-99
    }

    // 2. Выводим вектор
    std::cout << "Сгенерированный вектор:\n";
    for (int num : vec) {
        std::cout << num << " ";
    }
    std::cout << "\n\n";

    // 3. Находим максимальный элемент (3 способа)
    // Способ 1: range-based for
    int max1 = vec[0];
    for (int num : vec) {
        if (num > max1) max1 = num;
    }
    
    // Способ 2: STL алгоритм
    int max2 = *std::max_element(vec.begin(), vec.end());
    
    std::cout << "Максимальный элемент (for): " << max1 << "\n";
    std::cout << "Максимальный элемент (STL): " << max2 << "\n\n";

    // 4. Находим минимальный элемент
    int min = vec[0];
    for (int num : vec) {
        if (num < min) min = num;
    }
    std::cout << "Минимальный элемент: " << min << "\n\n";

    // 5. Находим сумму элементов
    // Способ 1: range-based for
    int sum1 = 0;
    for (int num : vec) {
        sum1 += num;
    }
    
    // Способ 2: STL алгоритм
    int sum2 = std::accumulate(vec.begin(), vec.end(), 0);
    
    std::cout << "Сумма элементов (for): " << sum1 << "\n";
    std::cout << "Сумма элементов (STL): " << sum2 << "\n\n";

    // 6. Находим среднее значение
    double average = static_cast<double>(sum1) / vec.size();
    std::cout << "Среднее арифметическое: " << average << "\n";

    return 0;
}