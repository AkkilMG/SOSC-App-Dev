def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text


plaintext = input("Enter a Plain Text :")
shift = int(input("Enter the shift :"))
ciphertext = caesar_cipher(plaintext, shift)
print("Ciphertext:", ciphertext)


"""OutPut:
Enter a Plain Text :Hello, World!
Enter the shift :3
Ciphertext: Khoor, Zruog!  """