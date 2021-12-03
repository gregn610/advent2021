eg = [
    'forward 5',
    'down 5',
    'forward 8',
    'up 3',
    'down 8',
    'forward 2',
]

def load(file):
    with open(file) as f:
        data = f.readlines()
        return data


def steps(lines, x_pos_char, y_pos_char):
    d1 = [ln.split(' ') for ln in lines]
    st = [(ln[0][0], int(ln[1]) * (1 if ln[0][0] in [x_pos_char, y_pos_char] else -1)) for ln in d1]
    return st


def walk(steps):
    aim = xx = yy = 0
    for st in steps:
        if st[0] in ['f', 'b']:
            xx += st[1]
            if st[0] == 'f':
                yy += (aim * st[1])
        elif st[0] in ['d', 'u']:
            aim += st[1]
#            yy += st[1]

    return xx * yy


test1 = walk(steps(eg, 'f', 'd'))
assert test1 == 900

st = load('data.txt')
ans = walk(steps(st, 'f', 'd'))
print(f"Answer: {ans}")