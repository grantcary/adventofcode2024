data = open('day2.txt', 'r').read().split('\n')
data = list(map(lambda x: list(map(int, x.split())), data))

def valid_levels(report):
    last = report[0]
    direction = None
    for level in report[1:]:
        if abs(last - level) not in range(1, 4):
            return 0
        temp = True if last < level else False
        if direction is not None:
            if direction != temp:
                return 0
        direction = temp
        last = level
    return 1

ans = sum([valid_levels(report) for report in data])

print(ans)