import math
import sys

n = int(input())

knights = ((n*n) -2)
board_fac = math.factorial(n*n)
knight_fac = math.factorial(knights)
su = board_fac // (knight_fac * math.factorial(2))



