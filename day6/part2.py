from time import time

data = open('day6.txt', 'r').read().split('\n')

directions = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
obstructions = []

for i in range(len(data)):
    for j in range(len(data[0])):
        obj = data[i][j]
        if obj in directions:
            guard = (i, j)
            direction = obj
        elif obj == '#':
            obstructions.append((i, j))

def printout(data):
    for d in data:
        print(d)
    print()

def trace_path(data, guard, direction):
    visited = {'^': [], '>': [], 'v': [], '<': []}
    position = guard
    looped = False
    inside = True
    while inside:
        x, y = position
        match direction:
            case '^':
                if (x - 1) >= 0:
                    next = data[x - 1][y]
                    if next == '#':
                        if position in visited[direction]:
                            inside = False
                            looped = True
                        else:
                            visited[direction].append(position)
                        direction = directions[direction]
                    else:
                        position = (x - 1, y)
                else:
                    inside = False
            case '>':
                if (y + 1) <= len(data[0]) - 1:
                    next = data[x][y + 1]
                    if next == '#':
                        if position in visited[direction]:
                            inside = False
                            looped = True
                        else:
                            visited[direction].append(position)
                        direction = directions[direction]
                    else:
                        position = (x, y + 1)
                else:
                    inside = False
            case 'v':
                if (x + 1) <= len(data) - 1:
                    next = data[x + 1][y]
                    if next == '#':
                        if position in visited[direction]:
                            inside = False
                            looped = True
                        else:
                            visited[direction].append(position)
                        direction = directions[direction]
                    else:
                        position = (x + 1, y)
                else:
                    inside = False
            case '<':
                if (y - 1) >= 0:
                    next = data[x][y - 1]
                    if next == '#':
                        if position in visited[direction]:
                            inside = False
                            looped = True
                        else:
                            visited[direction].append(position)
                        direction = directions[direction]
                    else:
                        position = (x, y - 1)
                else:
                    inside = False
    return looped

st = time()
counter = 0
for e1, a in enumerate(data):
    for e2, b in enumerate(a):
        if b != '#' and b not in directions:
            data[e1] = data[e1][:e2] + '#' + data[e1][e2 + 1:]
            if trace_path(data, guard, direction):
                # data[e1] = data[e1][:e2] + 'O' + data[e1][e2 + 1:]
                # printout(data)
                counter += 1
            data[e1] = data[e1][:e2] + '.' + data[e1][e2 + 1:]
print(time() - st)
print(counter)