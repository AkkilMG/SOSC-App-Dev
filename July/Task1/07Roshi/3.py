def is_palindrome(string):
    string = string.replace(" ", "").lower()
    
    if string == string[::-1]:
        return True
    else:
        return False

input = input("Enter a string: ")


if is_palindrome(input):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

"""OutPut:
Enter a string: Malayalam
The string is a palindrome."""