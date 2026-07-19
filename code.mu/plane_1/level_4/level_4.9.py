# Task 1 - Сформируйте с помощью циклов следующий список: 
# [[1, 2, 3], [4, 5, 6], [7, 8, 9],]
result = [list(range(i, i + 3)) for i in range(1, 10, 3)]
print(result)

# Task 2 - Дан текст: '''a-1 b-2 c-3 d-4 e-5'''.
# Разбейте эту строку в словарь следующим образом: 
# {'a': 1 'b': 2 'c': 3 'd': 4 'e': 5}
string1 = '''
	a-1
	b-2
	c-3
	d-4
	e-5
'''
result = {
  x.strip().split('-')[0]: int(x.strip().split('-')[1]) for x in string1.strip().splitlines() if x.strip()
}
print(result)