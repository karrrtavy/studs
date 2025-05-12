#include <iostream>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <map>

using namespace std;


int main() {

    // лямбда функции
    vector<int> v = {1, 3, 5, 2, 4, 1, 5, 7, 4, 9, 3, 4};

    int summ = 0;

    for_each(
        v.begin(), 
        v.end(), 
        [](int x){cout << x << ' ';}
    );
    //лямбда функция - такая функция, которую можно объявить на месте использования
    // также можно передать в качестве параметра

    cout << endl;
    for_each(
        v.begin(), 
        v.end(),
        [&summ](int x){
            cout << x << ' ';
            summ += x;
        }
    );
    cout << endl << "Summ: " << summ << endl;

    // auto f = [](int x){cout << x << ' ';};
    // f(111);

    return 0;
}