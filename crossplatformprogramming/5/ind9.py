# первые 16 предложений во второй файл. нужно посчитать кол-во гласных и кол-во согласных и вывести их кол-во.
# в новый файл записать предложения из 1 файла, но каждое нечетное слово развернуть

with open(r'crossplatformprogramming/5/besi.txt', 'r', encoding='utf-8') as f:
    data = f.read().strip()

besi = list(map(str, data))
# print(besi)

pr1d6 = []
count = 0

with open(r'crossplatformprogramming/5/besi2.txt', 'w', encoding='utf-8') as file2:    
    for i in besi:
        file2.write(i)
        if  i[len(i) - 1] == '.' or i[len(i) - 1] == '?':
            count += 1
        if count == 16:
            break

count = 0

with open(r'crossplatformprogramming/5/reverseword.txt', 'w', encoding='unt-8'):
    for i in besi:
        if count % 2 != 0:
            
