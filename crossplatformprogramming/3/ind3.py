import re
def validate_email(email):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(email_pattern, email))
def main():
    while True:
        email = input("Input email: ")
        if validate_email(email):
            print(f"{email} — Accept.")
            break
        else:
            print("Incorrect. Try again.")
if __name__ == "__main__":
    main()
