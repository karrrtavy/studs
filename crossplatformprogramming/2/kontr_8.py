x = int(input('Input number 1 to 9: '))

if 1 <= x <= 3:
    s = input('Input again: ')
    n = int(input('Input repeats: '))
    for i in range(n):
        print(f'b: {i + 1}: {s}')
if 4 <= x <= 6:
    m = int(input('Input a degree: '))
    print(f'c: {x.__pow__(m)}')
if 7 <= x <= 9:
    for i in range(10):
        x += 1
        print(f'd: {i + 1}: {x}')
else:
    print('Input error')