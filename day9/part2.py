data = open('day9.txt', 'r').read()

used = [int(x) for e, x in enumerate(data) if e % 2 == 0]
free = [int(x) for e, x in enumerate(data) if e % 2 != 0]
ids = [[e for _ in range(c)] for e, c in enumerate(used)]
if len(used) > len(free):
    free.append(0)

def move(array, i, j):
    array = array[:j] + [array[i]] + array[j:]
    return array[:i + 1] + array[i + 2:]

moved = []
i = len(used) - 1
while i >= 0:
    u = used[i]
    found = False
    j = 0
    while not found and j < len(free):
        f = free[j]
        if j < i and u <= f and f != 0 and ids[i][0] not in moved:
            moved.append(ids[i][0])
            ids = move(ids, i, j + 1)

            free[i - 1] += used[i] + free[i]
            used = move(used, i, j + 1)

            free = move(free, i, j + 1)
            free[j + 1] = free[j] - u
            free[j] = 0

            found = True
        j += 1
    if not found:
        i -= 1
    
ids = [ids[e] + [0] * f for e, f in enumerate(free)]
ids = [x for g in ids for x in g]

ans = sum([c * e for e, c in enumerate(ids)])
print(ans)