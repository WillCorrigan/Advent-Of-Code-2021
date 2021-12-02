filename = "C:\\Users\\wcorr\\Desktop\\AoC 2021\\Day 1\\data.txt"
with open(filename) as f:
    content = f.readlines()

content = [int(x.strip()) for x in content]
print(list(zip(content[:-1], content[3:])))
print(sum((y > x) for x, y in zip(content[:-1], content[3:])))