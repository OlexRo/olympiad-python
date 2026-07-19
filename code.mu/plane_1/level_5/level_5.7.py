from datetime import date, timedelta

# Task 1 - Попросите пользователя ввести свой номер телефона. 
# Проверьте, ввел ли он корректное значение.
my_number = input("Enter your number...")
cleaned_number = my_number.replace(" ", "").replace("-", "")
if cleaned_number.isdigit():
  print("Phone number is valid")
else:
  print("Phone number is NOT valid")

# # Task 2 - Попросите пользователя ввести десять чисел. 
# # Сохраните полученные числа в список, а затем получите 
# # среднее арифметическое этих чисел и выведите результат.
numbers = []
for i in range(10):
  num = int(input(f"Enter number {i+1}: "))
  numbers.append(num)
average = sum(numbers) / len(numbers)
print(f"Numbers: {numbers}")
print(f"Arithmetic mean: {average}")

# Task 3 - Выведите в консоль даты всех выходных дней текущего года в 
# формате год-месяц-день.
year = date.today().year
current_date = date(year, 1, 1)
while current_date.year == year:
  if current_date.weekday() in [5, 6]:
    print(current_date.isoformat())
  current_date += timedelta(days=1)