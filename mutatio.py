from itertools import permutations

array = [['веле', 'лелю', 'лювю', 'вюве'],
         ['жежю', 'вілі']]

mutatio = []

for elem in array:
    mutatio.append(list(permutations(elem)))
    for item in mutatio:
        for tup in item:
            print(' '.join(tup))

# print(mutatio)
