data = open('day1.txt', 'r').read().split('\n')
data = list(map(lambda x: list(map(int, x.split())), data)) # splits apart numbers in each row and converts them to ints

l1 = sorted(list(map(lambda x: x[0], data))) # sorted first column
l2 = sorted(list(map(lambda x: x[1], data))) # sorted second column

d = list(map(lambda a, b: abs(a - b), l1, l2)) # distances between first and second column
# d = [abs(a - b) for a, b in list(zip(l1, l2))] # iterable version, does same thing

ans = sum(d) # sum of all distances

print(ans)