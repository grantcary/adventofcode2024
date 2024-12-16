data = open('day10.txt', 'r').read().split('\n')
data = [list(map(int, list(r))) for r in data]

trailheads = []
for r, row in enumerate(data):
    for c, height in enumerate(row):
        if height == 0:
            trailheads.append((r, c))

directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def find_peak(data, current_position):
    a, b = current_position
    current_height = data[a][b]
    if current_height == 9:
        return 1
    rr = range(len(data))
    cr = range(len(data[0]))
    found = 0
    for x, y in directions:
        xx, yy = a + x, b + y
        if xx in rr and yy in cr:
            if data[xx][yy] == current_height + 1:
                found += find_peak(data, (a + x, b + y))
    return found

scores = []
for t in trailheads:
    reachable = find_peak(data, t)
    # print(t, reachable)
    scores.append(reachable)

ans = sum(scores)
print(ans)