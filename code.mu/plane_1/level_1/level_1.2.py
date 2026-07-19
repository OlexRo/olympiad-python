# Task 1 - Дано число. Выведите в консоль первую цифру этого числа.
number1 = 12
print(str(number1)[0])

# Task 2 - Дано число. Выведите в консоль последнюю цифру этого числа.
number2 = 12
print(str(number1)[-1])

# Task 3 - Дано число. Выведите в консоль сумму первой и последней цифры этого числа.
number3 = 12
print(int(str(number3)[0]) + int(str(number3)[-1]))

# Task 4 - Дано число. Выведите количество цифр в этом числе.
number4 = 12
print(len(str(number4)))

# Task 5 - Даны два числа. Проверьте, что первые цифры этих чисел совпадают.
number5 = 22
number6 = 34
if str(number5)[0] == str(number6)[0]:
  print("first numbers are equals")
else:
  print("first numbers are not equals")

# Task 5 - Дан список: [1, 2, 3, 4, 5, 6]. Получите из него следующий срез: [1, 2, 3
array = [1, 2, 3, 4, 5, 6]
print(array[0:3])