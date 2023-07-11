def print_pattern(n):
    for i in range(n):
        print(" " * i + "* " * (n - i))


print_pattern(4)

# OUTPUT
# * * * *
# * * *
#  * *
#   *
