import re

def printer_error(s):
    count = 0
    for i in s:
        if re.match('[a-mA-M]', i):
            count += 1
        
    return f"{len(s) - count}/{len(s)}"

print(printer_error('afjbafahfhafafmbnb,.;e'))
    
