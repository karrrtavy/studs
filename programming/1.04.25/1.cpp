#include <iostream>
#include <string>

using namespace std;

class Figure {
public:
    static Figure* createFigure(string name);

    virtual void draw() = 0;
};
class Circle : public Figure {
public:
    virtual void draw() {
        cout << "Draw Circle\n";
    }
};
class Rect : public Figure {
public:
    virtual void draw() {
        cout << "Draw Rect\n";
    }
};   
Figure* Figure::createFigure(string name) {
    if (name == "Circle")
        return new Circle();
    if (name == "Rect")
            return new Rect();

    return 0;
}


int main(){
    
    // паттерны программирования (проектирования). Приемы ООП
    // пораждащие шаблоны и поведенческие
    /*
    шаблон проектирования - хорошее решение типовой задачи, возникающей при разработке. 
    пораждающие шаблоны позволяют удобно создавать объекты.
    фабричный метод - пораждающий шаблон,определяющий интерфейс для создания объекта. цели: заранее неизветстно, объекты каких подклассов ему нужно создавать   
    */ 
   Figure* f1 = Figure::createFigure("Circle");
   Figure* f2 = Figure::createFigure("Rect");

   f1->draw();
   f2->draw();

   /*
    Figure* r = new Rect();
    Figure* f = Figure::creatFigure('Rect');

    2 способ лучше тем, что хз
   */

    /*
    Object pool - шаблон позволяет реализовать потворное использование объектов, за счет сохраненяия места уничтожения
    */

    /*
    Шаблон проектирования (object pool) - позволяет заранее создать объекты, можно ограничить кол-во объектов.    
    */

    /*
    шаблон Наблюдатель - тип: поведенческий. Он определяет зависимость "один ко многим" между объектами так, что когда один меняет свое состояние,
    все зависимые объекты оповещаются и обновляются автоматически 
    */

    return 0;
}