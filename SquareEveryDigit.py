def square_digits(num):
    nums = list(map(int, [char for char in str(num)]))
    return int(''.join(map(str, [num*num for num in nums])))

print(square_digits(765))
