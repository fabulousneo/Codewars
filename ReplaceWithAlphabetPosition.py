import re;

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def alphabet_position(text):
    s = ''
    for i in text:
        if re.match('[a-z]', i.lower()):
            s = f"{s} {str(alphabet.index(i.lower()) + 1)}"
        elif i == ' ':
            continue
        else:
            continue
    return s[1:]
             

print(alphabet_position('The most popular'))