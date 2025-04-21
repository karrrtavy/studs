lst = list(range(20))
lst[0] = 1
lst[-1] = 1
for i in lst:
    if i >= 1 and i <=19:
        lst[i] = 0
print(lst)