/*
Заполнить deque случайными числами. 
С помощью цикла for по коллекции найти максимум, минимум, сумму и среднее значение
*/

#include <iostream>
#include <deque>
#include <ctime>
#include <cstdlib>
#include <limits>

int main() {
    // Инициализация генератора случайных чисел
    std::srand(std::time(nullptr));

    // 1. Создаем и заполняем deque 15 случайными числами (от 1 до 100)
    std::deque<int> dq;
    for (int i = 0; i < 15; ++i) {
        dq.push_back(1 + std::rand() % 100);
    }

    // 2. Выводим содержимое deque
    std::cout << "Содержимое deque: ";
    for (int num : dq) {
        std::cout << num << " ";
    }
    std::cout << "\n\n";

    // 3. Находим максимум, минимум, сумму и среднее
    if (dq.empty()) {
        std::cout << "Deque пуст!\n";
        return 0;
    }

    int max = dq[0];
    int min = dq[0];
    int sum = 0;

    // Range-based for цикл для вычислений
    for (int num : dq) {
        if (num > max) max = num;
        if (num < min) min = num;
        sum += num;
    }

    double average = static_cast<double>(sum) / dq.size();

    // 4. Выводим результаты
    std::cout << "Максимальное значение: " << max << "\n";
    std::cout << "Минимальное значение: " << min << "\n";
    std::cout << "Сумма элементов: " << sum << "\n";
    std::cout << "Среднее значение: " << average << "\n";

    return 0;
}