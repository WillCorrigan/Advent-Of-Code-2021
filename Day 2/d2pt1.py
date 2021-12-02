import numpy as np
import pandas as pd

filename = "C:\\Users\\wcorr\\Desktop\\AoC 2021\\Day 2\\data.txt"
with open(filename) as f:
    content = f.readlines()

content = [[x[0], int(x[1])] for x in (y.strip().split(" ") for y in content)]
summed_content = [[k, v] for k, v in pd.DataFrame(content).groupby(0).sum()[1].items()]

answer = (summed_content[0][1] - summed_content[2][1]) * summed_content[1][1]

print(answer)