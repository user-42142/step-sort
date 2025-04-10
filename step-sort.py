import matplotlib.pyplot as plt
import random
import bisect

# Shuffle the initial list
a = list(range(100))
random.shuffle(a)

# Initialize previous sorted list as empty
previous_sorted = []

while True:
    plt.figure()
    plt.bar(range(len(a)), a)
    plt.clf()

    sorted_part = []
    unsorted_part = []

    # Unsorted portion: only the elements from the current round
    current_round = a[:len(a) - len(previous_sorted)]

    for i in current_round:
        if not sorted_part:
            sorted_part.append(i)
            continue
        if i > sorted_part[-1]:
            sorted_part.append(i)
        else:
            unsorted_part.append(i)

    # Apply binary search on previous_sorted if it exists
    if previous_sorted:
        index = bisect.bisect_right(previous_sorted, sorted_part[-1])
        sorted_part.extend(previous_sorted[index:])
        unsorted_part.extend(previous_sorted[:index])

    a = unsorted_part + sorted_part
    previous_sorted = sorted_part[:]

    if len(sorted_part) == len(a):
        break
plt.show()
