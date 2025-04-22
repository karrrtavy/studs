from random import randint
file = open(r'crossplatformprogramming\5\ind6.txt', 'w')
for i in range(10):
    file.write(str(randint(1, 9)))
file.close()
file = open(r'crossplatformprogramming\5\ind6.txt', 'r')
print(*file)