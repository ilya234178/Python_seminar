# НОД наибольший общий делитель


a = 100
b = 50

if a < b:
   a, b = b, a

while b != 0:
    a, b = b, a % b

print(a)
