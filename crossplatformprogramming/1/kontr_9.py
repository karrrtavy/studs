today = [2025, 2]

date_of_birth = input("Enter your date of birth with space-between, example (2004 9): ")
date = [int(i) for i in date_of_birth.split(' ') if i.isdigit()]
if today[1] != date[1]:
    print(f"Your age: {today[0] - date[0] - ((today[0], today[1]) > (date[0], date[1]))} years")
else:
        print(f"Your age: {today[0] - date[0] - ((today[0], today[1]) < (date[0], date[1]))} years")