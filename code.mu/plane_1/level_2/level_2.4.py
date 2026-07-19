# Task 1 - Дана некоторая строка с буквами и цифрами. 
# Получите позицию первой цифры в этой строке.
string1 = 'adasd2123ads'
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
for i in range(len(string1)):
    for j in range(len(numbers)):
      if string1[i] == numbers[j]:
        print(f"Position: {i}")
        break
    else:
      continue
    break

# Task 2 - Дано число. Выведите в консоль количество четных цифр в этом числе.
number = 1232
number_array = list(str(number))
result = 0
for x in number_array:
  if int(x) % 2 == 0:
    result += 1
print(result)
# or result = sum(1 for x in str(number) if int(x) % 2 == 0)

# Task 3 - Дан словарь: {'a': 1,'b': 2,'c': 3,'d': 4,}. 
# Получите список его ключей: ['a', 'b', 'c', 'd']
data1 = {
	'a': 1,
	'b': 2,
	'c': 3, 
	'd': 4,
}
print(list(data1.keys()))

# Task 4 - Дана некоторая строка: 'abcde'. 
# Переведите в верхний регистр все нечетные буквы этой строки. 
# В нашем случае должно получится следующее: 'AbCdE'
string2 = 'abcde'
print(string2.upper())

# Task 5 - Дана некоторая строка со словами: 'aaa bbb ccc'.
# Сделайте заглавным первый символ каждого слова в этой строке. 
# В нашем случае должно получится следующее:'Aaa Bbb Ccc'
array1 = 'aaa bbb ccc'
result = array1.title()
print(result)

# Task 6 - Дана дата в следующем формате: '2025-12-31'.
# Преобразуйте эту дату в следующий кортеж: ('31', '12', '2025')
string3 = '2025-12-31'
string3_split = string3.split('-')
print((string3_split[2], string3_split[1], string3_split[0]))