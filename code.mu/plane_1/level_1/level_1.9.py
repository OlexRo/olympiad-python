# Task 1 - Дана строка: 'abcdef'. 
# Получите три последних символа этой строки: 'def'
string1 = 'abcdef'
print(string1[-3:])

# Task 2 - Дан словарь с числами: {'a': 1,'b': 2,'c': 3, 'd': 4,}.
# Увеличьте каждое число из словаря в 2 раза: {'a': 2,'b': 4,'c': 6, 'd': 8,}
data1 = {
	'a': 1,
	'b': 2,
	'c': 3, 
	'd': 4,
}
result = { key: value * 2 for key, value in data1.items() }
print(result)