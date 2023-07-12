def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            shifted_char = chr(
                (ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text


plaintext = "Hello, World!"
shift = 3

encrypted_text = caesar_cipher(plaintext, shift)
print("Encrypted text:", encrypted_text)

decrypted_text = caesar_cipher(encrypted_text, -shift)
print("Decrypted text:", decrypted_text)

# OUTPUT
# Encrypted text: Khoor, Zruog!
# Decrypted text: Hello, World!
