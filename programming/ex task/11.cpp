/*
Задача: Разработать класс, в котором два метода, минимум и максимум, параметры передаются с помощью вектора и списка инициализации
*/

#include <iostream>
#include <vector>
#include <initializer_list>
#include <algorithm> // для std::min_element, std::max_element
#include <limits>    // для std::numeric_limits

class MinMaxFinder {
public:
    // Метод для нахождения минимума в векторе
    int findMin(const std::vector<int>& vec) {
        if (vec.empty()) {
            std::cerr << "Ошибка: вектор пуст!\n";
            return std::numeric_limits<int>::max(); // возвращаем максимальное значение int
        }
        return *std::min_element(vec.begin(), vec.end());
    }

    // Метод для нахождения максимума в векторе
    int findMax(const std::vector<int>& vec) {
        if (vec.empty()) {
            std::cerr << "Ошибка: вектор пуст!\n";
            return std::numeric_limits<int>::min(); // возвращаем минимальное значение int
        }
        return *std::max_element(vec.begin(), vec.end());
    }

    // Метод для нахождения минимума в списке инициализации
    int findMin(std::initializer_list<int> list) {
        if (list.size() == 0) {
            std::cerr << "Ошибка: список пуст!\n";
            return std::numeric_limits<int>::max();
        }
        return *std::min_element(list.begin(), list.end());
    }

    // Метод для нахождения максимума в списке инициализации
    int findMax(std::initializer_list<int> list) {
        if (list.size() == 0) {
            std::cerr << "Ошибка: список пуст!\n";
            return std::numeric_limits<int>::min();
        }
        return *std::max_element(list.begin(), list.end());
    }
};

int main() {
    MinMaxFinder finder;

    // Пример с вектором
    std::vector<int> numbers = {5, 2, 9, 1, 7, 4};
    std::cout << "Минимум в векторе: " << finder.findMin(numbers) << "\n";
    std::cout << "Максимум в векторе: " << finder.findMax(numbers) << "\n\n";

    // Пример со списком инициализации
    std::cout << "Минимум в списке: " << finder.findMin({8, 3, 6, 2, 5}) << "\n";
    std::cout << "Максимум в списке: " << finder.findMax({8, 3, 6, 2, 5}) << "\n";

    // Пример с пустыми контейнерами
    std::vector<int> empty_vec;
    std::cout << "\nПроверка пустого вектора:\n";
    std::cout << "Минимум: " << finder.findMin(empty_vec) << "\n";
    std::cout << "Максимум: " << finder.findMax(empty_vec) << "\n";

    std::cout << "\nПроверка пустого списка:\n";
    std::cout << "Минимум: " << finder.findMin({}) << "\n";
    std::cout << "Максимум: " << finder.findMax({}) << "\n";

    return 0;
}