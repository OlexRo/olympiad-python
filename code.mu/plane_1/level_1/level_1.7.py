# Task 1 - Дан словарь: {'a': 1, 'b': 2, 'c': 3, 'd': 4,}.
# Найдите сумму элементов этого словаря.
data1 = {
	'a': 1,
	'b': 2,
	'c': 3, 
	'd': 4,
}
sum1 = 0
for v in data1.values():
  sum1 += v
print(sum1)
# or result = sum(data1.values())

# Task 2 - Дан словарь: {'a': 1,'b': 2,'c': 3, 'd': 4,}.
# Найдите сумму квадратов элементов этого словаря.
data2 = {
	'a': 1,
	'b': 2,
	'c': 3, 
	'd': 4,
}
sum2 = 0
for v in data2.values():
  sum2 += v**2
print(sum2)
# or print(sum(v**2 for v in data2.values()))

#Task 3 - Дана строка: 'abcde'. Получите список букв этой строки.
string1 = 'abcde'
print(list(string1))

#Task 4 - Дана строка: 12345. Получите список цифр этого числа.
number1 = 12345
print(list(map(int, str(number1))))

#Task 5 - Дана строка: 12345. Переверните его: 54321.
number2 = 12345
print(str(number2)[::-1])

#Task 6 - Дана строка: 12345. Найдите сумму цифр этого числа.
number3 = 12345
print(sum(map(int, str(number3))))