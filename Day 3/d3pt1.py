from collections import Counter

filename = "C:\\Users\\wcorr\\Desktop\\AoC 2021\\Day 3\\data.txt"
with open(filename) as f:
    content = f.readlines()

content = [list(x.strip()) for x in content]

test = [Counter(z) for z in zip(*content)]

gamma_rate = "".join([z.most_common(1)[0][0] for z in test])
episolon_rate = "".join(([str(1-int(x)) for x in gamma_rate]))

power_consumption = int(gamma_rate, base=2) * int(episolon_rate, base=2)

print(power_consumption)