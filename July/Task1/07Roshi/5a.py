def print_pattern(rows):
    for i in range(rows):
        for j in range(i+1):
            print(chr(65+i), end=" ")
        print()
print_pattern(4)


"""OutPut:
A 
B B 
C C C 
D D D D """