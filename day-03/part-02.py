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

def load(file):
    with open(file) as f:
        data = f.readlines()
        return data


def process(data):
    bits = max(int(x, 2).bit_length() for x in data)
    arr = [int(ln, 2) for ln in data]
    return arr, bits


def instrument_recursive(data, mask, majority):
    zeros = [dd for dd in data if dd & mask == 0]
    ones = [dd for dd in data if dd & mask == mask]
    if majority == 1:
        if len(ones) >= len(zeros):
            return ones
        else:
            return zeros
    else:
        if len(zeros) <= len(ones):
            return zeros
        else:
            return ones


def instrument(data, bits, majority):
    mm = bits
    dd = data.copy()
    while len(dd) > 1:
        mm -= 1
        mask = 2 ** mm
        dd = instrument_recursive(dd, mask, majority)
    return dd[0]


def oxygen_generator(data, bits):
    return instrument(data, bits, 1)


def co2_scrubber(data, bits):
    return instrument(data, bits, 0)


def life_support(data,bits):
    return oxygen_generator(data, bits) * co2_scrubber(data, bits)


dd, bits = process(eg)
assert oxygen_generator(dd, bits) == 23
assert co2_scrubber(dd, bits) == 10
assert life_support(dd, bits) == 230

arr = load('data.txt')
dd, bits = process(arr)
ls = life_support(dd, bits)

print(f"Life support: {ls}")
