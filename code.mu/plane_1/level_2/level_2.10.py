# Task 1 - Дана строка с буквами и цифрами. Проверьте, что в этой строке не более трех букв.
string1 = 'sdd123'
counter = 0
for x in range(len(string1)):
  if string1[x].isalpha():
    counter += 1
print(counter <= 3) 

# Task 2 - Дано число. Получите первую четную цифру с конца этого числа.
string2 = '123321'
for char in reversed(string2):
  if int(char) % 2 == 0:  
    print(char)
    break

# Task 3 - Дана некоторая строка: 'abcde abcde abcde'. 
# Замените в ней первый символ каждого слова на '!':'!bcde !bcde !bcde'
string3 = 'abcde abcde abcde'
print(' '.join('!' + x[1:] for x in string3.split()))

# Task 4 - Дан список со строками, содержащими целые числа: ['1', '2', '3', '4', '5']. 
# Найдите сумму элементов этого списка.
array1 = ['1', '2', '3', '4', '5']
print(sum(int(x) for x in array1))