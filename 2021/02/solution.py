# forward 1, down 2, up 3
# down increases depth

x, y = 0, 0

with open("input.txt") as f:
    for line in f:
        cmd, unit = line.strip().split(" ")
        unit = int(unit)
        if cmd == "forward":
            x += unit
        if cmd == "up":
            y -= unit
        if cmd == "down":
            y += unit

print(x*y)

# forward -> horizontal += x, vert = x * aim


x, y, aim = 0, 0, 0

with open("input.txt") as f:
    for line in f:
        cmd, unit = line.strip().split(" ")
        unit = int(unit)
        if cmd == "forward":
            x += unit
            y += unit * aim
        if cmd == "up":
            aim -= unit
        if cmd == "down":
            aim += unit

print(x*y)
