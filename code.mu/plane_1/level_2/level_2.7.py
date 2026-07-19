# Task 1 - Дан символ. Узнайте, в каком регистре этот символ - в верхнем или нижнем.
char = 'A'
if char.isupper():
  print("Верхний регистр")
elif char.islower():
  print("Нижний регистр")
else:
  print("Не буква")

# Task 2 - Дано некоторое число, например, такое: 123789. 
# Удалите из этого числа все нечетные цифры. 
# В нашем случае получится такой результат: 28
number1 = 123789
number_str = str(number1)
result = ''.join(x for x in number_str if int(x) % 2 == 0)
print(int(result))

# Task 3 - Дан кортеж с датой: ('2025', '12', '31'). 
# Преобразуйте эту дату в следующий словарь: {'year' : '2025','month': '12','day'  : '31',}
tuple = ('2025', '12', '31')
print({'year': tuple[0], 'mouth': tuple[1], 'day': tuple[2]})