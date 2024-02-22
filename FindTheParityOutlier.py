def find_outlier(integers):
    even_values = [i for i in integers if i % 2 == 0]
    
    if len(even_values) > 1:
        for i in integers:
            if i % 2 != 0:
                return i
    else:
        return even_values[0]
        
print(find_outlier([2,6,8,10,3]))