from datetime import datetime

# Task 1 - Попросите пользователя ввести два числа целых числа через консоль. 
# Заполните список целыми числами от минимального введенного числа 
# до максимального.
n1 = int(input("Enter the first number..."))
n2 = int(input("Enter the second number..."))
print(list(range(min(n1, n2), max(n1, n2) + 1)))

# Task 2 - Попросите пользователя ввести дату в формате год-месяц-день. 
# Определите день недели, соответствующий этой дате.
n3 = input("Enter the date in 'year-month-day' format...")
try:
  day_of_week = datetime.fromisoformat(n3)
  print(f"The day of the week: ", {day_of_week.strftime("%A")})
except ValueError:
  print("Error")

# Task 3 - Попросите пользователя ввести год. 
# Определите, високосный этот год или нет.
n4 = int(input("Enter the year..."))
if (n4 % 4 == 0 and n4 % 100 != 0) or (n4 % 400 == 0):
  print("Leap year")
else:
  print("The year is not a leap year")

# Task 4 - Напишите программу, которая сформирует следующую строку: '54321'.
print(''.join(str(x) for x in range(5, 0, -1)))

# Task 5 - Дан некоторый список, например, вот такой: [1, 2, 3, 4, 5, 6].
# Поменяйте местами пары элементов этого списка: [2, 1, 4, 3, 6, 5].
array1 = [1, 2, 3, 4, 5, 6]
result = []
for i in range(0, len(array1), 2):
  result.append(array1[i + 1])
  result.append(array1[i])
print(result)