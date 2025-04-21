marks = [int(i) for i in range(6)]

for i in range(len(marks)): marks[i] = int(input('Input a ticket`s number: '))
print(f'Your ticket: {marks}')

sum1 = 0
sum2 = 0

for i in range(len(marks[:3])): sum1 += marks[i]
for i in range(len(marks[3::])): sum2 += marks[i]

print('Yuo`re lucky!') if sum1 == sum2 else print('Try again')