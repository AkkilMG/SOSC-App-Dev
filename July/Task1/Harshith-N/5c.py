def print_pattern(n):
    char = ord('A')
    for i in range(1, n + 1):
        for j in range(i):
            print(chr(char), end=' ')
            char += 1
        print()


print_pattern(5)

# OUTPUT
# A
# B C
# D E F
# G H I J
# K L M N O
