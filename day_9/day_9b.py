from collections import Counter

with open("day_9.txt") as f:
    disk_map = f.read()

disk_map_as_list = []

for i, n in enumerate(disk_map):

    if i % 2 == 0:
        for _ in range(int(n)):
            disk_map_as_list.append(int(i / 2))
    else:
        for _ in range(int(n)):
            disk_map_as_list.append(".")


counter = Counter([x for x in disk_map_as_list if x!= '.'])
max_file_id = max(counter.keys())

sections_of_space = [[] for _ in range(max_file_id)]

for i, n in enumerate(disk_map):
    if i % 2 == 1:
        for n in range(int(n)):
            sections_of_space[int((i - 1) / 2)].append('.')

for file_id in range(max_file_id, 0, -1):

    for section in sections_of_space[0:file_id]:
        if '.' not in section:
            pass
        else:
            size_of_section = len(section)
            index_of_first_empty_space = section.index('.')
            number_of_blocks_to_put_in = counter[file_id]

            if size_of_section - index_of_first_empty_space >= number_of_blocks_to_put_in:
                for x in range(index_of_first_empty_space, index_of_first_empty_space + number_of_blocks_to_put_in):
                    section[x] = file_id
                break

nums_moved = []
for section in sections_of_space:
    for num in section:
        if num != '.' and num not in nums_moved:
            nums_moved.append(num)

for i, x in enumerate(disk_map_as_list):
    if x in nums_moved:
        disk_map_as_list[i] = "*"

sections_concat = []
for section in sections_of_space:
    sections_concat += section

for i, x in enumerate(disk_map_as_list):
    if x == '.':
        disk_map_as_list[i] = sections_concat.pop(0)

checksum = 0

for i,x in enumerate(disk_map_as_list):
    if x not in [".", "*"]:
        checksum += i * x

print(checksum)
