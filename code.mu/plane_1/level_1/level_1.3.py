# Task 1 - Дана строка. Если в этой строке более одного символа, 
# выведите в консоль предпоследний символ этой строки.
string1 = "Hello"
if len(string1) > 1:
  print(string1[-2])
else:
  print("there are 0 characters in the line")

# Task 2 - Даны два целых числа. 
# Проверьте, что первое число без остатка делится на второе.
number1 = 2
number2 = 3
if number1 % number2 == 0:
  print("the first number is divisible by the second without a remainder")
else:
  print("the first number is divisible by the second with a remainder")

# Task 3 - Дана некоторая строка: 'abcde'. 
# Получите список ее символов: ['a', 'b', 'c', 'd', 'e']
string2 = 'abcde'
print(list(string2))

# Task 4 - Дан список: [1, 2, 3, 4, 5, 6]. 
# Получите из него следующий срез: [3, 4, 5]
array1 = [1, 2, 3, 4, 5, 6]
print(array1[2:5])

# Task 5 - Дан словарь с датой: {'year' : '2025', 'month': '12','day'  : '31',}.
# Из элементов этого словаря соберите дату в следующем формате: '2025-12-31'
data = {
	'year' : '2025',
	'month': '12',
	'day'  : '31',
}
print(f"{data['year']}-{data['month']}-{data['day']}")