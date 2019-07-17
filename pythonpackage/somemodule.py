def create(alphabet_letter):
    if not alphabet_letter.isalpha() or not alphabet_letter.isupper():
        raise Exception()

    top = []
    for x in range(ord('A'), ord(alphabet_letter) + 1):
        last_len = 0 if len(top) is 0 else len(top[-1])
        top.append(create_line(x, last_len))
    
    return mirror(pad_lines(top))

def create_line(index, last_length):
    if index is ord('A'): return 'A'
    return chr(index) + (" " * last_length) + chr(index)

def pad_lines(top):
    max_width = len(top[-1])
    for x in range(len(top)):
        space_count = int((max_width - len(top[x])) / 2)
        top[x] = (" " * space_count) + top[x] + (" " * space_count)
    return top

def mirror(half):
    mirrored = half.copy()
    mirrored.reverse()
    mirrored.pop(0)
    return half + mirrored