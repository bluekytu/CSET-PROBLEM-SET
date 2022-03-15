import math
from itertools import count


board = [
["1", "2", "9", "10", "25"],
["4", "3", "8", "11", "24"],
["5", "6", "7", "12", "23"],
["16", "15", "14", "13", "22"],
["17", "18", "19", "20", "21"],
]
amount_of_test = int(input())
results = []
for i in range(amount_of_test):

    x_row, y_row = input().split()
    number = board[int(x_row) - 1][int(y_row) - 1]
    results.append(number)
for i in results:
    print(i)



#spiral = []
#starting_no = 1
#for i in count(0):
#    number = i
#    spiral.append(number)
#    print(spiral)