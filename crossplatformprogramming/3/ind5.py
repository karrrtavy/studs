def find_digits(input_string):
    digits = {}
    for char in input_string:
        if char.isdigit():
            digits[char] = digits.get(char, 0) + 1
    unique_digits = [char for char in digits if digits[char] == 1]
    if unique_digits:
        print("Уникальные цифры:", ', '.join(unique_digits))
    else:
        print("НЕТ")
input_string = input()
find_digits(input_string)