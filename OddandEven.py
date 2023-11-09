def odd_or_even(arr):
    return 'even' if sum(arr) % 2 == 0 else 'odd'
        
print(odd_or_even([2, 3, 1]))
print(odd_or_even([2, 3, 2]))