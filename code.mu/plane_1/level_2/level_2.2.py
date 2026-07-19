# Task 1 - Дан список с числами. Подсчитайте количество отрицательных чисел в этом списке.
array1 = [1, -3, -4, -5, -0]
print(len([value for value in array1 if value < 0]))

# Task 2 - Дан список с числами. Оставьте в нем только положительные числа.
array2 = [1, -3, -4, -5, -0]
print(list(filter(lambda x: x > 0, array2)))
# or print([x for x in array2 if x > 0])

# Task 3 - Дана строка. Удалите предпоследний символ из этой строки.
string1 = 'Hello'
result = string1[0:3] + string1[-1:] 
print(result)

# Task 4 - Дан список со строками. Оставьте в этом списке только те строки, 
# которые заканчиваются на .html.
array3 = ['one.html', 'two.html', 'three.txt']
print([x for x in array3 if x.endswith('.html')])

# Task 5 - Дан список с дробями: [1.456, 2.125, 3.32, 4.1, 5.34]. 
# Округлите эти дроби до одного знака в дробной части.
array4 = [1.456, 2.125, 3.32, 4.1, 5.34]
print([round(x, 1) for x in array4])

# Task 6 - Дан словарь: {'a': 1, 'b': 2, 'c': 3, 'd': 4,}. 
# Получите список его значений: [1, 2, 3, 4]
data1 = {
	'a': 1,
	'b': 2,
	'c': 3, 
	'd': 4,
}
print([x for x in data1.values()])
# or print(list(data1.values()))