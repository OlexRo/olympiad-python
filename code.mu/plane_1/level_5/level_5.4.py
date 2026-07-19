# Task 1 - Попросите пользователя ввести целое число через консоль. 
# Получите факториал введенного числа.
n1 = int(input("Enter the number..."))
if n1 < 0:
  print("The factorial is not defined from a negative number")
if n1 == 1 or n1 == 0: 
  print(f"The factorial: ", 1)
factorial = 1
for i in range(2, n1 + 1):
  factorial *= i
print(f"The factorial: {factorial}")

# Task 2 - Напишите программу, которая сформирует следующую строку: '-1-2-3-4-5-'.
print(''.join('-' + str(x) for x in range(1, 6)) + '-')

# Task 3 - Дана некоторая строка: '1 22 333 4444 22 5555 1'.
# Удалите из этой строки все подстроки, в которых количество символов больше трех. 
# В нашем случае должно получится следующее: '1 22 333 22 1'.
string1 = '1 22 333 4444 22 5555 1'
print(' '.join(x for x in string1.split(' ') if len(x) <= 3))
