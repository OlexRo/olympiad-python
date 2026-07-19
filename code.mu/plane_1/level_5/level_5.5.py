from datetime import datetime, date

# Task 1 - Попросите пользователя ввести дату рождения в формате год-месяц-день. 
# Определите, сколько полных лет пользователю.
n1 = input("Enter your birthday date...")
try:
  birthday = datetime.fromisoformat(n1).date()
  today = date.today()
  age = today.year - birthday.year
  print(f"Your age: {age}")
except ValueError:
  print("Error: incorrect birthday date")

# Task 2 - Попросите пользователя ввести три числа. 
# Проверьте, что эти числа являются тройкой Пифагора: 
# квадрат самого большого числа должен быть равен сумме квадратов двух остальных.
n2 = int(input("Enter the first number..."))
n3 = int(input("Enter the second number..."))
n4 = int(input("Enter the third number..."))
numbers = [n2, n3, n4]
max_num = max(numbers)
numbers.remove(max_num)
if max_num ** 2 == numbers[0] ** 2 + numbers[1] ** 2:
  print("These numbers form a Pythagorean triple")
else:
  print("These numbers do not form a Pythagorean triple")

# Task 3 - Дано некоторое число: 35142. Отсортируйте цифры этого числа. 
# В нашем случае должно получится следующее: 12345.
string1 = 35142
print(''.join(x for x in sorted(str(string1))))