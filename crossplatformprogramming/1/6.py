y = int(input("Введите год "))
if y % 4 != 0:
    print("Обычный")
elif y % 100 == 0:
    if y % 400 == 0:
        print("Високосный")
    else:
        print("Обычный")
else:
    print("Високосный")

Century = y // 100
if  y % 100 <= 0:
    print(Century, "век")
else:
    print(Century + 1, "век")