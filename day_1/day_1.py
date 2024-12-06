from collections import Counter

with open("day_1.txt") as f:
    lines = [line.strip().split() for line in f.readlines()]

list1 = [int(line[0]) for line in lines]
list2 = [int(line[1]) for line in lines]

# Part A
list1.sort()
list2.sort()

diffs = [abs(list1[i] - list2[i]) for i, _ in enumerate(list1)]

total_diff = sum(diffs)
print(total_diff)

# Part B
similarity_score = 0
counter = Counter(list2)
for n in list1:
    similarity_score += counter[n] * n

print(similarity_score)
