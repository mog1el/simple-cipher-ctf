LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#Opening the file with a message and remembering the message as msg
with open('encrypted_message', 'r') as file:
    msg = file.read()

def caesar_cipher_decoder(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
    #changing every char one at a time
        if char.isalpha():
            char_code = ord(char)
            decrypted_char = chr((char_code - shift - ord('a')) % 26 + ord('a'))
            plaintext += decrypted_char
    print(plaintext)

#Bruteforcing all the changes and looking fot he one that somehow makes any sense as encrypted message has to make some sense
for i in range(1, 27):
    caesar_cipher_decoder(msg, i)