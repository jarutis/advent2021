# Part 1
horizontal = 0
vertical = 0

with open('input') as f:
    for command in f:
        match command.split():
            case ["forward", x]: horizontal += int(x)
            case ["up", x]: vertical -= int(x)
            case ["down", x]: vertical += int(x)

print(horizontal * vertical)

# Part 2
horizontal = 0
vertical = 0
aim=0
with open('input') as f:
    for command in f:
        match command.split():
            case ["forward", x]:
                step = int(x)
                horizontal += step
                vertical += step*aim
            case ["up", x]: aim -= int(x)
            case ["down", x]: aim += int(x)

print(horizontal * vertical)
