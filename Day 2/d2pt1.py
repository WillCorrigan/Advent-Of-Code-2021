import numpy as np
import pandas as pd

filename = "C:\\Users\\wcorr\\Desktop\\AoC 2021\\Day 2\\data.txt"
with open(filename) as f:
    content = f.readlines()

content = [[x[0], int(x[1])] for x in (y.strip().split(" ") for y in content)]
test = [[k, v] for k, v in pd.DataFrame(content).groupby(0).sum()[1].items()]

answer = (test[0][1] - test[2][1]) * test[1][1]

print(test)