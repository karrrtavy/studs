import random
a = random.randint(0, 10)
b = 10
for i in range(1, b + 1, 2):
    a += 1
    if b == 5: continue
    print(a)
    if a == 7: break
print('The end')