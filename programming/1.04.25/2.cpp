#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


class Document;

class Observer {
public:
    virtual void update(Document* doc) = 0;
};

class Document {
    vector<int> state;
    vector<Observer*> observers;
    void notify() {
        for (int i =0; i < observers.size(); ++i)
            observers[i]->update(this);
    }
public:
    void add(int a) {
        state.push_back(a);
        notify();
    }
    virtual void getState(Observer* o) = 0;

    void remove(int index) {
        state.erase(state.begin() + index);
        notify();
    }
    void attach(Observer* o) {
        observers.push_back(o);
    }
    void dettach(Observer* o) {
        observers.erase(find(observers.begin(), observers.end(), o));
    }
};

class PrintObserver : public Observer {
public:
    void update(Document* doc) {
        vector<int>& state = doc->getState();
        for (int i = 0; i < state.size(); ++i)
            cout << state[i] << ' ';
        cout << endl;
};

class SumObserver : public Observer {
public:
    void update(Document* doc) {
        int summ = 0;
        vector<int>& state = doc->getState();
        for (int i = 0; i < state.size(); ++i) 
            summ += state[i];
        cout << "Summ: " << summ << endl; 
    }
};

void main(){
    Document doc;
    
    PrintObserver po;
    doc.attach(&po);

    SumObserver so;
    doc.attach(&so);

    for (int i = 0; i < 10; ++i)
        doc.add(i);
}