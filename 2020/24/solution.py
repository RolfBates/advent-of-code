
def process_line(line):
    x, y = 0, 0
    i = 0
    while i < len(line):
        if line[i] == "e":
            x += 2
            i += 1
        elif line[i] == "w":
            x -= 2
            i += 1
        elif line[i] == "n" and line[i + 1] == "e":
            x += 1
            y += 1
            i += 2
        elif line[i] == "n" and line[i + 1] == "w":
            x -= 1
            y += 1
            i += 2
        elif line[i] == "s" and line[i + 1] == "e":
            x += 1
            y -= 1
            i += 2
        elif line[i] == "s" and line[i + 1] == "w":
            x -= 1
            y -= 1
            i += 2
    return x, y


lines = [
    "sesenwnenenewseeswwswswwnenewsewsw",
    "neeenesenwnwwswnenewnwwsewnenwseswesw",
    "seswneswswsenwwnwse",
    "nwnwneseeswswnenewneswwnewseswneseene",
    "swweswneswnenwsewnwneneseenw",
    "eesenwseswswnenwswnwnwsewwnwsene",
    "sewnenenenesenwsewnenwwwse",
    "wenwwweseeeweswwwnwwe",
    "wsweesenenewnwwnwsenewsenwwsesesenwne",
    "neeswseenwwswnwswswnw",
    "nenwswwsewswnenenewsenwsenwnesesenew",
    "enewnwewneswsewnwswenweswnenwsenwsw",
    "sweneswneswneneenwnewenewwneswswnese",
    "swwesenesewenwneswnwwneseswwne",
    "enesenwswwswneneswsenwnewswseenwsese",
    "wnwnesenesenenwwnenwsewesewsesesew",
    "nenewswnwewswnenesenwnesewesw",
    "eneswnwswnwsenenwnwnwwseeswneewsenese",
    "neswnwewnwnwseenwseesewsenwsweewe",
    "wseweeenwnesenwwwswnew",
]

set_black = set()
with open("input.txt") as f:
    lines = f.readlines()

for line in lines:
    x, y = process_line(line.strip())
    repr = (x, y)
    if repr in set_black:
        set_black.remove(repr)
    else:
        set_black.add(repr)
print(len(set_black))

def neighbors(x, y):
    for dx, dy in [(2, 0), (-2, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
        yield x + dx, y + dy

# set_black = set([(0, 0), (1, 1)])
for day in range(100):
    next_gen = set()
    for x, y in set_black:
        black_neighbors = 0
        for nx, ny in neighbors(x, y):
            if (nx, ny) in set_black:
                black_neighbors += 1
            else:
                white_black_neighbors = 0
                for mx, my in neighbors(nx, ny):
                    if (mx, my) in set_black:
                        white_black_neighbors += 1
                if white_black_neighbors == 2:
                    next_gen.add((nx, ny))
        if 1 <= black_neighbors <= 2:
            next_gen.add((x, y))
    print(f"Day {day + 1}: {len(next_gen)}")
    set_black = next_gen
