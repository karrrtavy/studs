digits = input("Enter digits in space between: ")

array = [int(i) for i in digits.split(' ') if i.isdigit()]
print(array)
print(f"Max: {max(array)}, Min: {min(array)}")
