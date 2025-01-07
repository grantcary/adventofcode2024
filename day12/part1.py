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

def get_perimeter(garden, plot_touch_count):
    for e, p in enumerate(garden):
        x1, y1 = p
        for x2, y2 in garden[:e] + garden[e + 1:]:
            if x1 + 1 == x2 or x1 - 1 == x2:
                if y1 == y2:
                    plot_touch_count[p] -= 1
            elif y1 + 1 == y2 or y1 - 1 == y2:
                if x1 == x2:
                    plot_touch_count[p] -= 1
    return plot_touch_count

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
    plot_touch_count = {plot: 4 for plot in garden}
    perimeter = sum(get_perimeter(garden, plot_touch_count).values())

    ans += area * perimeter 

    # remove found positions from starts
    for plot in garden:
        if plot in start_positions:
            start_positions.remove(plot)
            if start_positions:
                start = start_positions[0]

print(ans) # 1477762