def swap_each2numbers(x, y):
    x, y = y, x


with open('text.txt') as f:
    array = [row.split() for row in f]

print(array)

s = 'Lorem ipsum dolore'
wds = []
n = 2

for letter in ''.join(s.lower().split()):
    wds.append([letter[_:_ + n] for _ in range(0, len(letter), n)])

print(''.join(s.lower().split()))
