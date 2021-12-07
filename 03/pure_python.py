# Part 1

with open('input') as f:
    codes = f.read().splitlines()

no_codes = len(codes)
code_length = len(codes[0])

gamma_rate = ''
epsilon_rate = ''

def count_bits(codes, pos):
    return sum([int(code[pos]) for code in codes])

for i in range(code_length):
    no_ones = count_bits(codes, i)
    gamma_rate += str(int(no_ones >= no_codes / 2))
    epsilon_rate += str(int(no_ones < no_codes / 2))

print(int(gamma_rate, 2) * int(epsilon_rate, 2))

# Part 2
def find_code(codes, pos, comparator):
    if len(codes) > 1:
        bit = comparator(count_bits(codes, pos), len(codes) / 2)
        new_codes = [code for code in codes if code[pos] == str(int(bit))]
        print(len(new_codes))
        return find_code(new_codes, pos + 1, comparator)
    else:
        return codes[0]

gamma_rate = find_code(codes, 0, lambda x, y: x >= y)
epsilon_rate = find_code(codes, 0, lambda x, y: x < y)

print(int(gamma_rate, 2) * int(epsilon_rate, 2))
