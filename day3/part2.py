data = open('day3.txt', 'r').read().split('\n')

ans = 0
toggle = True
for memory in data:
    for i in range(len(memory) - 3):
        if memory[i : i + 4] == 'do()':
            toggle = True
        elif memory[i : i + 7] == "don't()":
            toggle = False
        elif memory[i : i + 4] == 'mul(' and toggle:
            j = i + 4
            register = 0
            buffer = ''
            while memory[j].isdigit() and j < (i + 8):
                buffer += memory[j]
                j += 1

            if memory[j] == ',':
                register = int(buffer)
                buffer = ''
                j += 1
                
                while memory[j].isdigit() and j < (i + 12):
                    buffer += memory[j]
                    j += 1

                if memory[j] == ')':
                    register *= int(buffer)
                    ans += register

print(ans)