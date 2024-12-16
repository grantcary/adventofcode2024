data = open('day6.txt', 'r').read().split('\n')

directions = {'^': '>', '>': 'v', 'v': '<', '<': '^'}

for i in range(len(data)):
    for j in range(len(data[0])):
        obj = data[i][j]
        if obj in directions:
            guard = (i, j)
            direction = obj

visited = [guard]
position = guard
inside = True
print(position)
while inside:
    x, y = position
    match direction:
        case '^':
            if (x - 1) >= 0:
                next = data[x - 1][y]
                if next == '#':
                    direction = directions[direction]
                else:
                    position = (x - 1, y)
            else:
                inside = False
        case '>':
            if (y + 1) <= len(data[0]) - 1:
                next = data[x][y + 1]
                if next == '#':
                    direction = directions[direction]
                else:
                    position = (x, y + 1)
            else:
                inside = False
        case 'v':
            if (x + 1) <= len(data) - 1:
                next = data[x + 1][y]
                if next == '#':
                    direction = directions[direction]
                else:
                    position = (x + 1, y)
            else:
                inside = False
        case '<':
            if (y - 1) >= 0:
                next = data[x][y - 1]
                if next == '#':
                    direction = directions[direction]
                else:
                    position = (x, y - 1)
            else:
                inside = False


    if position not in visited:
        visited.append(position)

ans = len(visited)
print(ans)