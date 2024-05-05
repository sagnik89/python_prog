alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n") 
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



def encrypt(text, shift):
    encrypted_word = ""
    for letters in text:

        # Ascii of a -> 97
        # Ascii of z -> 122
        # This does not handle the case of a and z edge cases
        new_ascii = ord(letters) + shift

        if new_ascii > 122:
            new_ascii = new_ascii - 122 + 96

        encrypted_word += chr(new_ascii)
    return encrypted_word


def decrypt(text, shift):
    decrypted_word = ""
    for letters in text:

        # Ascii of a -> 97
        # Ascii of z -> 122
        # This does not handle the case of a and z edge cases
        new_ascii = ord(letters) - shift

        if new_ascii < 97:
            new_ascii = 122 - (96 - new_ascii)

        decrypted_word += chr(new_ascii)
    return decrypted_word


if direction == "encode":
    print(encrypt(text, shift))
else:
    print(decrypt(text, shift))

