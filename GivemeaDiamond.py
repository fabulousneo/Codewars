def diamond(n):
    s = ''
    if n % 2 != 0 and n > 0:
        for i in range(n + 1):
            if i % 2 != 0:
                s += ((n+1)-i)//2*" " + i*'*' + '\n'
        for i in reversed(range(n)):
            if i % 2 != 0:
                s += ((n+1)-i)//2*" " + i*'*' + '\n'
    else:
        return None
    return s

print(diamond(15))