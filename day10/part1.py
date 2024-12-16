data = open('day10.txt', 'r').read().split('\n')
data = [list(map(int, list(r))) for r in data]

trailheads = []
for r, row in enumerate(data):
    for c, height in enumerate(row):
        if height == 0:
            trailheads.append((r, c))

directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def find_peak(data, current_position, found=None):
    a, b = current_position
    current_height = data[a][b]
    if current_height == 9:
        if (a, b) not in found:
            found.append((a, b))
    rr = range(len(data))
    cr = range(len(data[0]))
    if found is None:
        found = []
    for x, y in directions:
        xx, yy = a + x, b + y
        if xx in rr and yy in cr:
            if data[xx][yy] == current_height + 1:
                find_peak(data, (a + x, b + y), found)
    return found

scores = []
for t in trailheads:
    reachable = find_peak(data, t)
    # print(t, reachable)
    scores.append(len(reachable))

ans = sum(scores)
print(ans) # 688