data = open('day1.txt', 'r').read().split('\n')
data = list(map(lambda x: list(map(int, x.split())), data)) # splits apart numbers in each row and converts them to ints

l1 = list(map(lambda x: x[0], data)) # first column
l2 = list(map(lambda x: x[1], data)) # second column

c = [i * l2.count(i) for i in l1] # average run time: 0.007869863510131836

counts = {} # average run time: 0.00027914047241210936
for i in l2:
    if i not in counts:
        counts[i] = 0
    counts[i] += 1

ans = 0
for j in l1:
    if j in counts:
        ans += j * counts[j]

print(ans)