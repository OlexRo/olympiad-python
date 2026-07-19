# Task 1 - Найдите сумму всех целых чисел от 1 до 100.
result = 0
for i in range(1, 101):
  result+=i
print(result)
# or result = n * (n + 1) // 2

# Task 2 - Найдите сумму всех целых четных чисел в промежутке от 1 до 100.
result = 0
for i in range(2, 101, 2):
  result+=i
print(result)

# Task 3 - Найдите сумму всех целых нечетных чисел в промежутке от 1 до 100.
result = 0
for i in range(1, 101, 2):
  result+=i
print(result)

# Task 4 - Даны два целых числа. Найдите остаток от деления первого числа на второе.
number1 = 3
number2 = 2
print(number1 % number2)

# Task 5 - Дан список: [1, 2, 3, 4, 5, 6]. 
# Получите из него каждый второй элемент: [1, 3, 5]
array1 = [1, 2, 3, 4, 5, 6]
array2 = array1[::2]
print(array2)