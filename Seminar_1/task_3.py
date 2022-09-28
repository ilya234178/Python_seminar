from tkinter import N


# напишите программу которая будет принимать на вход число N 
# и выводить числа от -N до N

N = int(input('Введите число :'))

num = -N
while (num <= N):
    print(num , end = " ")
    num += 1

