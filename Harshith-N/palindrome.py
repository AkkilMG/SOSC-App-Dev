def is_palindrome(string):
    string = string.replace(" ", "").lower()

    len = len(string)
    for i in range(len // 2):
        if string[i] != string[len - i - 1]:
            return False
    return True


str = input("Enter a string: ")

if is_palindrome(str):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

# OUTPUT
# Enter a string: malayalam
# The string is a palindrome.
