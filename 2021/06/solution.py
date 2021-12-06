from collections import Counter
import time

# new fish every 7 days
# new fish need 9 days to reproduce

pc = time.perf_counter()

# fish = [1, 4, 1, 1, 1, 1, 1, 1, 1, 4, 3, 1, 1, 3, 5, 1, 5, 3, 2, 1, 1, 2, 3, 1, 1, 5, 3, 1, 5, 1, 1, 2, 1, 2, 1, 1, 3,
#         1, 5, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 4, 5, 3, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 4, 4, 4, 1, 1, 1, 1, 5, 1, 2, 4,
#         1, 1, 4, 1, 2, 1, 1, 1, 2, 1, 5, 1, 1, 1, 3, 4, 1, 1, 1, 3, 2, 1, 1, 1, 4, 1, 1, 1, 5, 1, 1, 4, 1, 1, 2, 1, 4,
#         1, 1, 1, 3, 1, 1, 1, 1, 1, 3, 1, 3, 1, 1, 2, 1, 4, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 2, 1, 3, 1, 1, 1, 1, 4, 1,
#         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 5, 1, 1, 1, 2, 2, 1, 1, 3, 5, 1, 1, 1, 1, 3, 1, 3, 3, 1, 1, 1, 1, 3,
#         5, 2, 1, 1, 1, 1, 5, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 5, 1, 4, 3, 3,
#         1, 3, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 3, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 2, 1, 4, 1, 1, 1, 1,
#         1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 4, 4, 1, 1, 1, 1, 1, 1, 1, 5, 1, 1, 2, 5, 1, 1, 4,
#         1, 3, 1, 1]

with open("input.txt") as f:
    fish = [int(x) for x in f.readline().strip().split(",")]
# fish = [3,4,3,1,2]

cooldown = 6
new_fish = 8
# days = 80
days = 256

counts = Counter(fish)
for day in range(days):
    nxt = Counter()
    for k, v in counts.items():
        if k == 0:
            nxt[cooldown] += v
            nxt[new_fish] += v
        else:
            nxt[k - 1] += v
    counts = nxt

print(f"Day: {day + 1} - Fish: {sum(counts.values())}")
end = time.perf_counter()
print(f"Took {end - pc:0.4f} seconds")
