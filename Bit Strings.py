import itertools

limit = input()

bit_strings = []

letters = ["1", "0"]
limit_list = []
limit_list.append(limit)
for x in limit_list:
    bit_strings.extend([''.join(y) for y in itertools.product(letters, repeat=(int(x)))])
print(len(bit_strings))