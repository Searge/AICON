from itertools import permutations

with open('text.txt') as f:
    array = [row.split() for row in f]

mutatio = []
out = open('new.txt', 'w')

for elem in array:
    mutatio.append(list(permutations(elem)))
    for item in mutatio:
        for tup in item:
            out.write(' '.join(tup))
            out.write('\n')

out.close()
