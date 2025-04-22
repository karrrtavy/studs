# первые 16 предложений во второй файл. нужно посчитать кол-во гласных и кол-во согласных и вывести их кол-во.
# в новый файл записать предложения из 1 файла, но каждое нечетное слово развернуть

file2 = open(r'crossplatformprogramming/5/besi2.txt', 'w')

with open(r'crossplatformprogramming/5/besi.txt', 'r', encoding='utf-8') as f:
    data = f.read().strip()

besi = list(map(str, data))
# print(besi)

pr1d6 = []
count = 0

while count < 16:
    for i in besi:
        if  i[len(i) - 1] == '.' or i[len(i) - 1] == '?':
            count += 1

