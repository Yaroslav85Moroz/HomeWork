# text = input('Введите текст: ')
# number1 = text.count('о')
# number2 = text.count('й')
# print(number1, number2)


# text = 'ой ой ой 123'
# number1 = text.count('о')
# number2 = text.count('й')
# dictionary = {}
# print(number1, number2)


# number2 = text.count('и')
# # number = text.count('й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', 'э', 'я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю', 'ё')
# print(number1, number2)
#
# dictionary = {
#     'й': 'number1',
#     'ц': '1',
#     'у': '1',
#     'к': '1',
#     'е': '1',
#     'н': '1',
#     'г': '1',
#     'ш': '1',
#     'щ': '1',
#     'з': '1',
#     'ф': '1',
#     'ы': '1',
#     'в': '1',
#     'а': '1',
#     'п': '1',
#     'р': '1',
#     'о': '1',
#     'л': '1',
#     'д': '1',
#     'ж': '1',
#     'э': '1',
#     'я': '1',
#     'ч': '1',
#     'с': '1',
#     'м': '1',
#     'и': '1',
#     'т': '1',
#     'ь': '1',
#     'б': '1',
#     'ю': '1',
#     'ё': '1',
# }

# text = input('Введите текст: ')
# text1 = list(text)
# print(text1)

# text = list(input('Введите текст: '))
# text1 = [text for i in range(0, 3)]
# print(text1)

# dic = {символ строки = количество повторений}


# text = input('Введите текст: ')
# dic = {}
# for i in range(1, (text)+1):
#    dic[i] = text[i-1]
# print(dic)

# text = input('Введите текст: ')
# dic = {}
# for i in text:
#     if i in dic:
#         dic[i] += 1
#     else:
#         dic[i] = 1
# print(dic)

text = input('Введите текст: ')
dic = {i: text.count(i) for i in set(text)}
print(dic)