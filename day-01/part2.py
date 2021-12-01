with open('data.txt') as f:
    data = f.readlines()

data = [int(i.rstrip()) for i in data]

grouped = [(aa + bb + cc) for aa, bb, cc in zip(data, data[1:], data[2:])]
part2 = sum([int(second > first) for first, second in zip(grouped, grouped[1:])])
print(f"Grouped count = {part2}")
