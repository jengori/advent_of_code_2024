with open("day_2.txt") as f:
    reports = [[int(n) for n in line.split()] for line in f.read().splitlines()]


def is_safe(r: list):
    i = 0
    direction = None

    while i < len(r) - 1:

        if not(0 < abs(r[i] - r[i + 1]) <= 3):
            return False

        else:
            if i == 0:
                if r[i] < r[i + 1]:
                    direction = "increasing"
                    i += 1
                else:
                    direction = "decreasing"
                    i += 1

            else:
                if r[i] > r[i + 1] and direction == "increasing":
                    return False
                elif r[i] < r[i + 1] and direction == "decreasing":
                    return False

                else:
                    i += 1

    return True

def is_safe_plus_tolerance(r: list):
    j = 0
    while j < len(r):
        new_l = [r[i] for i in range(len(r)) if i != j]

        if is_safe(new_l):
            return True
        else:
            j += 1

    return False


num_safe_reports = 0
unsafe_reports = []

for report in reports:
    if is_safe(report):
        num_safe_reports += 1
    else:
        unsafe_reports.append(report)

# Part A solution
print(num_safe_reports)

for level in unsafe_reports:
    num_safe_reports += is_safe_plus_tolerance(level)

# Part B solution
print(num_safe_reports)
