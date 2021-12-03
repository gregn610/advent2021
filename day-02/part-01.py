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


def steps(lines, pos_char, neg_char):
    directions = [ln.split(' ') for ln in lines if ln[0] in [pos_char, neg_char]]
    steps = [int(ln[1]) * (1 if ln[0][0] == pos_char else -1) for ln in directions]
    return steps


def split(data):
    horiz = steps(data, 'f', 'b')
    vert = steps(data, 'd', 'u')
    return horiz, vert

hh, vv = split(eg)
assert (sum(hh) * sum(vv)) == 150

dd = load('data.txt')
hh, vv = split(dd)
ans = sum(hh) * sum(vv)
print(f"Answer: {ans}")