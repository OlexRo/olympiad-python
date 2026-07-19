# Task 1 - С помощью цикла заполните список целыми числами от 1 до 10.
array1 = []
for x in range(1, 11):
  array1.append(x)
print(array1)

# Task 2 - Дана строка с буквами. 
# Проверьте, что в этой строке не более двух заглавных букв.
string1 = 'fsFEfd'
count = 0
for i in range(len(string1)):
  if string1[i].isupper():
    count += 1
print(count <= 2) 

# Task 2 - Дан список со строками, содержащими целые числа: ['1', '2', '3', '4', '5'].
# Преобразуйте элементы этого списка в числа: [1, 2, 3, 4, 5].
string2 = ['1', '2', '3', '4', '5']
print([int(x) for x in string2])