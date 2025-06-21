/*
Заполнить deque случайными числами с помощью алгоритма
for each и лямда функции. найти все нечетные числа 
больше определенного значения. Посчитать их сумму.
*/

#include <iostream>
#include <deque>
#include <algorithm>
#include <ctime>
#include <cstdlib>

int main() {
    // Инициализация генератора случайных чисел
    std::srand(std::time(nullptr));

    // Создаем deque и заполняем 20 случайными числами (от 1 до 100)
    std::deque<int> dq(20);
    std::for_each(dq.begin(), dq.end(), [](int& x) {
        x = 1 + std::rand() % 100;
    });

    // Выводим содержимое deque
    std::cout << "Сгенерированный deque:\n";
    std::for_each(dq.begin(), dq.end(), [](int x) {
        std::cout << x << " ";
    });
    std::cout << "\n\n";

    // Задаем пороговое значение (например, 50)
    const int threshold = 50;
    std::cout << "Ищем нечётные числа больше " << threshold << "\n";

    // Находим нечётные числа больше threshold и считаем их сумму
    int sum = 0;
    std::cout << "Найденные числа: ";
    std::for_each(dq.begin(), dq.end(), [threshold, &sum](int x) {
        if (x > threshold && x % 2 != 0) {
            std::cout << x << " ";
            sum += x;
        }
    });

    // Выводим результат
    std::cout << "\nСумма найденных чисел: " << sum << "\n";

    return 0;
}