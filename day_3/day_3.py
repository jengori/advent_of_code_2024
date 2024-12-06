import re

with open("day_3.txt") as f:
    text = f.read()

sums = re.findall("mul\(\d+,\d+\)", text)

total = 0

for s in sums:
    nums = re.findall("\d+", s)
    result = int(nums[0]) * int(nums[1])
    total += result

print(total)

index = 0
status = "enabled"
total = 0

while True:
    x = re.search("mul\(\d+,\d+\)|do\(\)|don't\(\)", text[index::])
    if x:
        index += x.end()
        if x.group() == "do()":
            status = "enabled"
        elif x.group() == "don't()":
            status = "disabled"
        else:
            if status == "enabled":
                nums = re.findall("\d+", x.group())
                result = int(nums[0]) * int(nums[1])
                total += result
    else:
        break

print(total)
