number1 = float(input('Введите первое число: '))
action = input('Укажите действие: ')
number2 = float(input('Введите второе число: '))

if action == '-':
    print(number1 - number2)
if action == '+':
    print(number1 + number2)
if action == '*':
    print(number1 * number2)
if action == '/':
    print(number1 / number2)
