# напишите программу которая будет принимать на вход дробь и показывать первую цифру дробной части числа


import math


n = float(input('Введите дробное число : '))
num_result = n*10
if num_result%10 == 0:
    print("no")
else:
    print(math.floor(num_result)%10)
