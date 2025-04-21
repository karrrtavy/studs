a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if (a != 0 and b != 0 and c != 0) and (b + c != 0) and (a - c != 0):
    z1 = ((1 / a - 1 / (b + c)) / (1 / a + 1 / (b + c))) * (1 + ((b** 2 + c** 2 - a** 2) / (2 * b * c))) / ((a - b - c) / (a * b * c))
    print(f"z1 = {z1}")
    
    z2 = ((a - b - c) / 2) * a
    print(f"z2 = {z2}")
else:
    print('ZeroDivisonError')
