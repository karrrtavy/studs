#include <iostream>
#include <vector>
#include <stdio.h>
#include <map>

using namespace std;


int main() {

    // Тема: C++11
    // Вывод че то там
    auto i = 1;
    cout << i << endl;

    vector<int> v = {1, 2, 3};

    map<string, multimap<string, int>> index_map;
    map<string, multimap<string, int>>::iterator it = index_map.begin();
    auto it2 = index_map.begin();

    for(auto it = v.begin(); it != v.end(); ++it)
        cout << *it << ' ';

    cout << endl;

    for(vector<int>::iterator it = v.begin(); it != v.end(); ++it)
        cout << *it << ' ';

    return 0;
}