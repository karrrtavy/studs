with open(r'crossplatformprogramming/5/ind5.txt', 'r', encoding='utf-8') as file:
    lines = [line.strip() for line in file]
filtered_lines = [line for line in lines if line]
print(filtered_lines)