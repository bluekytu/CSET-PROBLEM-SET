import random


n = str(input())

NO_OF_CHARS = 256




def canFormPalindrome(st):

    count = [0] * (NO_OF_CHARS)


    for i in range(0, len(st)):
        count[ord(st[i])] = count[ord(st[i])] + 1

    odd = 0

    for i in range(0, NO_OF_CHARS):
        if (count[i] & 1):
            odd = odd + 1

        if (odd > 1):
            return False

    return True

count_of_tries = 0
while True:
    if canFormPalindrome(n) == False:
        print("NO SOLUTION")
        break
    else:
        count_of_tries = count_of_tries + 1
        str_list = list(n)

        n = ''.join(random.sample(str_list, len(str_list)))
        if n == n[::-1]:
            print(n)
            break

