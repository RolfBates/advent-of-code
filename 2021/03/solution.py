from collections import Counter
with open("input.txt") as f:
    lines = [int(line.strip(), 2) for line in f]

def score(nums, bit_pos):
    res = 0
    for num in nums:
        if num >> bit_pos & 1:
            res += 1
        else:
            res -= 1
    return res

count = Counter()
for i in range(11, -1, -1):
    count[i] = score(lines, i)

gamma = 0
epsilon = 0
for c in count.keys():
    gamma = gamma << 1
    epsilon = epsilon << 1
    if count[c] < 0:
        epsilon += 1
    else:
        gamma += 1

print(gamma * epsilon)

o2_rating = set(lines)
bp = 11
while len(o2_rating) > 1:
    s = score(o2_rating, bp)
    if s < 0:
        o2_rating = {r for r in o2_rating if (r >> bp & 1) == 0}
    else:
        o2_rating = {r for r in o2_rating if (r >> bp & 1) == 1}
    bp -= 1
bp = 11
co2_rating = set(lines)
while len(co2_rating) > 1:
    s = score(co2_rating, bp)
    if s < 0:
        co2_rating = {r for r in co2_rating if (r >> bp & 1) == 1}
    else:
        co2_rating = {r for r in co2_rating if (r >> bp & 1) == 0}
    bp -= 1

temp = o2_rating.pop()
print(temp * co2_rating.pop())


