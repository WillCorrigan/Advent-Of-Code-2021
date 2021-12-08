decipher_output = []
solve_output = []

filename = "data.txt"
with open(filename) as f:
    content = f.readlines()

    for line in content:
        tmp_output = None
        tmp_decipher = None
        tmp_decipher, tmp_output = line.strip().split(" | ")
        solve_output.append(tmp_output.split(" "))
        decipher_output.append(tmp_decipher.split(" "))

letters = {'a': None, 'b': None, 'c': None, 'd': None, 'e': None, 'f': None, 'g': None}
numbers = {0: '', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}

def solve_letters(input):
        numbers[1] = "".join((filter(lambda x : len(x) == 2, input)))
        numbers[4] = "".join(filter(lambda x : len(x) == 4, input))
        numbers[7] = "".join(filter(lambda x : len(x) == 3, input))
        letters['a'] = "".join([letter for letter in numbers[7] if letter not in numbers[1]])
        numbers[8] = "".join(filter(lambda x : len(x) == 7, input))
        numbers[6] = "".join(filter(lambda x : len(x) == 6 and len("".join(set(numbers[1]+x))) == 7, input))
        letters['c'] = "".join([letter for letter in numbers[1] if letter not in numbers[6]])
        numbers[9] = "".join(filter(lambda x : len(x) == 6 and len([letter for letter in x if letter not in "".join(set(numbers[7]+numbers[4]))]) == 1, input))
        letters['e'] = "".join([letter for letter in numbers[8] if letter not in numbers[9]])
        letters['g'] = "".join([letter for letter in numbers[9] if letter not in "".join(set(numbers[7]+numbers[4]))])
        numbers[3] = "".join(filter(lambda x : len(x) == 5 and len([letter for letter in x if letter not in "".join(set(numbers[7]+letters['g']))]) == 1, input))
        letters['d'] = "".join([letter for letter in numbers[3] if letter not in "".join(set(numbers[7]+letters['g']))])
        letters['b'] = "".join([letter for letter in 'abcdefg' if letter not in "".join(set(numbers[3]+letters['e']))])
        numbers[0] = "".join(filter(lambda x : len(x) == 6 and letters['d'] not in x, input))
        numbers[5] = "".join(filter(lambda x : len(x) == 5 and letters['c'] not in x, input))
        numbers[2] = "".join(filter(lambda x : len(x) == 5 and x != numbers[5] and x != numbers[3], input))
        letters['f'] == "".join([letter for letter in numbers[8] if letter not in "".join(set(numbers[2]+letters['b']))])

        return numbers

answer_to_sum = []

for index, item in enumerate(solve_output):
    numbers = solve_letters(decipher_output[index])

    for key, value in numbers.items():
        numbers[key] = "".join(sorted(value))

    total = 0
    tmp_number = []

    for letter_combo in item:
        letter_combo = "".join(sorted(letter_combo))
        tmp_number.append(list(numbers.keys())[list(numbers.values()).index(letter_combo)])
        
    tmp_number = int("".join([str(x) for x in tmp_number]))
    total += tmp_number
    tmp_number = []
    answer_to_sum.append(total)


print(sum(answer_to_sum))

# letters in 0: a, b, c, e, f, g (d)
# letters in 1: c, f (a, b, d, e, g)
# letters in 2: a, c, d, e, g (b, f)
# letters in 3: a, c, d, f, g (b, e)
# letters in 4: c, f, d, b (a, e, g)
# letters in 5: a, b, d, f, g (c, e)
# letters in 6: a, b, d, e, f, g (c)
# letters in 7: c, f, a (b, d, e, g)
# letters in 8: a, b, c, d, e, f, g (none)
# letters in 9: a, b, c, d, f, g (e)

# b, d, e, f
# 0, 2, 3, 5, 9
# a = top line letter: 7-1
# 0, 9, 6 are len 6.
# 6 can be found if it doesn't contain all of 1
# this also identifies c = missing letter (8-6)
# 9 - (4 + a) = g

# unique: 1, 4, 7, 8
# len5: 2, 3, 5
# len6: 0, 6, 9

# 6 = not all 1 (finds c)
# 9 = 4 + 7 + 1 extra (g)
# 3 = 7 + g + 1 extra (d)
# 0 = 8 - len6 that doesn't contain d
# 5 = len5 that doesn't contain c (find e by adding c and minusing from 8)
# 2 = len 5 that isn't 3 or 5
