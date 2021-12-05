from collections import defaultdict

coords_dict = defaultdict(int)

filename = "data.txt"
with open(filename) as f:
    content = f.readlines()

    for line in content:
        cloud_start, cloud_end = line.strip().split(' -> ')
        x_start_coord, y_start_coord = cloud_start.split(",")
        x_end_coord, y_end_coord = cloud_end.split(",")

        delta_x = (int(x_end_coord) - int(x_start_coord))
        delta_y = (int(y_end_coord) - int(y_start_coord))

        for i in range(max(abs(delta_x), abs(delta_y))+1):
            x_increment = int(x_start_coord) + (i *(1 if delta_x > 0 else (-1 if delta_x < 0 else 0)))
            y_increment = int(y_start_coord) + (i *(1 if delta_y > 0 else (-1 if delta_y < 0 else 0)))
            coords_dict[(x_increment, y_increment)] += 1

print(len([x for x in coords_dict if coords_dict[x] > 1]))