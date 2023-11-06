def high_and_low(numbers): 
    list_num = list(map(int, numbers.split(" ")))
    return f'{max(list_num)} {min(list_num)}'

print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))