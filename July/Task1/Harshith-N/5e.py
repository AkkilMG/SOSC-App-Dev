def print_pattern(n):
    for i in range(n):
        print(" " * (n - i - 1) + "* " * (i + 1))
    for i in range(n - 1):
        print(" " * (i + 1) + "* " * (n - i - 1))


print_pattern(3)

# OUTPUT
#  *
# * *
# * * *
# * *
#  *
