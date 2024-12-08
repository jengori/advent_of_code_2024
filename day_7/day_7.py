from itertools import combinations

with open('day_7.txt') as f:
    text = [line.strip() for line in f.readlines()]

equations = []

for line in text:
    test_value = int(line.split(":")[0])
    numbers =  [int(n) for n in line.split(":")[1].split()]

    equations.append((test_value, numbers))

numbers_lengths = [len(equation[1]) for equation in equations]
max_length = max(numbers_lengths)
min_length = min(numbers_lengths)

options_dict = {}
for n in range(min_length-1, max_length):
    arr = []
    for _ in range(n):
        arr.append(0)
        arr.append(1)

    options = list(set(list(combinations(arr, n))))
    options.sort()

    options_dict[n] = options

test_values = [equation[0] for equation in equations]

result = 0

for j, value in enumerate(test_values):
    numbers = equations[j][1]

    options = options_dict[len(numbers)-1]
    for option in options:
        i = 0
        total = numbers[0]
        while i < len(numbers) - 1:
            if option[i] == 0:
             total += numbers[i + 1]
            else:
                total *= numbers[i + 1]
            i += 1
            if total > value:
                break
        if total == value:
            result += value
            break

print(result)