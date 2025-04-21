str = str(input('Input a string: '))
print(f'b:   {str[2]}')
print(f'c:   {str[-2]}')
print(f'd:   {str[:5]}')
print(f'e:   {str[0:len(str) - 2]}')
sim = []
for i in range(len(str)):
    if i % 2 == 0:
        sim.append(str[i]) 
print(f'f:  {sim}')
sim.clear()
for i in range(len(str)):
    if i % 2 != 0:
        sim.append(str[i]) 
print(f'g:  {sim}')
print(f'h:  {str[::-1]}')
sim.clear()
i = 1
while i <= len(str):
    sim.append(str[-i])
    i += 2
print(f'i:  {sim}')
print(f'j:  {len(str)}')