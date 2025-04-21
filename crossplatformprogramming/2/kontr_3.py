FIO = (input('Input your SNP: '))
FIO = [str(i) for i in FIO.split()]
FIO.sort(key=len)
print(FIO)