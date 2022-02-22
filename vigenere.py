def encrypt_vigenere(plaintext, keyword):
    dict_lower = {}
    dict_upper = {}

    if plaintext.islower():
        dict_lower = {chr(letter): letter - 97 for letter in range(ord('a'), ord('z') + 1)}
    else:
        dict_upper = {chr(letter): letter - 65 for letter in range(ord('A'), ord('Z') + 1)}

    if len(plaintext) > len(keyword):
        keyword = (keyword * ((len(plaintext) - len(keyword)) // 2))[:len(plaintext)]

    for i in range(len(keyword)):
        if 'a' <= plaintext[i] <= 'z' and ord(plaintext[i]) + dict_lower.get(keyword[i]) < 123:
            print(chr(ord(plaintext[i]) + dict_lower.get(keyword[i])), end='')

        elif 'A' <= plaintext[i] <= 'Z' and ord(plaintext[i]) + dict_upper.get(keyword[i]) < 91:
            print(chr(ord(plaintext[i]) + dict_upper.get(keyword[i])), end='')

        elif 'a' <= plaintext[i] <= 'z':
            print(chr(ord(plaintext[i]) + dict_lower.get(keyword[i]) - 26), end='')

        elif 'A' <= plaintext[i] <= 'Z':
            print(chr(ord(plaintext[i]) + dict_upper.get(keyword[i]) - 26), end='')
    print()


def decrypt_vigenere(ciphertext, keyword):
    dict_lower = {}
    dict_upper = {}

    if ciphertext.islower():
        dict_lower = {chr(letter): letter - 97 for letter in range(ord('a'), ord('z') + 1)}
    else:
        dict_upper = {chr(letter): letter - 65 for letter in range(ord('A'), ord('Z') + 1)}

    if len(ciphertext) > len(keyword):
        keyword = (keyword * ((len(ciphertext) - len(keyword)) // 2))[:len(ciphertext)]

    for i in range(len(keyword)):
        if 'a' <= ciphertext[i] <= 'z' and ord(ciphertext[i]) - dict_lower.get(keyword[i]) > 96:
            print(chr(ord(ciphertext[i]) - dict_lower.get(keyword[i])), end='')

        elif 'A' <= ciphertext[i] <= 'Z' and ord(ciphertext[i]) - dict_upper.get(keyword[i]) > 64:
            print(chr(ord(ciphertext[i]) - dict_upper.get(keyword[i])), end='')

        elif 'a' <= ciphertext[i] <= 'z':
            print(chr(ord(ciphertext[i]) - dict_lower.get(keyword[i]) + 26), end='')

        elif 'A' <= ciphertext[i] <= 'Z':
            print(chr(ord(ciphertext[i]) - dict_upper.get(keyword[i]) + 26), end='')
    print()


def vigenere_main():
    method = int(input('Encrypt or Decrypt?\nEncrypt = 1, Decrypt = 2\nprint here '))

    if method == 1:
        encrypt_vigenere(input('print here text '), input('print here Key '))
    elif method == 2:
        decrypt_vigenere(input('print here text '), input('print here Key '))


print('Welcome to Vigenere Cipher (encoder/decoder)')
vigenere_main()
