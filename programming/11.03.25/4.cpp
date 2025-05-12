#include <iostream>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <map>

#define X 123


using namespace std;


class TestClass{
    public:
        void operator()(int x){
            auto f = [&](int x){this->print(x);};
            f(x);
        }
        void print(int x){
            cout << x << ' ';
        }
};
// такое лучше не стоит использовать

class PredClass{
public:
    void operator()(int x){
        cout << x << ' ';
    }
};

template<class Pred>
void fun(vector<int>& vec, Pred p){
    for (int i : vec)
        p(i);
}


int main() {

    cout << X << endl;

    vector<int> v = {1, 3, 5, 2, 4, 1, 5, 7, 4, 9, 3, 4};

    fun(v, [](int x){cout << x << ' ';});
    /* передаем лямбду функцию */

    cout << endl;

    PredClass pc;
    fun(v, pc);
    /* использование объекта класса с перегруженным оператором */

    /*
    в первом случае передаем лямбду функцию,
    во втором случае передаем объекта класса с перегруженным оператором.
    */

    return 0;
}