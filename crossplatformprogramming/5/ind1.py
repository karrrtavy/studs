with open(r'crossplatformprogramming/5/input.txt', 'r') as f:
    data = f.read().strip()
nums = list(map(int, data.split()))
proc = 1
for num in nums:
    proc *= num
with open(r'crossplatformprogramming/5/output.txt', 'w') as f:
    f.write(str(proc))
f = open(r'crossplatformprogramming/5/output.txt', 'r')
print(*f)