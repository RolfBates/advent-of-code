
cups = "418976235"
cur = 0
# 100 moves
# cur is first
# each move
# take 3 left of cur out
# dest = cur_label - 1 # decrease until it's an available cup OR wrap around to max
# removed cups go clockwise of dest cup
# cur is clockwise of cur

state = {}

def do_move(cups, cur):
    cur_label = int(cups[cur])
    out_cur = (cur + 1) % len(cups)
    out = []
    for i in range(3):
        out.append(cups[out_cur])
        out_cur = (out_cur + 1) % len(cups)
    print(cups, out)
    cups = [c for c in cups if c not in out]
    found = False
    while not found:
        cur_label -= 1
        if cur_label == 0:
            cur_label = 9
        idx = cups.index(f"{cur_label}")
        if idx != -1:
            found = True
            dest = idx

    print(cups, out, idx)

do_move(cups, cur)

