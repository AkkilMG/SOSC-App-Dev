def print_pattern(n):
    for i in range(1, n + 1):
        letter = chr(ord('A') + i - 1)
        line = letter + ' ' * (i - 1)
        print(line * i)


num_lines = 4
print_pattern(num_lines)

# OUTPUT
# A
# B B
# C  C  C
# D   D   D   D
