# напишите программу которая принимает на вход два числа и проверяет
# является ли одно число квадратом другого

a = int(input('Введите число 1 :'))
b = int(input('Введите число 2 :'))
# if a*a == b:
#     print(f'{a},{b} -> да')
# elif b*b == a:
#      print(f'{a},{b} -> да')
# else:
#      print(f'{a},{b} -> нет')


if a**2 == b or b**2 == a : 
     print(f'{a},{b} -> да')
else:
     print(f'{a},{b} -> нет')