data = open('day4.txt', 'r').read().split('\n')

patterns = [0, 1, 2], [2, 1, 0]
pattern_key = [(0, 0),
               (1, 0)]

def kernel(data, keyword, patterns, pattern_key):
    count = 0
    print(len(data), len(data[0]))
    for r in range(len(data) - 2):
        for c in range(len(data[0]) - 2):
            local_count = 0
            for p in pattern_key:
                buffer = ''
                for a, b in zip(patterns[p[0]], patterns[p[1]]):
                    buffer += data[r + a][c + b]
                if keyword == buffer or keyword == buffer[::-1]:
                    local_count += 1
            if local_count == 2:
                count += 1
    return count

ans = kernel(data, 'MAS', patterns, pattern_key)

print(ans)