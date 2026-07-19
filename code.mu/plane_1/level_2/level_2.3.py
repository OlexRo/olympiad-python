# Task 1 - Даны два слова. Проверьте, что последняя буква 
# первого слова совпадает с первой буквой второго слова.
string1 = 'Hello'
string2 = 'Hello'
print([string1[1] == string2[1]])

# Task 2 - Дана некоторая строка. Найдите позицию третьего нуля в строке.
string3 = '000'
counter = 0
for i in range(len(string3)):
  if string3[i] == '0':
    counter += 1
    if counter == 3:
      print(f"third position 0: {i}")
      break

# Task 3 - Даны числа, разделенные запятыми: '12,34,56'. Найдите сумму этих чисел.
string4 = '12,34,56'
print(sum([int(x) for x in string4.split(',')]))

# Task 4 - Дана дата в следующем формате: '2025-12-31'. 
# Преобразуйте эту дату в следующий словарь: {'year' : '2025','month': '12','day'  : '31',}
string4 = '2025-12-31'
string4_split = string4.split('-')
result = {'year': string4_split[0], 'month': string4_split[1], 'day': string4_split[2]}
print(result)

# Task 5 - Дан словарь: {'a': 1,'b': 2,'c': 3, 'd': 4,}. Получите сет его значений: {1, 2, 3, 4}
data1 = {
	'a': 1,
	'b': 2,
	'c': 3, 
	'd': 4,
}
print(list(data1.values()))