with open('text.txt') as file:
    arr = [''.join(row.split()) for row in file]

comb = []
for sentence in arr:
    comb.append([sentence[letter:letter + 2] for letter in range(0,
                                                                 len(sentence),
                                                                 2)])

# Перевірка
print(arr, '\n', comb)
