//лекция 9.12.24
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

class TestPred{
    public:
    bool operator()(int i){
        cout<<i<<' ';
        //terminal output
        //
        if (i > 3 && i < 7)
            return true;
        return false;
    }   
};

class PrintPred{
    public:
    bool operator()(int i){
        cout<<i<<' ';
        return false;
    }
};

int main(){
	//iterator - объект, с помощью которого можно перебрать контейнер/коллекцию в некоторой последовательности. *чем-то похож на указатель.
    vector<int> collection = {1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,6,7,8,9,10};
    PrintPred pp;
    for_each(collection.begin(), collection.end(), pp); cout<<"\n";
    //1 2 3 4 5 1 2 3 4 5 1 2 3 4 5 6 7 8 9 10 


    //алгоритмы:
    //
	//size_t count(It p, It q, const T& x);	size_t (начало, элемент последовательности, ...)
	//size_t count_if(It p, It q, preq p); алгоритм возвращает кол-во раз, когда p = истина для элементов коллекции
	for (int i=0;i<11;++i){
		cout<<"count "<<i<<" = "<<count(collection.begin(), collection.end(), i) << endl;
        //terminal output:
        // count 0 = 0
        // count 1 = 3
        // count 2 = 3
        // count 3 = 3
        // count 4 = 3
        // count 5 = 3
        // count 6 = 1
        // count 7 = 1
        // count 8 = 1
        // count 9 = 1
        // count 10 = 1
	}
    
    TestPred tp;
    cout<<"TestPred: "<<count_if(collection.begin(), collection.end(), tp) <<endl;
    //terminal output
    //TestPred: 7

    cout<<"TestPred test: "<<tp(4)<<endl;
    //terminal output
    //TestPred test: 1

    //It find(It p, It q, preq p);
    //It find(It p, It q, const T& x);
    vector<int>::iterator result_1 = find(collection.begin(), collection.end(), 3);
    if(result_1 == collection.end())
        cout<<"element not found\n";
	else
        cout<<"element found " << *result_1<<"\n";
        //terminal output:
        //element found 3

    vector<int>::iterator result_2 = find_if(collection.begin(), collection.end(), tp);
    if(result_2 == collection.end())
        cout<<"element not found\n";
	else
        cout<<"element found " << *result_2<<"\n";
        //terminal output:
        //1 2 3 4 element found 4


    //random_shuffle(It p, It q);
    random_shuffle(collection.begin(), collection.end());   //random_shuffle перемешивает элементы в случайном порядке
    find_if(collection.begin(), collection.end(), pp); cout<<"\n";
    //5 1 2 6 5 7 8 2 2 5 4 3 10 3 1 3 1 9 4 4 

    //reverse(It p, It q);
    reverse(collection.begin(), collection.end());
    find_if(collection.begin(), collection.end(), pp); cout<<"\n"; 
    //4 4 9 1 3 1 3 10 3 4 5 2 2 8 7 5 6 2 1 5 

    //Func for_each (It p, It q, Func f); можно вместо find_if
    for_each(collection.begin(), collection.end(), pp); cout<<"\n";

    //rotate(It p, It middle, It q); алгоритм сдвигает элементы последовательности так, что элемент, на который указывает итератор, становится первым
    rotate(collection.begin(), collection.begin()+3, collection.end()); //begin()+3 - указывает на элемент, который будет первым
    for_each(collection.begin(), collection.end(), pp); cout<<"\n";
    //4 5 1 2 3 4 5 1 2 3 4 5 6 7 8 9 10 1 2 3 

    //reomve(It p, It q, const T& x);   алгоритм "удаляет" из последовательности элементов равной X, возвращает итератор на конец новой 
    //
    // vector<int>::iterator newEnd = remove(collection.begin(), collection.end(), 1);
    // for_each(collection.begin(), collection.end(), pp); cout<<"\n";
    // //4 5 2 3 4 5 2 3 4 5 6 7 8 9 10 2 3 1 2 3 
    // for_each(collection.begin(), newEnd, pp); cout<<"\n";
    // //4 5 2 3 4 5 2 3 4 5 6 7 8 9 10 2 3 
    // for_each(newEnd, collection.end(), pp); cout<<"\n";
    // //1 2 3
    //
    // collection.erase(newEnd, collection.end());
    // for_each(collection.begin(), collection.end(), pp); cout<<"\n";
    // //4 5 2 3 4 5 2 3 4 5 6 7 8 9 10 2 3 
    //
    collection.erase(remove(collection.begin(), collection.end(), 1), collection.end());
    for_each(collection.begin(), collection.end(), pp); cout<<"\n";    
    //4 5 2 3 4 5 2 3 4 5 6 7 8 9 10 2 3     

    //sort(It p, It q); сортировка
    sort(collection.begin(), collection.end());
    for_each(collection.begin(), collection.end(), pp); cout<<"\n";

    //stable_sort(It p, It q); стабильная и устойчивая соритровка не меняет порядок одинаковых элементов
    stable_sort(collection.begin(), collection.end());
    for_each(collection.begin(), collection.end(), pp); cout<<"\n";
    //1 1 1 2 2 2 3 3 3 4 4 4 5 5 5 6 7 8 9 10  

    //unique(It p, It q); "удаляет" подряд идущие одинаковые элементы. оставляет по одному значению
    //
    // unique(collection.begin(), collection.end());
    // for_each(collection.begin(), collection.end(), pp); cout<<"\n";
    // //1 2 3 4 5 6 7 8 9 10 4 4 5 5 5 6 7 8 9 10
    //
    collection.erase(unique(collection.begin(), collection.end()), collection.end());
    for_each(collection.begin(), collection.end(), pp); cout<<"\n";
    //1 2 3 4 5 6 7 8 9 10 

    

    return 0;
}