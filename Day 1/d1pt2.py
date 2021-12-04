filename = "data.txt"
with open(filename) as f:
    content = f.readlines()

content = [int(x.strip()) for x in content]

print(sum((y > x) for x, y in zip(content[:-1], content[3:])))