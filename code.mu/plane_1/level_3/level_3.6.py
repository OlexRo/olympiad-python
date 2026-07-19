# Task 1 - Дан список со числами. Удалите из него числа, состоящие более чем из трех цифр.
array1 = [123, 1234, 123]
print(list(filter(lambda x: len(str(x)) <= 3, array1)))
# or result = [x for x in array1 if len(str(x)) <= 3]

# Task 2 - Дана строка. Проверьте, что эта строка состоит только из цифр.
string2 = 'hello123'
print(all(x.isdigit() for x in string2)) 

# Task 3 - Дано число, например, вот такое: num = 12345.
# Проверьте, что все цифры этого числа больше нуля.
num = 12345
print(all(int(x) > 0 for x in str(num)))

# Task 4 - Даны два списка: lst1 = [1, 2, 3, 4, 5] st2 = [1, 2, 3].
# Проверьте, что все элементы первого списка есть во втором.
lst1 = [1, 2, 3, 4, 5]
lst2 = [1, 2, 3]
print(set(lst1).issubset(set(lst2)))