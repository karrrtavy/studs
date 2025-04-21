s = 'У лукоморья 123 дуб зеленый'

for i in range(len(s)):
    if s[i] == 'я':
        print(f'a: буква \'я\' встречается на {i + 1} позиции')

count = 0
for i in range(len(s)):
    s = s.lower()
    if s[i] == 'у':
        count += 1
print(f'b: буква \'у\' встречается {count} раза')

if s.isalpha():
    print('c: No changes')
else:
    print(f'c: string after changes - {s.upper()}')

if len(s) > 4:
    print(f'd: string`s length = {len(s)} than > 4 so --> {s.lower()}')

s = [str(i) for i in s]
s[0] = 'О'
s = "".join(s)
print(f'e: {s}')