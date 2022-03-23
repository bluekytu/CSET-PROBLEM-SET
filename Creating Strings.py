import itertools
n = str(input())
numbersof = (len(n) - 1 + 1)
numbers = [numbersof]
words = []

letters = list(n)


def uniqueCharacters(st):
    st = sorted(st)

    for i in range(len(st) - 1):


        if (st[i] == st[i + 1]):
            return False

    return True


    return True;
a = [''.join(items) for items in itertools.combinations_with_replacement(letters, r=numbersof)]
a = list(dict.fromkeys(a))
for i in a:
    if "a" not in i:
        print(i)
        if uniqueCharacters(i) == False:
            a.remove(i)


print(len(a))
print(a)

