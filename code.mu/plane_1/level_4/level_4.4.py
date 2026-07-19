# Task 1 - Дан список с числами. 
# Оставьте в нем только те числа, которые делятся на 5.
array1 = [1, 2, 4, 5, 6, 7, 9, 10]
print([x for x in array1 if x % 5 == 0])

# Task 2 - Дано число. Проверьте, 
# что у этого числа есть только один делитель, 
# кроме него самого и единицы.
number1 = 12
divisors = [i for i in range(2, number1) if number1 % i == 0]
result = len(divisors) == 1
print(result)

# Task 3 - Дан следующий словарь. Найдите сумму элементов этого словаря.
dct = {
	1: {
		1: 11,
		2: 12,
		3: 13,
	},
	2: {
		1: 21,
		2: 22,
		3: 23,
	},
	3: {
		1: 24,
		2: 25,
		3: 26,
	},
}
total = 0
for value1 in dct.values():
  for value2 in value1.values():
    total += value2
print(total)