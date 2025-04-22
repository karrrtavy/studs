with open(r'crossplatformprogramming/5/input.txt', 'r') as f:
    data = f.read().strip()
print(data)
nums = list(map(int, data.split()))
proc = 1
for num in nums:
    proc *= num
print(proc)