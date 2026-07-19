# Task 1 - Дана строка. 
# Сделайте заглавной последнюю букву каждого слова в этой строке.
string1 = 'hello hello'
print(' '.join([x[:-1] + x[-1].upper() for x in string1.split(' ')]))

# Task 2 - Дана строка. 
# Проверьте, что эта строка состоит только из четных цифр.
string2 = '2 4 6 8 10'
print(all(int(x) % 2 == 0 for x in string2.split(' ')))

# Task 3 - Даны две строки: txt1 = '12345' txt2 = '45678'.
# Получите символы, которые есть и в одной, и в другой строке: '45'.
txt1 = '12345'
txt2 = '45678'
print(''.join(set(txt1) & set(txt2)))

# Task 4 - Дана некоторая строка: 'a bc def ghij'.
# Переведите в верхний регистр все подстроки, 
# в которых количество букв меньше или равно трем. 
# В нашем случае должно получится следующее: 'A BC DEF ghij'
string3 = 'a bc def ghij'
print(' '.join(x.upper() if len(x) <= 3 else x for x in string3.split()))
