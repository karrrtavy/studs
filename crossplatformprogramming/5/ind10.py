# первые 16 предложений записать во второй файл. нужно посчитать кол-во гласных и кол-во согласных и вывести их кол-во.
# в новый файл записать предложения из 1 файла, но каждое нечетное слово развернуть, какой-то файл переименовать

with open(r'crossplatformprogramming/5/besi.txt', 'r', encoding='utf-8') as file1:
    data = file1.read().strip()

besi = data

with open(r'crossplatformprogramming/5/besi2.txt', 'r+', encoding='utf-8') as file2:
    count = 0
    for word in besi:
        file2.write(word)
        if  word[len(word) - 1] == '.' or word[len(word) - 1] == '?':
            count += 1
        if count == 16:
            break
    
    file2.seek(0)
    besi2 = file2.read().strip()
    glas_dict = 'аАуУоОыЫэЭяЯюЮёЁиИеУ'
    sogl_dict = 'бБвВгГдДжЖзЗйЙкКлЛмМнНпПрРсСтТфФхХцЦчЧшШщЩ'
    glas, sogl = [], []
    for word in besi2:
        for char in word:
            if char in glas_dict:
                glas.append(char)
            elif word in sogl_dict:
                sogl.append(char)
    print(f'кол-во гласных: {len(glas)}')
    print(f'кол-во согласных: {len(sogl)}')
    # import os
    # os.rename(r'crossplatformprogramming/5/besi2.txt', r'crossplatformprogramming/5/tepernebesi2.txt')    100% что будет переименован

with open(r'crossplatformprogramming\5\reverseword.txt', 'w', encoding='utf-8') as file3:
    i = 1
    for word in besi.split():
        if i % 2 != 0:
            file3.write(word[::-1])
        else:
            file3.write(word)
        file3.write(' ')
        i += 1