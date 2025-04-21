FIO = str(input('Input your SNP: '))
print(f'min: {min(FIO.split(), key=len)}')
print(f'max: {max(FIO.split(), key=len)}')