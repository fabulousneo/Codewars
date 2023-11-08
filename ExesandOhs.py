def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')

print(xo('xxoo'))
print(xo('zzoo'))
print(xo('Xxoo'))