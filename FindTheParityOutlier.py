import random

def find_outlier(integers):
    one = random.randint(0, len(integers) - 1)
    two = random.randint(0, len(integers) - 1)
    while True:
        if integers[one] % 2 == 0 & integers[two] % 2 == 0:
            for i in integers:
                if i % 2 != 0:
                    print(i)
                    break
        else:
            for i in integers:
                if i % 2 == 0:
                    print(i)
                    break
            


print(find_outlier([2,6,8,200,700,1,84,10,4]))