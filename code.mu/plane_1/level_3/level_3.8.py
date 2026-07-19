# Task 1 - Дан список со числами. 
# Проверьте, что все числа из этого списка содержат в себе цифру 3.
numbers = [13, 23, 33]
print(all('3' in str(num) for num in numbers))

# Task 2 - Через запятую написаны числа. 
# Получите максимальное из этих чисел.
numbers2 = 1, 2, 3, 4, 5
print(max(numbers2))

# Task 3 - Дана строка в формате:'kebab-case'.
# Преобразуйте ее в формат: 'snake_case'
string3 = 'hello-world'
print(string3.replace('-', '_'))

# Task 4 - Дана строка в формате: 'snake_case'.
# Преобразуйте ее в формат: 'camelCase'
string4 = 'hello_world'
print(string4.split('_' )[0] + ''.join(x.title() for x in string4.split('_' )[1:]))

# Task 5 - Дана строка в формате: 'camelCase'. Преобразуйте ее в формат: 'snake_case'
string5 = 'helloWorld'
print(''.join('_' + x.lower() if x.isupper() else x for x in string5))