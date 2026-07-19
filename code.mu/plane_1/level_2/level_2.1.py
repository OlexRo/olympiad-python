# Task 1 - Дан список со строками. Оставьте в этом списке только те строки, которые начинаются на http://.
array1 = ['http://one.ru', 'asdasd', 'http://two.tu',]
print([value for value in array1 if value.startswith('http://')])

# Task 2 - Дана некоторая строка. Найдите позицию первого нуля в строке.
string1 = '0ad012d0'
print(string1.find('0'))

# Task 3 - Дан список. Удалите из него элементы с заданным значением.
array2 = ['1', '2', '5', '4']
value_to_remove = '2'
print([value for value in array2 if value != value_to_remove])
# or array2 = list(filter(lambda x: x != value_to_remove, array2))

# Task 4 - Выведите в консоль все числа в промежутке от 10 до 1000, 
# сумма первой и второй цифры которых равна пяти.
print([x for x in range(10, 1001) if int(str(x)[0]) + int(str(x)[1]) == 5])

# Task 5 - Дана некоторая строка: 'abcdeabc'. Очистите ее от дублей символов: 'abcde'
string3 = 'abcdeabc'
result = ''.join(dict.fromkeys(string3))
print(result)