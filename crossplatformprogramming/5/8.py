file = open(r'crossplatformprogramming\5\строки.txt', 'w')
file.write('строка 1')
file.write('строка 2')
file.close()
list_l = []
file = open(r'crossplatformprogramming\5\строки.txt', 'r')
for line in file:
    list_l.append(line.strip())
    print(list_l)