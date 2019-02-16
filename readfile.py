with open('text.txt') as f:
    array = [row.split() for row in f]

print(array)

for item in array:
    print(' '.join(item))
