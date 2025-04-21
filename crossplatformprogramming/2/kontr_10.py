import math, re


def input_expression():
    while True:
        try:
            expression = str(input(('Input an expression: ')))
            return expression
        except Exception as e:
            print(f'Error: {e}')

class Calc:
    def calc(self, expression):
        try:
            result = eval(expression)
            return result
        except ZeroDivisionError:
            return 'Can`t divide by zero'
        except Exception as e:
            return f'Error: {e}'

    def function(self, expression):
        if 'sin' in expression:
            match = re.search(r'sin(\d+)', expression)
            if match:
                angle = float(match.group(1))
                return math.sin(math.radians(angle))
        if 'cos' in expression:
            match = re.search(r'cos(\d+)', expression)
            if match:
                angle = float(match.group(1))
                return math.cos(math.radians(angle))
        if 'tg' in expression:
            match = re.search(r'tg(\d+)', expression)
            if match:
                angle = float(match.group(1))
                return math.tan(math.radians(angle))
        if 'ctg' in expression:
            match = re.search(r'ctg(\d+)', expression)
            if match:
                angle = float(match.group(1))
                return 1 / math.tan(math.radians(angle))
        if '!' in expression:
            match = re.search(r'!(\d+)', expression)
            if match:
                number = int(match.group(1))
                if number < 0:
                    return 'Factorial`s number < 0'
                else:
                    return math.factorial(number)

def main():
    calculate = Calc()

    while True:
        expression = input_expression()
        if any(trig in expression for trig in ['sin', 'cos', 'tg', 'ctg', '!']):
            result = calculate.function(expression)
        else:
            result = calculate.calc(expression)
        print(f'{expression} = {result}')

if __name__ == '__main__':
    main()