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

def search_combo(px, py, e):
    ax, ay = A[e]
    bx, by = B[e]
    tx, ty = (0, 0)
    i = 0
    while i <= (px // ax) + 1:
        j = 0
        while tx < px and ty < py:
            tx = (ax * i) + (bx * j)
            ty = (ay * i) + (by * j)
            j += 1

        if tx == px and ty == py:
            return (i, j-1)
        
        tx, ty = (0, 0)
        i += 1
    return (0, 0)

ans = 0
for e, (px, py) in enumerate(P):
    a, b = search_combo(A, B, px, py, e)
    print(a, b)
    ans += (a * 3) + b

print(ans)