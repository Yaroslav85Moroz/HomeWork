num1 = float(input('Введите число под номером 1: '))
num2 = float(input('Введите число под номером 2: '))
num3 = float(input('Введите число под номером 3: '))

plus1 = num1>0
plus2 = num2>0
plus3 = num3>0
plus = plus1+plus2+plus3

minus1 = num1<0
minus2 = num2<0
minus3 = num3<0
minus = minus1+minus2+minus3

print(f'Из трёх введённых чисел {plus} положительных и {minus} отрицательных')