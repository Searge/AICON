with open('text.txt') as f:
    array = [row.split() for row in f]

permutl = []
for lst in array:
    for word in lst:
        lst_of_two = [word[letter:letter + 2]
                      for letter in range(0, len(word), 2)]
        for double in lst_of_two:
            a, b = double
            permutl.extend([b, a])

# print(array)
lst_of_four = [permutl[i:i+4] for i in range(0, len(permutl), 4)]
# Склеюємо значення по 4 в окремий список
for i in [j for j in lst_of_four]:
    print(i)
