def highest_rank(arr):
    highest = []
    maximum = []
    for i in arr:
        if arr.count(i) > 1 and i not in highest:
            highest.append(i)
    
    if highest == []:
        return max(arr)
    
    for i in highest:
        maximum.append(arr.count(i))
        
    if len(set(maximum)) == 1:
        return max(highest)
    
    return highest[maximum.index(max(maximum))]

print(highest_rank([1, 1, 5, 5, 3, 3, 2,2]))