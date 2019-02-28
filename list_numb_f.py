# Створюємо простий список
vectors = [i + 1 for i in range(10)]

# Ділимо на пари
lst_of_two = [vectors[i:i + 2] for i in range(0, len(vectors), 2)]

# lst_of_two
# [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]

permutl = []
# Перетасовуємо кожну пару
for i in lst_of_two:
    a, b = i
    permutl.append(b)
    permutl.append(a)

# permutl
# [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]

lst_of_four = [permutl[i:i+4] for i in range(0, len(permutl), 4)]
# Склеюємо значення по 4 в окремий список
for i in [j for j in lst_of_four]:
    print(i)

# [2, 1, 4, 3]
# [6, 5, 8, 7]
# [10, 9]

# Перетворюємо числові списки в окремі стрічкові рядки
for i in [j for j in lst_of_four]:
    print(''.join(map(str, i)))
