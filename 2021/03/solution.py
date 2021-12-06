from collections import Counter
with open("input.txt") as f:
    lines = [int(line.strip(), 2) for line in f]

lines.sort()

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


lo, hi = 0, len(lines)
bp = 11
while lo < hi:
    mid = (lo + hi) // 2

    most_common = (lines[mid] >> bp & 1)

    if most_common:
        # search between lo and mid for first 0

        while lo < mid:
            mid2 = (lo + mid) // 2
            if lines[mid2] >> bp & 1:
                mid = mid2
            else:
                lo = mid2 + 1

        hi = mid
    else:
        # search between mid and hi for first 1

        while mid < hi:
            mid2 = (mid + hi) // 2
            if lines[mid2] >> bp & 1:
                hi = mid2
            else:
                mid = mid2 + 1
        lo = mid + 1

print(temp, lines[lo])






