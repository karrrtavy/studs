#include <iostream>
#include <time.h>
#include <stdlib.h>
#include <limits.h>
#include <cfloat>

using namespace std;


int main() {

    srand(time(0));
    cout.setf(ios::fixed);
    cout << sizeof(int) << endl;
    /*
    Terminal: 4
    */    
    cout << sizeof(long) << endl;
    /*
    Terminal: 8
    */
    cout << RAND_MAX << endl;
    /*
    Terminal: 2147483647
    */

    int count = 30000000;
    int avgWieght = 70;
    int delta = 30;
    int totalWieght = 0;
    /*
    если totalWieght тип заменить на float, то при большом count результат будет некорректным
    но если заменить на int, то при большом count результат будет приближенным к avgWieght при любом count, не больше 30000000
    */
    for (int i = 0; i < count; ++i) {
        int w = avgWieght - delta + (rand() % (2 * delta + 1));
        totalWieght += w;
    }
    cout << (float)totalWieght / count << endl;
    /*
    Terminal: 70.000740
    */

    cout << "__________\n";

    /*
    float 4 байта, 32 бита
        Sign 1 бит
        Exponent 8 бит
        Mantissa 23 бита

        S Exponent Mantissa
        0 00000000 00000000000000000000000

        (-1)^S * 1.M * 2^(E - 127)

    1. Есть число с плавающей точкой.
    2. Переводим целую и дробную часть в двоичную систему
    3. Сдвигаем точку на N разрядов влево или вправо, так, чтобы целая часть = 1
    0.00000101 вправо на 6, N = 6
    0.1
    101011.101 влево на 5, N = 5
    1.01011101
    4. Записываем знак
    5. Часть числа после точки записываем в мантиссу
    6. Экспоненту записываем как 127 + N (кол-во разрядов)

        185.4375 = 10111001.0111
                   .01110010111 - Mantissa
                
        0 10000110 01110010111000000000000

                   127 + 7 = 134
        185     128 + 32 + 16 + 8 + 1   10111001
        .4375   .0111    
        1 / 2 = 0.5
        1 / 4 = 0.25
        1 / 8 = 0.125
        1 / 16 = 0.0625
        1 / 32 = 0.03125


        Обратный перевод
        0 10000110 01110010111000000000000

        10000110 = 2 + 4 + 128 = 134 - 127 = 7
        1.01110010111 -> 10111001.0111
        185.4375
    */

    cout.setf(ios::fixed);

    cout << UINT_MAX << endl;
    /*
    Terminal: 4294967295
    */
    cout << sizeof(int) << endl;
    cout << sizeof(float) << endl;
    /*
    Terminal:
    4
    4
    */
    
    float f = 2000000000.f;
    
    cout << f << endl;
    /*
    Terminal: 2000000000.000000
    */
    f += 64;
    cout << f << endl;
    /*
    Terminal: 2000000000.000000
    */
    f += 65;
    cout << f << endl;
    /*
    Terminal: 2000000128.000000
    */

    cout << FLT_MIN << endl;
    /*
    Terminal: 0.000000
    */
    cout << FLT_MAX << endl;
    /*
    Terminal: 340282346638528859811704183484516925440.000000
    */

   return 0;
}