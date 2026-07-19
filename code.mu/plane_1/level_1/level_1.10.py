# Task 1 - Дана строка: 'abcdef'
# Получите каждый второй символ этой строки: 'ace'
string1 = 'abcdef'
print(string1[::2])

# Task 2 - Дано некоторое число: 12345.
# Выведите в консоль все его символы с конца.
number1 = 12345
for c in str(number1)[::-1]:
  print(c, end='')