def add(x, y):
    return x + y
print(add('123', '456'))
print(add('abc', 'abc'))

def newfunc(n):
    def myfunc(x):
        return x + n
    return myfunc
new = newfunc(100)
print(new(200))

def inputfunc(a, b, c):
    return a[::-1], float(b), ord(c)
a1 = str(input('Input a string: '))
b1 = int(input('Input a digit: '))
c1 = (input('Input another one: '))
func = inputfunc(a1, b1, c1)
print(func)