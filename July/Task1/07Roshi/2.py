def replace_1st_vowel(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in string:
        if char.lower() in vowels:
            return string.replace(char, '-')
    return string


input = input("Enter a string: ")


result = replace_1st_vowel(input)

print("String after replacing the first vowel with '-' :", result)


"""OutPut:
Enter a string: Roshith
String after replacing the first vowel with '-' : R-shith"""