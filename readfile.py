with open('svg_text.txt', 'r') as f:
    array = [row.strip().split() for row in f]

print(array)
