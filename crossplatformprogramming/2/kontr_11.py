import math, re


def input_factorial():
    while True:
        try:
            expression = str(input(('Input an expression: ')))
            return expression
        except Exception as e:
            print(f'Error: {e}')

def factorial(expression):
    if '!' in expression:
        match = re.search(r'!(\d+)', expression)
        if match:
            number = int(match.group(1))
            if number < 0:
                return 'Factorial`s number < 0'
            else:
                return math.factorial(number)
            
def main():
    while True:
        expression = input_factorial()
        result = factorial(expression)
        print(f'{expression} = {result}')

if __name__ == '__main__':
    main()
