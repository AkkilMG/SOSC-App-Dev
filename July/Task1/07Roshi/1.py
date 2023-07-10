def remove_duplicates(arr):
    return list(set(arr))

input = input("Enter the elements of the array :")
array = list(map(int,input.split()))


result = remove_duplicates(array)


print("Array after Removing Duplicates :", result)





"""OutPut:
Enter the elements of the array :1 2 2 3 4 4 5 6 7 6 8
Array after Removing Duplicates : [1, 2, 3, 4, 5, 6, 7, 8]"""

