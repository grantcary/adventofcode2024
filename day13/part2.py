data = open('day13.txt', 'r').read().split('\n\n')
data = [d.split('\n') for d in data]

def match(d):
    Z = ''
    q = d[0]
    while q.isdigit():
        Z += q
        d = d[1:]
        if d:
            q = d[0]
        else:
            return Z
    return Z

def sep(d):
    X = 0
    Y = 0
    for e, c in enumerate(d):
        if c == 'X':
            X = int(match(d[e+2:]))
        if c == 'Y':
            Y = int(match(d[e+2:]))
    return (X, Y)

A = [sep(d[0]) for d in data]
B = [sep(d[1]) for d in data]
P = [sep(d[2]) for d in data]

def search_tree(px, py, mix, max, miy, may, e):
    ax, ay = A[e]
    bx, by = B[e]
    i = ((max + mix) // 2)
    j = ((may + miy) // 2)
    tx = (ax * i) + (bx * j)
    ty = (ay * i) + (by * j)
    if tx == px and ty == py:
        return (i, j)
    print(i, j, '|', px, py, '|', tx, ty, '|', mix, max, miy, may)
    if mix != max or miy != may:
        if tx > px and ty > py:
            return search_tree(px, py, mix, i + 1, miy, j + 1, e)
        elif tx < px and ty < py:
            return search_tree(px, py, i - 1, max + 1, j - 1, may + 1, e)
        elif tx > px and ty < py:
            return search_tree(px, py, 0, i + 1, j - 1, may + 1, e)
        elif tx < px and ty > py:
            return search_tree(px, py, i - 1, max + 1, 0, j + 1, e)
    else:
        return (0, 0)

ans = 0
P = [P[0]]
for e, (px, py) in enumerate(P):
    # px += 10000000000000
    # py += 10000000000000
    ax, ay = A[e]
    bx, by = B[e]
    a = max((px // ax, py // ay )) + 1
    b = max((px // bx, py // by )) + 1
    n = search_tree(px, py, 0, a, 0, b, e)
    print(n)
    # print(a, b)
    # ans += (a * 3) + b

# print(ans)