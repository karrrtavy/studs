text = input("Enter the text: ")
text = text.lower()

retext = ''.join(text.split())
test = ''.join(reversed(retext))
if test == retext:
    print("palindrom")
else:
    print("isn't palindrom")
