data = open('day2.txt', 'r').read().split('\n')
data = list(map(lambda x: list(map(int, x.split())), data))

def valid_levels(report):
    last = report[0]
    direction = None
    for level in report[1:]:
        if abs(last - level) not in range(1, 4):
            return 0
        temp = True if last < level else False
        if direction is not None:
            if direction != temp:
                return 0
        direction = temp
        last = level
    return 1

def validate(report): # this function was all i needed
    if valid_levels(report):
        return True
    
    for i in range(len(report)):
        if valid_levels(report[:i] + report[i + 1:]):
            return True
    
    return False

ans = sum([validate(report) for report in data])

print(ans)

### +++---WASTEOFTIME---+++ ###
# about three or four versions of this and they were all shit.
# many hours gone. what the fuck. i even tried a version of the function that 
# ended up working but instead of stopping the loop when it finds a solution, 
# i had it loop through everything. i saw multiple errors per report so i deemed
# it the wrong way to do it. lessons to learn here, dont waste time, and practice
# your shit. i couldnt spot the problem when i was close to solving it. 
# PRACTICE PRACTICE PRACTICE PRACTICE PRACTICE

# def check(x, y, d):
#     def check_direction(x, y, d):
#         direction = 1 if x < y else -1
#         return False if direction == d else True
#     def check_range(x, y):
#         return False if abs(x - y) in range(1, 4) else True
#     return check_direction(x, y, d) or check_range(x, y)

# def search_error(a, b, c, d):
#     if check(a, b, d) or check(b, c, d):
#         return check(a, b, d) + check(b, c, d) + check(a, c, d)
#     else: return check(a, b, d) + check(b, c, d)

# def define_direction(a, b, c):
#     def direction(x, y):
#         return 1 if x < y else -1
#     return direction(a, b) if a != b else direction(a, c)

# total_error = 0
# for report in data:
#     a, b, c = report[0], report[1], report[2]
#     if len(set([a, b, c])) > 1:
#         d = define_direction(a, b, c)
#         local_error = check(a, b, d)
#         p = a
#         for e in range(2, len(report) - 1):
#             a, b = [report[e], report[e + 1]]
#             error_a = check(a, b, d)
#             local_error += error_a
#             error_b = 0
#             if error_a > 0:
#                 print(p, a, b)
#                 error_b = check(p, b, d)
#                 local_error += error_b
#             if error_a == 0 and error_b == 0:
#                 p = a

#             # error = search_error(a, b, c, d)
#             # print(a, b, error)
#         # print()
#         print(report, local_error)
#         if local_error == 0:
#             total_error += 1
#     print('------------------------------------------------')

# print(total_error)
### +++---WASTEOFTIME---+++ ###
