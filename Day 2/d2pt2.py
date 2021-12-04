filename = "data.txt"
with open(filename) as f:
    content = f.readlines()

content = [[x[0], int(x[1])] for x in (y.strip().split(" ") for y in content)]

aim = 0
horizontal = 0
depth = 0

for x in content:
    if x[0] == 'forward':
        horizontal += x[1]
        depth += x[1] * aim
    if x[0] == 'down':
        aim += x[1]
    if x[0] == 'up':
        aim -= x[1]

print(horizontal * depth)