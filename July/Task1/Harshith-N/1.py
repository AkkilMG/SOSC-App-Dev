def remove_duplicate(array):
    return list(set(array))


str = input("enter the numbers from 1-9 and repeat some numbers: ")
num = list(map(int, str.split()))

non_repeated_num = remove_duplicate(num)
print("The non repeated numbers are: ", non_repeated_num)

# Output is :
# enter the numbers from 1-9 and repeat some numbers: 1 2 2 3 4 5 5 6 7 8 9 9
# The non repeated numbers are:  [1, 2, 3, 4, 5, 6, 7, 8, 9]
