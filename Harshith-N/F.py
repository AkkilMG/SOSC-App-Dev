def print_pattern(n):
    for i in range(n):
        print("  " * (n - i - 1) + "* " * (i + 1))


print_pattern(4)

# OUTPUT
#     *
#    * *
#  * * *
# * * * *
