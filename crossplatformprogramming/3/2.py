sum = 0
while True:
    a = int(input())
    if a == 5: break
    sum += a
print(sum)

import random
sum = 0
while True:
    a = random.randint(0, 10)
    print(a)
    if a == 5: break
    sum += a
print(sum)