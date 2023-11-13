def scramble(s1, s2):
    for i in range(len(s2)):
        if s2[i] in s1:
           s1 = s1.replace(s2[i], '', 1)
        else:
           return False
    return True

def large_test():
        s1 = "rkqodlw"
        s2 = "world"
        print(scramble(s1, s2))

large_test()