# N = int(input("Введите количество холодильников: "))
# refregerators = []
# for i in range(N):
#     refregerators.append(str(input()))
# print("Заражены холодильники с номерами: ")
# for i in range(N):
#     if refregerators[i].find('a') != -1:
#         if refregerators[i].find('n', refregerators[i].find('a')) != -1:
#             if refregerators[i].find('t', refregerators[i].find('n')) != -1:
#                 if refregerators[i].find('o', refregerators[i].find('t')) != -1:
#                     if refregerators[i].find('n', refregerators[i].find('o')) != -1:
#                         print(i + 1, end= " ")
# print()


for i in range(int(input())):
    s, virus, x = input(), 'anton', 0
    for sym in s:
        if sym == virus[x]:
            x += 1
        if x == 5:
             print(' Холодильник с заражением: ', i + 1 )
             break
