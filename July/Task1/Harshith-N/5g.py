def print_pattern(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()


print_pattern(4)

# OUTPUT
# 1 2 3 4
# 1 2 3
# 1 2
# 1
