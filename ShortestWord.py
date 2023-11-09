def find_short(s):
    return len(min(s.split(' '), key=len))

print(find_short("bitcoin take over the world maybe who knows perhaps"))