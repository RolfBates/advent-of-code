
file_name = "input.txt"

with open(file_name) as f:
    data = [int(line.strip()) for line in f]


def count_increases(data):
    res = 0
    for i in range(len(data) - 1):
        if data[i+1] > data[i]:
            res += 1
    print(res)

windows = [data[i] + data[i+1] + data[i+2] for i in range(len(data) - 2)]

count_increases(data)
count_increases(windows)

res = 0
for i in range(len(data) - 3):
    if data[i] < data[i+3]:
        res += 1
print(res)

    
