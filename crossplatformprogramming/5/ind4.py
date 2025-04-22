with open(r'crossplatformprogramming/5/newfileind3.txt', 'r', encoding='utf-8') as file:
    for line in file:
        stripped_line = line.strip()  
        if stripped_line:  
            print(stripped_line)