def reverse_words(text):
    arr = text.split(' ')
    reverse = [s[::-1] for s in arr]
    return ' '.join(reverse)