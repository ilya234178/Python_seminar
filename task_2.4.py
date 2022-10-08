# транслитерация

alphabetE = \
    ['a', 'b', 'v', 'g', 'd', 'e', 'yo', 'zh', 'z', 'i','y', 'k', 'l', 'm', 'n', 'o', 'p', 'r',
    's', 't', 'u', 'f', 'kh', 'ts', 'ch', 'sh', 'shch', '`', 'bl', '\'', 'e', 'yu', 'ya']
alphabetR = \
    ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р',
     'с', 'т', 'у', 'ф','х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', '.', 'z']

base = input('Введите слово : ')
word = [] 

for i in range(len(base)):
    word.append(alphabetR.index(base[i]))
    index = word[i]
    print(alphabetE[index], end= '')
