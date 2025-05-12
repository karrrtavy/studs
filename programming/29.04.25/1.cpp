#include <iostream>


using namespace std;
// шаблон наблюдателя: разбор, улучшения, парсинг обновлений на несклько состояний
class Document {};

class Figure {};

class Point {};

class InputObserver {
public:
    virtual void onKeyPressed(string key) {}
    virtual void onMouseMoved(Point position) {}
    virtual void onMousePressed(string button) {}
};

class Observer {
public:
    // virtual void update(Document* doc) = 0;
    virtual void onChangeProperties(Document* doc, Figure* f) {}
    
    virtual void onSetLink(Figure* parent, Figure* child) {} 
    virtual void onRemoveLink(Figure* parent, Figure* child) {} 

    virtual void onAddFigure(Figure* f) {}
    virtual void onRemoveFigure(Figure* f) {}
};

class FigureCountObserver : public Observer {
public:
    void onAddFigure(Figure* f) {}
    void onRemoveFigure(Figure* f) {}
};

class DocumentSctructureObserver : public Observer {
public:    
    void onSetLink(Figure* parent, Figure* child) {} 
    void onRemoveLink(Figure* parent, Figure* child) {} 
    void onAddFigure(Figure* f) {}
    void onRemoveFigure(Figure* f) {}
};

class LogObserver : public Observer {
public:
    void onChangeProperties(Document* doc, Figure* f) {}
    void onSetLink(Figure* parent, Figure* child) {} 
    void onRemoveLink(Figure* parent, Figure* child) {} 
    void onAddFigure(Figure* f) {}
    void onRemoveFigure(Figure* f) {}
}; 

int main() {

    return 0;
}