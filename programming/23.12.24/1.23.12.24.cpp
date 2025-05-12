#include <iostream>

using namespace std;


int main() {
    /*  Числа с плавающей точкой    */
    cout << sizeof(float) << endl;
    /*
    Terminal: 4
    */
    cout << (1.0f +2.0f == 3.0f) << endl;
    /*
    Terminal: 1
    */
    cout << (0.1f + 0.2f == 0.3f) << endl;
    /*
    Terminal: 1
    */
    cout << (0.1 + 0.2 == 0.3) << endl;
    /*
    Terminal: 0
    */
    cout << (0.1 + 0.2) << endl;
    /*
    Terminal: 0.3
    */
    cout << (1.0 + 2.0 == 3.0) << endl;
    /*
    Terminal: 1
    */

    cout << "__________\n";

    cout << (16777215.f == 16777216.f) << endl;
    /*
    Terminal: 0
    */
    cout << (16777216.f == 16777217.f) << endl;
    /*
    Terminal: 1
    */

    cout << "__________\n"; 

    cout << 2000000000 << endl;
    cout << 2000000001 << endl;
    cout << 2000000064 << endl;
    cout << 2000000065 << endl;
    /*
    Terminal:
    2000000000
    2000000001
    2000000064
    2000000065
    */
    cout.setf(ios::fixed);
    cout << 2000000000.f << endl;
    cout << 2000000001.f << endl;
    cout << 2000000064.f << endl;
    cout << 2000000065.f << endl;
    /*
    Terminal:
    2000000000.000000
    2000000000.000000
    2000000000.000000
    2000000128.000000
    */

    cout << "__________\n";

    cout.setf(ios::fixed);

    



    return 0;
}