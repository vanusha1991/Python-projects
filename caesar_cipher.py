def continue_again(start):
    if start == 1:
        return 1
    elif start == 2:
        print('Goodbye.')
        return 2


def decryption_unknown_shift():
    language = input('en or ru = ')
    words = list(input('Enter text here '))

    if language == 'en':
        for j in range(1, 26):
            print('Key', j)

            for i in words:
                if i not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                    print(i, end='')

                elif 'a' <= i <= 'z' and ord(i) - j > 96:
                    print(chr(ord(i) - j), end='')

                elif 'A' <= i <= 'Z' and ord(i) - j > 64:
                    print(chr(ord(i) - j), end='')

                else:
                    print(chr(ord(i) - j + 26), end='')
            print()

    elif language == 'ru':
        for j in range(1, 33):
            print('Key', j)

            for i in words:
                if i not in 'абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ':
                    print(i, end='')

                elif 'а' <= i <= 'я' and ord(i) - j > 1071:
                    print(chr(ord(i) - j), end='')

                elif 'А' <= i <= 'Я' and ord(i) - j > 1039:
                    print(chr(ord(i) - j), end='')

                else:
                    print(chr(ord(i) - j + 32), end='')
            print()


def decryption():
    language = input('en or ru = ')
    shift_left = int(input('shift = '))
    words = list(input('Enter text here '))

    if language == 'en':
        for i in words:
            if i not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                print(i, end='')

            elif 'a' <= i <= 'z' and ord(i) - shift_left > 96:
                print(chr(ord(i) - shift_left), end='')

            elif 'A' <= i <= 'Z' and ord(i) - shift_left > 64:
                print(chr(ord(i) - shift_left), end='')

            else:
                print(chr(ord(i) - shift_left + 26), end='')
        print()

    elif language == 'ru':
        for i in words:
            if i not in 'абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ':
                print(i, end='')

            elif 'а' <= i <= 'я' and ord(i) - shift_left > 1071:
                print(chr(ord(i) - shift_left), end='')

            elif 'А' <= i <= 'Я' and ord(i) - shift_left > 1039:
                print(chr(ord(i) - shift_left), end='')

            else:
                print(chr(ord(i) - shift_left + 32), end='')
        print()


def selective_encryption():
    language = input('en or ru = ')
    shift_selective = int(input('shift = '))
    words = list(input('Enter text here '))

    if language == 'en':
        for i in words:
            if i not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                print(i, end='')

            elif 'a' <= i <= 'z' and ord(i) + shift_selective < 123:
                print(chr(ord(i) + shift_selective), end='')

            elif 'A' <= i <= 'Z' and ord(i) + shift_selective < 91:
                print(chr(ord(i) + shift_selective), end='')

            else:
                print(chr(ord(i) + shift_selective - 26), end='')
        print()

    elif language == 'ru':
        for i in words:
            if i not in 'абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ':
                print(i, end='')

            elif 'а' <= i <= 'я' and ord(i) + shift_selective < 1104:
                print(chr(ord(i) + shift_selective), end='')

            elif 'А' <= i <= 'Я' and ord(i) + shift_selective < 1072:
                print(chr(ord(i) + shift_selective), end='')

            else:
                print(chr(ord(i) + shift_selective - 32), end='')
        print()


def standart_encryption():
    print('Standard mode performs encryption with 3 character shifts to the right.'
          '\nNumbers and signs are not affected.')

    shift_standart = 3
    language = input('en or ru = ')
    words = list(input('Enter text here '))

    if language == 'en':
        for i in words:
            if i not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                print(i, end='')

            elif 'a' <= i <= 'z' and ord(i) + shift_standart < 123:
                print(chr(ord(i) + shift_standart), end='')

            elif 'A' <= i <= 'Z' and ord(i) + shift_standart < 91:
                print(chr(ord(i) + shift_standart), end='')

            else:
                print(chr(ord(i) + shift_standart - 26), end='')
        print()

    elif language == 'ru':
        for i in words:
            if i not in 'абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ':
                print(i, end='')

            elif 'а' <= i <= 'я' and ord(i) + shift_standart < 1104:
                print(chr(ord(i) + shift_standart), end='')

            elif 'А' <= i <= 'Я' and ord(i) + shift_standart < 1072:
                print(chr(ord(i) + shift_standart), end='')

            else:
                print(chr(ord(i) + shift_standart - 32), end='')
        print()


def caesar_cipher_main():
    cycle_break = continue_again(int(input('Start? Yes = 1, No = 2\nprint here ')))

    while True:

        if cycle_break == 2:
            break
        choice_method = int(input('Encryption or Decryption?\nEncryption = 1, Decryption = 2\nprint here '))

        if choice_method == 1:
            choice_mode = int(input('Standart or Selective?\nStandart = 1, Selective = 2\nprint here '))

            if choice_mode == 1:
                standart_encryption()
                cycle_break = continue_again(int(input('Decryption finished\nRepeat? Yes = 1, No = 2\nprint here ')))

            elif choice_mode == 2:
                selective_encryption()
                cycle_break = continue_again(int(input('Decryption finished\nRepeat? Yes = 1, No = 2\nprint here ')))

        elif choice_method == 2:
            choice_mode = int(input('I know the key = 1, I don"t know the key = 2\nprint here '))

            if choice_mode == 1:
                decryption()
                cycle_break = continue_again(int(input('Decryption finished\nRepeat? Yes = 1, No = 2\nprint here ')))

            elif choice_mode == 2:
                decryption_unknown_shift()
                cycle_break = continue_again(int(input('Decryption finished\nRepeat? Yes = 1, No = 2\nprint here ')))


print('Welcome to Caesar Cipher (encoder/decoder)')

caesar_cipher_main()
