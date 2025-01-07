data = open('day12.txt', 'r').read().split('\n')

directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def find_garden(data, current_position, found=None, previous=None):
    a, b = current_position
    current_plot = data[a][b]

    if current_plot == previous:
        if (a, b) not in found:
            found.append((a, b))

    rr = range(len(data))
    cr = range(len(data[0]))

    if previous is None:
        previous = current_plot

    if found is None:
        found = []

    for x, y in directions:
        xx, yy = a + x, b + y
        if xx in rr and yy in cr:
            if data[xx][yy] == current_plot and (xx, yy) not in found:
                find_garden(data, (xx, yy), found, current_plot)

    return found

def build_map(garden):
    r, c = {}, {}
    for x, y in garden:
        if x not in r:
            r[x] = [y]
        else:
            r[x].append(y)
        if y not in c:
            c[y] = [x]
        else:
            c[y].append(x)
    return r, c

def search_sides(garden):
    rows, cols = build_map(garden)
    count = 0
    sides = []
    garden_swapped = [(b, a) for a, b in garden]
    for g, d in [(garden, rows), (garden_swapped, cols)]:
        v1, v2 = {}, {}
        for a, b in g:
            if b + 1 not in d[a]:
                if b not in v1:
                    v1[b] = [a]
                else:
                    v1[b].append(a)
            if b - 1 not in d[a]:
                if b not in v2:
                    v2[b] = [a]
                else:
                    v2[b].append(a)
        sides.extend([v1, v2])

    for s in sides:
        for v in s.values():
            blocks = 1
            if len(v) > 1:
                v = sorted(v)
                p = v[0]
                for n in v[1:]:
                    if p + 1 != n:
                        blocks += 1
                    p = n
            count += blocks

    return count

start_positions = []
for i, plots in enumerate(data):
    last = None
    for e, p in enumerate(plots):
        if last != p:
            start_positions.append((i, e))
        last = p

# for start in start_positions:
ans = 0
start = start_positions[0]
while start_positions:
    garden = find_garden(data, start, [start])
    area = len(garden)
    sides = search_sides(garden)

    ans += area * sides

    for plot in garden:
        if plot in start_positions:
            start_positions.remove(plot)
            if start_positions:
                start = start_positions[0]

print(ans) # 923480