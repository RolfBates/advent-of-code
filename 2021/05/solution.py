from collections import Counter
marks = Counter()

def mark_line(xs, ys, xd, yd):
    if xs == xd:
        for i in range(min(ys, yd), max(ys, yd) + 1):
            marks[xs, i] += 1
    elif ys == yd:
        for i in range(min(xs, xd), max(xs, xd) + 1):
            marks[i, yd] += 1
    elif abs(xs - xd) == abs(ys - yd):
        if xs > xd:
            xs, ys, xd, yd = xd, yd, xs, ys
        if ys < yd:
            for i in range(xd - xs + 1):
                marks[xs + i, ys + i] += 1
        else:
            for i in range(xd - xs + 1):
                marks[xs + i, ys - i] += 1


with open("input.txt") as f:
    for line in f:
        src, dest = line.strip().split("->")
        xs, ys = src.strip().split(",")
        xs, ys = int(xs), int(ys)
        xd, yd = dest.strip().split(",")
        xd, yd = int(xd), int(yd)
        mark_line(xs, ys, xd, yd)

overlaps = 0
for value in marks.values():
    if value > 1:
        overlaps += 1
print(overlaps)

