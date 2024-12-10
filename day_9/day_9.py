with open("day_9_test.txt") as f:
    disk_map = f.read()

disk_map_as_list = []


for i, n in enumerate(disk_map):
    if i % 2 == 0:
        for _ in range(int(n)):
            disk_map_as_list.append(int(i / 2))
    else:
        for _ in range(int(n)):
            disk_map_as_list.append(".")

print(disk_map_as_list)


num_spaces = disk_map_as_list.count(".")

nums_to_fill_spaces = [x for x in disk_map_as_list if x != "."][::-1][:num_spaces]
print(nums_to_fill_spaces)

i = 0
while i < num_spaces:
    for j, x in enumerate(disk_map_as_list):
        if x == ".":
            disk_map_as_list[j] = nums_to_fill_spaces[i]
            i += 1

for n in range(-1, -num_spaces - 1, -1):
    disk_map_as_list[n] = "."


checksum = 0
for k, n in enumerate(disk_map_as_list[:len(disk_map_as_list) - num_spaces]):
    checksum += k * n

print(checksum)
