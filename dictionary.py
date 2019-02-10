svg_text = open('svg_text.txt', 'r')

# svg_text.write('', 'w')

with open('svg_text.txt', 'r') as f:
    array = [row.strip() for row in f]


with open('svg_text.txt', 'r') as f:
    for line in f.readlines():
        array.append(line.split())

x_ord = {
    'б': 1,
    'в': 2,
    'г': 3,
    'д': 4,
    'ж': 5,
    'з': 6,
    'к': 7,
    'л': 8,
    'м': 9}

y_ord = {
    'а': 1,
    'е': 2,
    'є': 3,
    'и': 4,
    'і': 5,
    'о': 6,
    'у': 7,
    'ю': 8,
    'я': 9}


# def letter_to_number(letters):
#     letters = letters.lower()
#     dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7,
#                   'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
#                   'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
#                   't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
#     strlen = len(letters)
#     if strlen == 1:
#         number = dictionary[letters]
#     elif strlen == 2:
#         first_letter = letters[0]
#         first_number = dictionary[first_letter]
#         second_letter = letters[1]
#         second_number = dictionary[second_letter]
#         number = (first_number * 26) + second_number
#     elif strlen == 3:
#         first_letter = letters[0]
#         first_number = dictionary[first_letter]
#         second_letter = letters[1]
#         second_number = dictionary[second_letter]
#         third_letter = letters[2]
#         third_number = dictionary[third_letter]
#         number = (first_number * 26 * 26) + (second_number * 26) + third_number
#     return number


svg_text.close()
