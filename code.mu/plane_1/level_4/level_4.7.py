# Task 1 - Дан список со числами. Проверьте, что в нем есть число, 
# содержащее в себе цифру 3.
array1 = [1, 44, 55, 44, 636]
print(any(x for x in array1 if '3' in str(x)))

# Task 2 - Дана следующая структура. 
# Найдите сумму элементов этой структуры.
lst = [
	{
		1: (1, 2, 3),
		2: (1, 2, 3),
		3: (1, 2, 3),
	},
	{
		1: (1, 2, 3),
		2: (1, 2, 3),
		3: (1, 2, 3),
	},
	{
		1: (1, 2, 3),
		2: (1, 2, 3),
		3: (1, 2, 3),
	},
];
total = 0
for value in lst:
  for value2 in value.values():
    for value3 in value2:
      total += value3
print(total)
# or total = sum(sum(t) for d in lst for t in d.values())

# Task 3 - Дан список. Сделайте из этого списка строку так, 
# чтобы каждый элемент списка был на новой линии.
array2 = [
	'text1',
	'text2',
	'text3',
	'text4',
	'text5',
]
print('\n'.join(array2))