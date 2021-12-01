with open('data.txt') as f:
    data = f.readlines()

data = [int(i.rstrip()) for i in data]
incr = 0

for idx, val in enumerate(data):
    if idx == 0:
        print(data[0])
        continue
    if data[idx-1] < data[idx]:
        incr += 1
        print(f"{data[idx]} increase")
    else:
        print(f"{data[idx]}")

print(f"Loop Total {incr}")

asdf = sum([int(second > first) for first, second in zip(data, data[1:])])
print(f"Generator count = {asdf}")
