output = []

filename = "data.txt"
with open(filename) as f:
    content = f.readlines()

    for line in content:
        tmp_output = None
        _, tmp_output = line.strip().split(" | ")
        output.append(tmp_output.split(" "))

output = [x for lst in output for x in lst]

counting = {1: 0, 4: 0, 7: 0, 8: 0}

for item in output:
    if len(item) == 2:
        counting[1] += 1
        continue
    if len(item) == 4:
        counting[4] += 1
        continue
    if len(item) == 3:
        counting[7] += 1
        continue
    if len(item) == 7:
        counting[8] += 1
        continue


print(sum(counting.values()))
