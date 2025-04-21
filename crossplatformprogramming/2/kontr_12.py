import math


def input_sides():
    while True:
        try:
            a = float(input('Input side of the triangle: '))
            b = float(input('Input side of the triangle: '))
            c = float(input('Input side of the triangle: '))
            return a, b, c
        except ValueError:
            print('Try again')

def perimeter(a, b, c):
    p = a + b + c
    return p

def area(a, b, c, p):
    pp = p / 2
    s = math.sqrt(pp * (pp - a) * (pp - b) * (pp - c))
    return s

def main():
    while True:
        a, b, c = input_sides()
        p = perimeter(a, b, c)
        print(f'perimeter: {p}')
        s = area(a, b, c, p)
        print(f'Area: {s}')

        exit = str(input('Y/n? '))
        if exit.lower() == 'n':
            break
        else:
            continue

if __name__ == '__main__':
    main()