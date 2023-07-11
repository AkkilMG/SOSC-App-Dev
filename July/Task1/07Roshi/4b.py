def deci_to_bin(decimal):
    binary = ""
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal = decimal // 2
    return binary

input = int(input("Enter a decimal number: "))

output = deci_to_bin(input)

print("Binary representation:", output)


"""OutPut:
Enter a decimal number: 45
Binary representation: 101101"""