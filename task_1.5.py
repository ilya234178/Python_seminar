# Объявите анонимную (лямбда) функцию для определения вхождения в переданную 
# ей строку фрагмента "plr".
#  То есть, функция должна возвращать True,
#  если такой фрагмент присутствует в строке и False - в противном случае.

# print((lambda x: 'prl' in x)(input()))  # решение в одну строку

contains = lambda s, sample= 'prl': sample in s
s  = input()
print(contains(s))