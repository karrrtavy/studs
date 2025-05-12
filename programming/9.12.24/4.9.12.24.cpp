//лекция 9.12.24
#include <iostream>
#include <algorithm>
#include <vector>

//little_endian младший байт записывается по меньшему адрессу. big_endian наоборот      

using namespace std;

//0000 0001     0010 1101
//1111 1110     1101 0010
//1111 1111     1101 0011
//0000 0000     0010 1100
//0000 0001     0010 1101

//0000 0000 0000 0000 0000 0000 0000 0000
//2^32 = 4 294 967 296 = 0010 0000 0000 0000 0000 0000 0000 0000
//2^32 - 1 = 4 294 967 295 = 1111 1111 1111 1111 1111 1111 1111 1111
//0 - положительное
//1 - отрицательное 

//max int = 2 147 483 647

//1000 0000     0000 0000   0000 0000   0000 0000 
//0100 0000     0000 0000   0000 0000   0000 0000 
//0010 0000     0000 0000   0000 0000   0000 0000 

void printBin(int value){
    int count = sizeof(value) * 8;
    for(int i = count - 1; i >= 0; --i){
        int m = 1 << i;
        int res = m & value;
        if(res)
            cout<< 1;
        else
            cout<< 0;
        if(i != 0){
            if(i % 4 == 0) cout << ' ';
            if(i % 8 == 0) cout << ' ';
        }
    }
    cout<<endl;
}

int main(){

    int i = 0;
    char* pc = (char*)&i; //получение адреса переменной i и указатель на ее элементы

    cout <<(int)pc[0] << (int)pc[1] << (int)pc[2] << (int)pc[3] << endl;
    //0000

    pc[0] = 1;
    pc[1] = 1;
    cout << i << endl;
    //257

    cout << (int*)&pc[0] << endl << (int*)&pc[1] << endl << (int*)&pc[2] << endl << (int*)&pc[3] << endl;
    // 0x7fffc6cd24dc
    // 0x7fffc6cd24dd
    // 0x7fffc6cd24de
    // 0x7fffc6cd24df    

    return 0;
}