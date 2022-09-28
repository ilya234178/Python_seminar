# напишите программу которая на вход принимает 5 чисел и находит максимальное из них


num1 = int(input('Введите число 1 :'))
num2 = int(input('Введите число 2 :'))
num3 = int(input('Введите число 3 :'))
num4 = int(input('Введите число 4 :'))
num5 = int(input('Введите число 5 :'))

arr = [num1,num2,num3,num4,num5]
numMax = num1

for i in arr :
 if numMax < i :
    numMax = i
print(f'Максимальное число : {numMax}')        


