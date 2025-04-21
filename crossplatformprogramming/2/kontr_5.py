lst = input('Input another symbol: ').split()
lst = [int(i) if i.isdigit() else i for i in lst]

min = 0
max = 0

for i in range(len(lst)):
    if lst[i] < lst[min]:
        min = i
    if lst[i] > lst[max]:
        max = i

lst[min], lst[max] = lst[max], lst[min]
print("List after some changes:", lst)

unique_elements = set(lst)
count_repeats = sum(lst.count(el) > 1 for el in unique_elements)
print("Doubles:", count_repeats)
