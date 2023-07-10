def print_pattern(rows):
    alphabet = 65 
    count = 1
    for i in range(rows):
        for j in range(i+1):
            print(chr(alphabet), end=" ")
            alphabet += 1
            count += 1
        print()
print_pattern(5)


"""OutPut:
A 
B C 
D E F 
G H I J 
K L M N O """