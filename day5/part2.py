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

def search_swap(page, chunk, lookup):
    for x in lookup[page]:
        for e, y in enumerate(chunk):
            if x == y:
                temp = page
                page = chunk[e]
                chunk[e] = temp
                return page, chunk
    return page, chunk

def swap(pages, e, after, before):
    pre, post, page = pages[:e], pages[e+1:], pages[e]
    if post and (page in before):
        page, post = search_swap(page, post, before)
        return pre + [page] + post
    if pre and (page in after):
        page, pre = search_swap(page, pre, after)
        return pre + [page] + post
    return pre + [page] + post

def validate_pages(pages, before, after):
    print(pages)
    correct = False
    while not correct:
        e = 0
        errors = 0
        while e < len(pages):
            prev = pages
            pages = swap(pages, e, after, before)
            if pages != prev:
                errors += 1
            print(pages)
            e += 1
        if errors == 0:
            correct = True
    return pages

ans = 0
for pages in update:
    updated = validate_pages(pages, before, after)
    print()
    if pages != updated:
        ans += updated[(len(updated) // 2)]

print(ans)