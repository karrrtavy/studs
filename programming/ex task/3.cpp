/*
задача записать в вектор рандомные числа, с помощью алгоритма for_each и lambda-выражения 
распределить чётные числа в list и нечётные в  deque
*/

#include <iostream>
#include <vector>
#include <list>
#include <deque>
#include <algorithm>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {
    srand(time(0));

    // заполнение вектора случайными числами
    vector<int> numbers(15);
    generate(numbers.begin(), numbers.end(), []() { 
        return rand() % 100 + 1; 
    });

    for (int num : numbers) {
        cout << num << " ";
    }
    cout << "\n\n";

    // контейнеры для чётных и нечётных чисел
    list<int> evenNumbers;    // чётные
    deque<int> oddNumbers;    // нечётные

    // распределение чисел с помощью for_each и лямбды
    for_each(numbers.begin(), numbers.end(), 
        [&evenNumbers, &oddNumbers](int num) {
            if (num % 2 == 0) {
                evenNumbers.push_back(num);
            } else {
                oddNumbers.push_front(num);
            }
        });

    cout << "чётные числа:  ";
    for (int num : evenNumbers) {
        cout << num << " ";
    }

    cout << "\n нечётные числа: ";
    for (int num : oddNumbers) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}