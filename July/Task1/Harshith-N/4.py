def decimal_to_octal(decimal):
    if decimal == 0:
        return 0

    octa_num = []

    while decimal > 0:
        remainder = decimal % 8
        octa_num.insert(0, str(remainder))
        decimal = decimal // 8

    octa_number = ''.join(octa_num)
    return octa_number


# Example usage
decimal_number = int(input("Enter a decimal number: "))
octa_number = decimal_to_octal(decimal_number)
print("Octa number:", octa_number)

# OUTPUT
# Enter a decimal number: 100
# Octa number: 144
