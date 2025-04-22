import os
f = open(r'crossplatformprogramming/5/deti.txt', 'r', encoding='utf-8')
childrens = []
for line in f:
    parts = line.strip().split()
    surname, name, age, strage = parts[0], parts[1], int(parts[2]), parts[3]
    childrens.append((surname, name, age, strage))
f.close()
f2 = open(r'crossplatformprogramming/5/newfileind3.txt', 'w', encoding='utf-8')
f2.write(str(min(childrens)))
f2.write(str(max(childrens)))
os.rename(r'crossplatformprogramming/5/deti.txt', r'crossplatformprogramming/5/detskiysad.txt')