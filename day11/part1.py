data = open('day11.txt', 'r').read().split(' ')

blinks = 1
for b in range(blinks):
    e = 0
    while e < len(data):
        stone = data[e]
        if stone == '0':
            data[e] = '1'
        elif len(stone) % 2 == 0:
            data = data[:e] + [stone[:len(stone) // 2], str(int(stone[len(stone) // 2:]))] + data[e + 1:]
            e += 1
        else:
            data[e] = str(int(stone) * 2024)
        e += 1

ans = len(data)
print(ans) # 217443