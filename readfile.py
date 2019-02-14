with open('text.txt') as f:
    arr = [''.join(row.split()) for row in f]

comb = []
for i in arr:
    comb.append([i[j:j + 2] for j in range(0, len(i), 2)])
