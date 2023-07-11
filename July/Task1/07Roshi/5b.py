def print_pattern(rows):
    num = 1
    for i in range(rows):
        for j in range(i+1):
            print(num, end=" ")
            num += 1
        print()
print_pattern(4)


"""OutPut:
1 
2 3 
4 5 6 
7 8 9 10 """