def abbrev_name(name):
    stroka = name.split(' ')
    return ((stroka[0])[:1] + "." + (stroka[1])[:1]).upper()

print(abbrev_name("Sam Harris"))
print(abbrev_name("Sam C"))