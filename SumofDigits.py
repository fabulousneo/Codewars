def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int, list(str(n)))))

print(digital_root(493193))