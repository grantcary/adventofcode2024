from itertools import product

data = open('day7.txt', 'r').read().split('\n')
data = list(map(lambda x: x.split(':'), data))
test_value = [int(tv) for tv, _ in data]
numbers = [list(map(int, nums.split())) for _, nums in data]

def generate_combinations(size):
    return [''.join(p) for p in product('+*', repeat=size)]

ans = 0
for tv, n in zip(test_value, numbers):
    test = False
    for combo in generate_combinations(len(n) - 1):
        prev = n[0]
        for i, o in enumerate(combo):
            if o == '+':
                prev += n[i + 1]
            elif o == '*':
                prev *= n[i + 1]
        if prev == tv:
            test = True
    if test:
        ans += tv

print(ans)