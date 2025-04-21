def input_bytes():
    while True:
        try:
            byte = int(input('Input value of bytes: '))
            return byte
        except ValueError:
            print('Try again')

class Transformation:
    def kbyte(self, byte):
        return byte / 1024

    def mbyte(self, kbyte):
        return kbyte / 1024
    
def main():
    transform = Transformation()

    while True:
        byte = input_bytes()

        kbyte = transform.kbyte(byte)
        print(f'{byte} bytes transformed to {kbyte} kbytes')
        mbyte = transform.mbyte(kbyte)
        print(f'{kbyte} kbytes transformed to {mbyte} mbytes')

if __name__ == '__main__':
    main()

