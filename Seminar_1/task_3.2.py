# 3. Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

# a = input('введите строку 1 : ')
# b = input('введите строку 2 : ')

# print(a.count(b))

s = input('Введите первую строку: ')
s_1 = input('Введите вторую строку: ')

if len(s) > len(s_1):
 n = len(s_1)
else:
 n = len(s)


count = 0
for i in s:
 for j in s_1:
  if i == j:
   count += 1

print(count)
