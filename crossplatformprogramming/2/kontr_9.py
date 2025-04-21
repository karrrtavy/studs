def get_user_age():
    while True:
        try:
            age = int(input('Input your age: '))
            return age
        except ValueError:
            print('Input an integer')

def preferences(age):
    if 0 <= age < 7:
        print('Вам в детский сад')
    elif 7 <= age < 18:
        print('Вам в школу')
    elif 18 <= age < 25:
        print('Вам в профессиональное учебное заведение')
    elif 25 <= age < 65:
        print('Вам на работу')
    elif 65 <= age < 120:
        print('Вам предоставляется выбор')

def main():
    print('Age preference')

    while True:
        age = get_user_age()
        preferences(age)

if __name__ == '__main__':
    main()