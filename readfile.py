import re

with open('svg_text.txt', 'r') as f:
    array = [row.strip().split() for row in f]

print(array)

re.findall(r"/[\w'._±]+@[\w'._±]+/", array)
