a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if a % 2 and b % 2 and c % 2 or a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
    a += 1
    c += 1
print(a, b, c)
if a % 2 and c % 2:
    print(a, c)
else:
    print(b)