data = open('day4.txt', 'r').read().split('\n')

patterns = [0, 0, 0, 0], [3, 3, 3, 3], [0, 1, 2, 3], [3, 2, 1, 0]
pattern_key = [(2, 2),
               (3, 2)]

def kernel(data, keyword, patterns, pattern_key):
    count = 0
    print(len(data), len(data[0]))
    for r in range(len(data)):
        for c in range(len(data[0]) - 3):
            buffer = ''
            for a in patterns[2]:
                buffer += data[r][c + a]
            if keyword == buffer or keyword == buffer[::-1]:
                count += 1

    for r in range(len(data) - 3):
        for c in range(len(data[0])):
            buffer = ''
            for a in patterns[2]:
                buffer += data[r + a][c]
            if keyword == buffer or keyword == buffer[::-1]:
                count += 1

    for r in range(len(data) - 3):
        for c in range(len(data[0]) - 3):
            for p in pattern_key:
                buffer = ''
                for a, b in zip(patterns[p[0]], patterns[p[1]]):
                    buffer += data[r + a][c + b]
                if keyword == buffer or keyword == buffer[::-1]:
                    count += 1
    return count

ans = kernel(data, 'XMAS', patterns, pattern_key)

print(ans)