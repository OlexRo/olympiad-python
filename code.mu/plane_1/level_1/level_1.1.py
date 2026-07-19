# Task 1 - Дано число. Проверьте, отрицательное оно или нет.
number1 = 1
if number1 < 0:
  print("Even number")
else:
  print("Odd number")

# Task 2 - Дана строка. Выведите в консоль длину этой строки.
string1 = "Hello"
print(len(string1))

# Task 3 - Дана строка. Выведите в консоль последний символ строки.
string2 = "Hello"
print(string1[-1])
# or print(string1[len(string1) - 1])

# Task 4 - Дано число. Проверьте, четное оно или нет.
number2 = 1
if number2 % 2 == 0:
  print("Even number")
else:
  print("Odd number")

# Task 5 - Даны два слова. Проверьте, что первые буквы этих слов совпадают.
string3 = "Hello"
string4 = "Hello"
if string3[0] == string4[0]:
  print("first lettres are equals")
else:
  print("first lettres are not equals")
# or if string4.startswith(string3[0]):
