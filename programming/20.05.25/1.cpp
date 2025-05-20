#include <iostream>


using namespace std;

int main() {
    // тема: рефакторинг
    // рефакторинг - изменение структуры программы без изменения наблюдаемого поведения, направленное на улучшение качества кода
    /*
    причины проведения рефакторинга:
        1. дублирвоание кода (пр. два похожих блока);
        2. большой объем методов и функций ();
        3. большой цикл или большая глубины вложенных циклов ();
        4. класс имеет плохую связанность ();
            неверно:
            class Rect {
            public:
                void draw();
                void loadFromFile(); убрано с помощью FileManager
                void saveToFile(); убрано с помощью FileManager

                void calculate(); убрано с помощью Algorythm
            };
            верно:
            class Figure {
            public:
                void draw(Rect* r);
            };
            class FileManager {
            public:
                Rect* loadRect(string fileName)
                void saveRect(Rect* r, string fileName);
                ... другие объекты ...
            };
            class Algorythm {
            public:
                static void algorythm_1(Rect* r);
            };

            интерфейс класса формируется абстракцией
        5. метод принимает слишком много параметров  ();
        6. при изменении программы требуется вносить изменения в несколких классах (); 
            class Figure
            class Rect
            ...
            class Circle
            class X
        7. необходимо изменять несколько иерархий классов ();
        8. приходиться параллельно изменять несколько блоков case / if-else;
            class Client {
            public:
                virtual void doSomething() {}
            };
            class ClientReguelar : public Client {};
            class ClientVIP : public Client {};

            int main() {
                //рефакторим
                if(clientType == 1)
                    ...
                else if(clientType == 2)
                    ...
                ...

                Client* c = new ClientVIP();
                ...
                c->doSomething;
            }
        9. родственные элементы данных используемые вместе не объедененны в класс ();
            class Point2f {};
            class Vector2f {
            public:
                float x, y;
            };
            class Figure {
                Vector2f position;
            };

            void f(int x, int y) {
                
            }
        10. метод использует больше элементов другого класса, чем своего собственного ();
        11. элементарный тип данных перегружен ();
            int x = 100; рублей
            int y = 20; градусов
            int z = 10; яблок
        12. класс имеет ограниченную функциональность ();
        13. бродячие данные ();
        
    */

    

    return 0;
}