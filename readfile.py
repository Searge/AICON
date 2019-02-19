from itertools import permutations
import time
start = time.time()

# ЗМІНИТИ НАЗВУ ФАЙЛУ НА ПОТРІБНУ
with open('text.txt') as f:
    array = [row.split() for row in f]

mutatio = []
out = open('new.txt', 'w')

for lst in array:
    mutatio.append(list(permutations(lst)))
    for item in mutatio:
        for tup in item:
            out.write(' '.join(tup))
            out.write('\n')
out.close()

end = time.time()
print(f'Операція зайняла {end - start} секунд')
