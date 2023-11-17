def parts_sums(ls):
    result = [sum(ls)]
    for item in ls:
        result.append(result[-1]-item)
    return result

print(parts_sums([744125, 935, 407, 454, 430, 90, 144] * 10))