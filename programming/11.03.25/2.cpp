#include <iostream>
#include <vector>
#include <stdio.h>
#include <map>

using namespace std;


int main() {

    //цикл for по коллекции
    vector<int> v = {1, 2, 3};

    for(auto it = v.begin(); it != v.end(); ++it)
        cout << *it << ' ';

    cout << endl;

    for(vector<int>::iterator it = v.begin(); it != v.end(); ++it)
        cout << *it << ' ';

    cout << endl;

    for(int& i : v)     //тот самый цикл for по коллекции в короткой записи
        cout << i << ' ';
    /* объявляем тип итератора по коллекции, и саму коллекцию, 
    работает с контейнерами у которых есть метды begin() и end(),
    и их методы должны возвращать итератор.
    с апперсантом i может менять значения контейнера, а без & просто для вывода.
    auto упрощает запись, при этом необходимо знать что за тип,
     и есть ли смысл упрощать запись */

    return 0;
}