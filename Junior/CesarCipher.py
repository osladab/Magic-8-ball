ru_al_up = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
ru_al_lo = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
en_al_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
en_al_lo = 'abcdefghijklmnopqrstuvwxyz'



def cipher(text, lang):
    res = ''

    if lang == 'ru':
        for c in text:
            if c.isalpha():
                if c.isupper():
                    res += ru_al_cifr_up[ru_al_up.find(c) % 32]
                elif c.islower():
                    res += ru_al_cifr_lo[ru_al_lo.find(c) % 32]
            else:
                res = res + c
        return res

    elif lang == 'en':
        for c in text:
            if c.isalpha():
                if c.isupper():
                    res += en_al_cifr_up[en_al_up.find(c) % 26]
                elif c.islower():
                    res += en_al_cifr_lo[en_al_lo.index(c) % 26]

            else:
                res = res + c
        return res


def decipher(text, lang):
    res = ''

    if lang == 'ru':
        for c in text:
            if c.isalpha():
                if c.isupper():
                    res += ru_al_up[ru_al_cifr_up.index(c) % 32]
                elif c.islower():
                    res += ru_al_lo[ru_al_cifr_lo.index(c) % 32]
            else:
                res = res + c
        return res

    elif lang == 'en':
        for c in text:
            if c.isalpha():
                if c.isupper():
                    res += en_al_up[en_al_cifr_up.index(c) % 32]
                elif c.islower():
                    res += en_al_lo[en_al_cifr_lo.index(c) % 32]
            else:
                res = res + c
        return res

def lang_detect(text):
    for c in text:
        if ord(c.upper()) in range(65, 91):
            return 'en'
        elif ord(c.upper()) in range(1040, 1072):
            return 'ru'
        else:
            continue


print('Welcome to Caesar Cipher machine!')
cont = 'y'
while cont.lower() == 'y':
    print('Do you want to encode or decode text? For encode enter "e", for decode enter "d".')
    action = input().lower().strip()
    print('What text do you want to encode/decode?')
    text = input().strip()
    print('Enter shift for coding.')
    shift = int(input().strip())

    lang = lang_detect(text)

    if lang == 'ru': #зашифрованный со сдвигом shift русский алфавит
        ru_al_cifr_up = ''
        for c in ru_al_up:
            ru_al_cifr_up += ru_al_up[(ru_al_up.index(c) + shift) % 32]
        ru_al_cifr_lo = ''
        for c in ru_al_lo:
            ru_al_cifr_lo += ru_al_lo[(ru_al_lo.index(c) + shift) % 32]

    elif lang == 'en':#зашифрованный со сдвигом shift англ алфавит
        en_al_cifr_up = ''
        for c in en_al_up:
            en_al_cifr_up += en_al_up[(en_al_up.index(c) + shift) % 26]
        en_al_cifr_lo = ''
        for c in en_al_lo:
            en_al_cifr_lo += en_al_lo[(en_al_lo.index(c) + shift) % 26]


    if action == 'e':
        print(cipher(text, lang))
    elif action == 'd':
        print(decipher(text, lang))

    print('Do you want to continue? y/n')
    cont = input().strip()
print('Goodbye!')

