from itertools import permutations

array = [[11, 22, 33, 44], [55, 66], [77, 88, 99, 00, 10, 11]]

mutatio = []

for elem in array:
    mutatio.append(list(permutations(elem, len(elem))))
