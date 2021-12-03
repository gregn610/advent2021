with open('data.txt') as f:
    data = [int(i) for i in f.readlines()]

grouped = [sum(tup) for tup in zip(data, data[1:], data[2:])]
part2 = sum([1 for first, second in zip(grouped, grouped[1:]) if second > first])
print(f"Grouped count = {part2}")
