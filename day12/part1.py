data = open('day12.txt', 'r').read().split('\n')

directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def find_garden(data, current_position, found=None):
    a, b = current_position
    current_plot = data[a][b]
    if current_plot == 9:
        if (a, b) not in found:
            found.append((a, b))
    rr = range(len(data))
    cr = range(len(data[0]))
    if found is None:
        found = []
    for x, y in directions:
        xx, yy = a + x, b + y
        if xx in rr and yy in cr:
            if data[xx][yy] == current_plot:
                find_garden(data, (a + x, b + y), found)
    return found

unique = set([plot for plots in data for plot in plots])
gardens = []
visited = []

for i, plots in enumerate(data):
    start_positions = []
    last = None
    for e, p in enumerate(plots):
        if last != p:
            start_positions.append((i, e))
        last = p
    print(start_positions)
    # for plot in plots:
    #     pass