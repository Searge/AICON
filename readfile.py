import re

with open('svg_text.txt', 'r') as f:
    array = [row.strip().split() for row in f]

print(array)

re.findall(r"/[\w'._±]+@[\w'._±]+/", array)

array = []
with open('svg.txt') as f:
    array = [''.join(row.split()) for row in f]

        #for word in row:
            #array = [word.split()]

print(array)

array2 = []
for word in array:
    for i in word:
        array2.append(i)
    #array2 = word.split()

print(array2)
