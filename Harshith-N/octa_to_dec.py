def octa_to_decimal(octa):
    decimal = 0
    power = 0

    while octa != 0:
        digit = octa % 10
        decimal += digit * (8 ** power)
        octa //= 10
        power += 1

    return decimal


octa_number = input("Enter an octal number: ")
decimal_number = octa_to_decimal(int(octa_number))
print("Decimal number:", decimal_number)

# OUTPUT
# Enter an octal number: 144
# Decimal number: 100
