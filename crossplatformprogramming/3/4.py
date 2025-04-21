sum = 0
a = int(input())
while a != 5:
    sum += a
    if a < 0: print('Отрицательное число'); break
    a = int(input())
else: print('Все положительные'); print(sum)