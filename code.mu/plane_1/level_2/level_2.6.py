# Task 1 - Дана некоторая строка с буквами и цифрами. 
# Получите список позиций всех цифр из этой строки.
string1 = '1fdfedf34'
array1 = []
for i in range(len(string1)):
  if string1[i].isdigit():
    array1.append(i)
print(array1)

# Task 2 - Дана некоторая строка: 'AbCdE'. 
# Смените регистр букв этой строки на противоположный. 
# В нашем случае должно получится следующее: 'aBcDe'.
string2 = 'AbCdE'
print(string2.swapcase())

# Task 3 - Дан некоторый список с числами, например, вот такой: [1, 2, 3, 4, 5, 6]. 
# Слейте пары элементов вместе: [12, 34, 56]
array2 = [1, 2, 3, 4, 5, 6]
print([int(str(array2[i]) + str(array2[i+1])) for i in range(0, len(array2), 2)])

# Task 4 - Дана некоторая строка со словами: 'aaa bbb ccc eee fff'.
# Сделайте заглавным первый символ каждого второго слова в этой строке. 
# В нашем случае должно получится следующее: 'aaa Bbb ccc Eee fff'
string3 = 'aaa bbb ccc eee fff'
words = string3.split(' ')
for i in range(1, len(words), 2):
  words[i] = words[i].title()
print(' '.join(words))