"""
https://adventofcode.com/2021/day/3
"""
eg = [
    '00100',
    '11110',
    '10110',
    '10111',
    '10101',
    '01111',
    '00111',
    '11100',
    '10000',
    '11001',
    '00010',
    '01010',
]

BITS=12

def load(file):
    with open(file) as f:
        data = f.readlines()
        return data


def process(data):
    bits = max([len(i.rstrip()) for i in data])
    arr = [int(ln, 2) for ln in data]
    return arr, bits


def gamma(data, bits):
    mask = [2 ** idx for idx in reversed(range(bits))]
    ret = 0b0
    for mm in mask:
        if (sum([int(ln & mm > 0) for ln in data]) > (len(data) // 2)):  # number of set bit n > 1/2 of the list
            ret |= mm
    return ret


def epsilon(data, bits):
    """
    bitflip the gamma word XOR all 1
    """
    return gamma(data, bits) ^ (2 ** bits - 1)  # bitwise XOR


def power_consumption(data, bits):
    ret = gamma(data, bits) * epsilon(data, bits)
    return ret


dd, bits = process(eg)
assert gamma(dd, bits) == 0b10110
assert epsilon(dd, bits) == 0b01001
assert power_consumption(dd, bits) == 198

arr = load('data.txt')
dd, bits = process(arr)
pc = power_consumption(dd, bits)

print(f"Power consumption: {pc}")
