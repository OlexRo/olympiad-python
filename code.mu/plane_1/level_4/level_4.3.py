# Task 1 - Дан список. Удалите из него каждый пятый элемент.
array1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print([x for i, x in enumerate(array1) if (i + 1) % 5 != 0])

# Task 2 - Даны два числа. Получите список общих делителей этих чисел.
number1 = 12
number2 = 5
print([x for x in range(1, min(number1, number2)) if number1 % x == 0 and number2 % x == 0])

# Task 3 - Даны два числа: txt1 = 12345, txt2 = 45678.
# Получите кортеж цифр, которые есть и в одном, и в другом числе: (4, 5).
txt1 = 12345
txt2 = 45678
my_set = set(str(txt1)) & set(str(txt2))
print(tuple(int(x) for x in my_set))

# Task 4 - Дан список. Найдите сумму элементов этого списка.
array2 = [
	[
		[11, 12, 13],
		[14, 15, 16],
		[17, 17, 19],
	],
	[
		[21, 22, 23],
		[24, 25, 26],
		[27, 27, 29],
	],
	[
		[31, 32, 33],
		[34, 35, 36],
		[37, 37, 39],
	],
]
print(sum(sum(sum(row) for row in deep_array) for deep_array in array2))