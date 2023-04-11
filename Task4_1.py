# number1 = pow(2, 1)
# text = float(input('Введите степень числа: '))
# number2 = pow(number1, text)
# numbers = [number1, number2]
# print(numbers)
#
# text1 = [number1 for i in range(number2)]
# print(text1)
#
# text1 = [i for i in range(0, number2)]
# print(text1)

text = int(input('Введите степень числа: '))
text1 = [pow(2, i) for i in range(1, text)]
print(text1)

