# Task 1 - Дано некоторое число. 
# Проверьте, что цифры этого числа расположены по возрастанию.
number = 12345
digits = str(number)
print(all(digits[i] < digits[i + 1] for i in range(len(digits) - 1)))

# Task 2 - Дан список: [1, '', 2, 3, '', 5]. 
# Удалите из списка все пустые строки.
array1 = [1, '', 2, 3, '', 5]
print(list(filter(lambda x: x != '', array1)))
# or list(filter(None, array1)

# Task 3 - Дан список: [[1, 2, 3], [4, 5, 6], [7, 8, 9],].
# Выведите в консоль все элементы этого списка.
array2 = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9],
]
print([y for x in array2 for y in x])