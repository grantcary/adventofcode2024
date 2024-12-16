data = open('day11.txt', 'r').read().split(' ')

def entry(stone, value, stones):
    if stone not in stones:
        stones[stone] = value
    else:
        stones[stone] += value

stones = {}
for d in data:
    entry(d, 1, stones)

blinks = 75
for b in range(blinks):
    for stone, count in stones.copy().items():
        if stone == '0' and count > 0:
            entry('1',  count, stones)
            stones[stone] -= count
        elif len(stone) % 2 == 0 and count > 0:
            entry(stone[:len(stone) // 2], count, stones)
            entry(str(int(stone[len(stone) // 2:])), count, stones)
            stones[stone] -= count
        elif count > 0:
            entry(str(int(stone) * 2024), count, stones)
            stones[stone] -= count

ans = 0
for count in stones.values():
    ans += count

print(ans) # 257246536026785