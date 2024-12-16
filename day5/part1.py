rules, update = open('day5.txt', 'r').read().split('\n\n')
rules = list(map(lambda x: tuple(map(int, x.split('|'))), rules.split('\n')))
update = list(map(lambda x: list(map(int, x.split(','))), update.split('\n')))

after = {}
for a, b in rules:
    if a not in after:
        after[a] = [b]
    else:
        after[a].append(b)

before = {}
for a, b in rules:
    if b not in before:
        before[b] = [a]
    else:
        before[b].append(a)

def validate_pages(pages, before, after):
    for e, page in enumerate(pages):
        pre, post = pages[:e], pages[e+1:]
        if pre and (page in before):
            for x in pre:
                if x not in before[page]:
                    return False
        if post and (page in after):
            for x in post:
                if x not in after[page]:
                    return False
    return True

ans = 0
for pages in update:
    if validate_pages(pages, before, after):
        ans += pages[(len(pages) // 2)]

print(ans)