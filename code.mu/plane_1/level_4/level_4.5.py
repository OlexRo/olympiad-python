# Task 1 - Выведите в консоль все числа в промежутке от 10 до 1000, 
# у которых предпоследняя цифра четная.
print([x for x in range(10, 1001) if int(str(x)[-2]) % 2 == 0])

# Task 2 - Дана строка: '''text1 text2 text3 text4 text5'''.
# Разбейте эту строку в список так, 
# чтобы каждая непустая линия текста стала отдельным элементом списка: 
# ['text1','text2','text3','text4','text5',]
string1 = '''
	text1
	text2
	text3
	text4
	text5
'''
result = string1.split()
print(result)

# Task 3 - Дан следующий словарь. Найдите сумму элементов этого словаря.
dct = {
	1: {
		1: {
			1: 111,
			2: 112,
			3: 113,
		},
		2: {
			1: 121,
			2: 122,
			3: 123,
		},
	},
	2: {
		1: {
			1: 211,
			2: 212,
			3: 213,
		},
		2: {
			1: 221,
			2: 222,
			3: 223,
		},
	},
	3: {
		1: {
			1: 311,
			2: 312,
			3: 313,
		},
		2: {
			1: 321,
			2: 322,
			3: 323,
		},
	},
}
total = 0
for value1 in dct.values():
  for value2 in value1.values():
    for value3 in value2.values():
      total += value3
print(total)