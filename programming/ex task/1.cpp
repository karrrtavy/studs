/*
Задача:
Заполнить вектор на рандом, использовать лямбда-функцию и фор по коллекции, 
вывести числа и найти их сумму
*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {
    srand(time(0));

    // создание и заполнение вектора случайными числами
    vector<int> numbers(10); // вектор из 10 элементов
    generate(numbers.begin(), numbers.end(), []() { 
        return rand() % 100 + 1; // генерация чисел от 1 до 100
    });

    for (int num : numbers) {
        cout << num << " ";
    }
    cout << endl;

    // вычисление суммы с использованием лямбда-функции
    int sum = 0;
    for_each(numbers.begin(), numbers.end(), 
        [&sum](int n) { sum += n; }
    );

    cout << sum << endl;

    return 0;
}