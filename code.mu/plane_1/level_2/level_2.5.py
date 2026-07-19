# Task 1 - Дана некоторая строка, например, вот такая: '023m0df0dfg0'. 
# Получите сет позиций всех нулей в этой в строке.
string1 = '023m0df0dfg0'
array1 = []
for i in range(len(string1)):
  if string1[i] == '0':
    array1.append(i)
result = set(array1)
print(result)

# Task 2 - Дана некоторая строка: 'abcdefg'. 
# Удалите из этой строки каждый третий символ. 
# В нашем случае должно получится следующее: 'abdeg'
string2 = 'abcdefg'
result = [string2[i] for i in range(len(string2)) if (i + 1) % 3 != 0]
print(''.join(result))

# Task 3 - Дан некоторый список, например, вот такой: [1, 2, 3, 4, 5, 6].
# Поделите сумму элементов, стоящих на четных позициях, на сумму элементов, стоящих на нечетных позициях.
string3 = [1, 2, 3, 4, 5, 6]
sum1 = sum(string3[i] for i in range(len(string3)) if i % 2 == 0)
sum2  = sum(string3[i] for i in range(len(string3)) if i % 2 != 0)
print(sum1 / sum2)

# Task 4 - Дана дата в следующем формате: ['2025', '12', '31'].
# Преобразуйте эту дату в следующий кортеж: ('31', '12', '2025')
array2 = ['2025', '12', '31']
print((array2[2], array2[1], array2[0]))