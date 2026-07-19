# Task 1 - Дан список с числами. 
# Оставьте в нем только те числа, которые содержат цифру ноль.
array = [10, 11, 20, 12]
print([x for x in array if '0' in str(x)])

# Task 2 - Дана следующая структура. 
# Найдите сумму элементов этой структуры.
lst = [
	{
		1: 11,
		2: 12,
		3: 13,
	},
	{
		1: 21,
		2: 22,
		3: 23,
	},
	{
		1: 24,
		2: 25,
		3: 26,
	},
];
total = 0
for value in lst:
  for value2 in value.values():
    total += value2
print(total)
# or total = sum(sum(d.values()) for d in lst)
# or total = sum(map(lambda d: sum(d.values()), lst))