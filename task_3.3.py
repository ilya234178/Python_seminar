# Задайте список. Напишите программу, которая определит,
#  присутствует ли в заданном списке строк некое число.

array = ['fjashfjasghglah342', '324324f23','q23fd23a', '23', 'sdas23']
number = 23
for word in array:
    if str(number) in word:
        print(True)
    else:
        print(False)
