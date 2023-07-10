def deci_to_oct(decimal):
    octa = ""
    while decimal > 0:
        remainder = decimal % 8
        octa = str(remainder) + octa
        decimal = decimal // 8
    return octa

input = int(input("Enter a decimal number: "))

output = deci_to_oct(input)

print("Octal representation:", output)


"""OutPut:
Enter a decimal number: 45
Octal representation: 55"""