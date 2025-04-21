a = int(input('Input the first number: '))
b = int(input('Input the second number: '))
if a > b:
    print(f'{a}>{b};{a}-{b}={a-b}')
else:
    print(f'{a} < {b}; {b} - {a} = {b-a}')
c = int(input('Input the second number: '))
d = int(input('Input the second number: '))
if c > d:
    print(f'{c}>{d};{c}-{d}={c-d}')
else:
    print(f'{c} < {d}; {d} - {c} = {d-c}')
e = int(input('Input the second number: '))
f = int(input('Input the second number: '))
if e > f:
    print(f'{e}>{f};{e}-{f}={e-f}')
else:
    print(f'{e} < {f}; {f} - {e} = {f-e}')

print('___________________')

i = 0
while i < 3:
    a = int(input('Input the first number: '))
    b = int(input('Input the second number: '))
    if a > b:
        print(f'{a}>{b};{a}-{b}={a-b}')
    else:
        print(f'{a} < {b}; {b} - {a} = {b-a}')
        i += 1

print('___________________')

def diff():
    m = int(input('Input the first number: '))
    n = int(input('Input the second number: '))
    if m > n:
        print(f'{m}>{n};{m}-{n}={m-n}')
    else:
        print(f'{m} < {n}; {n} - {m} = {n-m}')
    return m, n

a1, b1 = diff()
c1, d1 = diff()
e1, f1 = diff()