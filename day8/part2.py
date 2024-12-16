data = open('day8.txt', 'r').read().split('\n')

frequencies = []
antennas = []

for i, r in enumerate(data):
    for j, c in enumerate(r):
        if c != '.':
            frequencies.append(c)
            antennas.append((i, j))

print(frequencies)
print(antennas)

antinodes = []
row_range = range(len(data))
col_range = range(len(data[0]))

for a, pos_1 in zip(frequencies, antennas):
    for b, pos_2 in zip(frequencies, antennas):
        if a == b and pos_1 != pos_2:
            if pos_1 not in antinodes:
                antinodes.append(pos_1)
            if pos_2 not in antinodes:
                antinodes.append(pos_2)

            x1, y1 = pos_1; x2, y2 = pos_2
            sy, sx = (y2 - y1, x2 - x1)

            m = 0
            p1 = (x1 - sx * m, y1 - sy * m)
            while p1[0] in col_range and p1[1] in row_range:
                if p1 not in antinodes:
                    antinodes.append(p1)
                m += 1
                p1 = (x1 - sx * m, y1 - sy * m)
            
            m = 0
            p2 = (x2 + sx * m, y2 + sy * m)
            while p2[0] in col_range and p2[1] in row_range:
                if p2 not in antinodes:
                    antinodes.append(p2)
                m += 1
                p2 = (x2 + sx * m, y2 + sy * m)

            print(a, pos_1, pos_2, (sy, sx), p1, p2)

for x, y in antinodes:
    if data[x][y] == '.':
        data[x] = data[x][:y] + '#' + data[x][y + 1:]

for r in data:
    print(r)

print(len(antinodes))