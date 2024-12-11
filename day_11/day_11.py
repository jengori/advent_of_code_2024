from collections import Counter

with open('day_11.txt') as f:
    my_stones = [int(n.strip()) for n in f.read().split()]

def num_stones_after_blinking(n: int, stones: list):
    """Given an integer n and a list of integers representing stones,
    return the number of stones after blinking n times"""

    counter = Counter(stones)

    for _ in range(n):
        next_counter = counter.copy()
        for key in counter.keys():
            if key == 0:
                next_counter[0] -= counter[key]
                next_counter[1] += counter[key]

            elif len(str(key)) % 2 == 0:
                half_length = int(len(str(key)) / 2)
                key_as_str = str(key)

                val1 = int(key_as_str[:half_length])
                val2 = int(key_as_str[half_length:])

                next_counter[val1] += counter[key]
                next_counter[val2] += counter[key]
                next_counter[key] -= counter[key]

            else:
                next_counter[key] -= counter[key]
                next_counter[key * 2024] += counter[key]

        counter = next_counter

    return sum(counter.values())

print(num_stones_after_blinking(25, my_stones))
print(num_stones_after_blinking(75, my_stones))
