# read the input
with open("day_5.txt") as f:
    text = f.read().splitlines()

# put all the rules in a list
rules = [[int(n) for n in line.split('|')] for line in text if '|' in line]
# put all the updates in a list
updates = [[int(n) for n in line.split(',')] for line in text if ',' in line]

result = 0
incorrect_updates = []

for update in updates:
    correct = True
    # start at the first page number
    i = 0
    # put the applicable rules (i.e. those which contain page numbers that are both in the update) in a list
    applicable_rules = [rule for rule in rules if rule[0] in update and rule[1] in update]

    while correct and i < len(update) - 1:
        for rule in applicable_rules:
            if rule[1] == update[i]:
                    correct = False

        # remove rules relating to current page number from the list of applicable rules
        applicable_rules = [rule for rule in applicable_rules if update[i] not in rule]
        # go to the next page number
        i += 1

    middle = int((len(update) - 1) / 2)

    # if the page order is correct, add the middle page number to the result;
    # otherwise put the update in a list of incorrect updates (for use in Part B)
    if correct:
        result += update[middle]
    else:
        incorrect_updates.append(update)

# the answer to part A is ...
print(result)

result = 0

# go through the list of incorrectly ordered updates
for update in incorrect_updates:
    # put the applicable rules (i.e. those which contain two page numbers that are both in the update) in a list
    applicable_rules = [rule for rule in rules if rule[0] in update and rule[1] in update]
    correct_order = []

    while len(correct_order) < len(update):
        # find the correct next page number and append it to correct_order

        # n isn't the next page number if it is the second number in any of the applicable rules
        for n in update:
            if n not in correct_order:
                next_ = True
                for rule in applicable_rules:
                    if n == rule[1]:
                        next_ = False

                if next_:
                    correct_order.append(n)
                    applicable_rules = [rule for rule in applicable_rules if n not in rule]

    # find the middle page number in the update and add it to the result
    middle = int((len(correct_order) - 1) / 2)
    result += correct_order[middle]

# the answer to part B is ...
print(result)
