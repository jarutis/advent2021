#!/usr/bin/env python3
count = 0
inf = 999

# Part 1
with open('input') as f:
    previous_depth = inf
    for line in f:
        depth = int(line)
        if depth > previous_depth:
            count += 1
        previous_depth = depth

print(count)

# Part 2
count = 0
buffer = []
with open('input') as f:
    previous_depth = inf
    for line in f:
        buffer.append(int(line))
        if len(buffer) == 3:
            depth = sum(buffer)
            if depth > previous_depth:
                count += 1
            previous_depth = depth
            buffer.pop(0)

print(count)
