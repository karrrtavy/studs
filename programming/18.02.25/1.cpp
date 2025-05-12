#include <iostream>
#include <initializer_list>
#include <vector>

using namespace std;

class X {
public:
    X(initializer_list<int> il) {
        cout << *il.begin() << endl;
        cout << *il.begin()+1 << endl;
        cout << *il.begin()+2 << endl;
    }
};


int main() {

    // Тема: C++11
    // Списки и инициализация
    X x = {1, 2, 3};

    vector<int> v = {1, 2, 3};
    cout << v[0] << v[1] << v[2] << endl;

    return 0;
}