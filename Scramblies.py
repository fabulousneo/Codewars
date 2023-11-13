def scramble(s1, s2):
    for i in range(len(s2)):
        if s2[i] in s1:
           s1 = s1.replace(s2[i], '', 1)
           continue
        else:
           return False
    return True

def large_test():
        s1 = "abcdefghijklmnopqrstuvwxyz" * 10_000
        s2 = "zyxcba" * 9_000
        print(scramble(s1, s2))

large_test()