print(list('ВоГУ'))

s = []
l = ['s', 'p', ['isok'], 2]
print(s)
print(l)

c = [c * 3 for c in 'list']
print(c)

c = [c * 3 for c in 'list' if c != 'i']
print(c)
c = [c + d for c in 'list' if c != 'i' for d in 'spam' if d != 'a']
print(c)