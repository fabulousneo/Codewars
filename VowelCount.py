def get_count(sentence):
    count = 0
    for sym in sentence:
        if 'a' == sym or 'o' == sym or 'u'== sym or 'i' == sym or 'e' == sym:
            count += 1
    return print(count)

get_count("abracadabra")