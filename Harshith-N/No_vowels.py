def replace_first_vowel(string):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowel_index = []

    for i in range(len(string)):
        if string[i].lower() in vowels:
            vowel_index.append(i)
            break

    if vowel_index:
        index = vowel_index[0]
        new_string = string[:index] + '-' + string[index+1:]
    else:
        new_string = string

    return new_string


input_str = input("Enter a string: ")

new_string = replace_first_vowel(input_str)
print("Modified string:", new_string)

# OUTPUT
# Enter a string: Harshith
# Modified string: H-rshith
