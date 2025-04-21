sum_pos = 0
sum_neg = 0
while True:
    num = int(input("Input a number: "))    
    if num == 0:
        break    
    if num > 0:
        sum_pos += num
    else:
        sum_neg += num
print(f"Сумма положительных чисел: {sum_pos}")
print(f"Сумма отрицательных чисел: {sum_neg}")