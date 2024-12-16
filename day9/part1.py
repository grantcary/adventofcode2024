data = open('day9.txt', 'r').read()

used = [int(x) for e, x in enumerate(data) if e % 2 == 0]
free = [int(x) for e, x in enumerate(data) if e % 2 != 0]


s = [e for e, c in enumerate(used) for _ in range(c)]

offset = 0
if len(used) > len(free):
    used = used[:len(used) - 1]

for u, f in zip(used, free):
    offset += u
    if f != 0:
        s = s[:offset] + s[-f:][::-1] + s[offset:]
        s = s[:-f]
        offset += f

ans = sum([c * e for e, c in enumerate(s)])
print(ans)