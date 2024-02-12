from math import sqrt;

def is_square(n):
    return n > -1 and sqrt(n) % 1 == 0

print(is_square(0))