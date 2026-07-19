from datetime import datetime, date

# Task 1 - Попросите пользователя ввести свой email. 
# Проверьте, ввел ли он корректное значение.
email = input("Enter your email...")
if '@' in email and '.' in email:
  print("Email is correct")
else:
  print("Email isn't correct")

# Task 2 - Попросите пользователя ввести дату в формате год-месяц-день. 
# Определите, была уже дата в текущем году.
my_date = input("Enter the date in 'year-month-day' format...")
try:
  check_date = datetime.fromisoformat(my_date).date()
  current_date = date.today()
  if check_date <= current_date:
    print("This date has already passed this year")
  else:
    print("This date has not yet arrived this year")
except ValueError:
  print("Error: incorrect date")

# Task 2 - Дан некоторый список, например, вот такой: [123, 456, 789].
# Слейте все элементы этого списка в один список, разбив их посимвольно:
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
array1 = [123, 456, 789]
print([int(y) for x in array1 for y in str(x)])