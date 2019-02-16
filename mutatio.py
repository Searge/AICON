from itertools import permutations

array = [['веле', 'лелю', 'лювю', 'вюве'],
         ['жежю', 'вілі']]

mutatio = []
out = open('new.txt', 'w')

for elem in array:
    mutatio.append(list(permutations(elem)))
    for item in mutatio:
        for tup in item:
            out.write(' '.join(tup))
            out.write('\n')

out.close()
# print(mutatio)
