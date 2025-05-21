ru_alph = ''
for i in range(1040, 1104):
    ru_alph += chr(i)

en_alph = ''
for i in range(65, 91):
    en_alph += chr(i)
en_alph += en_alph.lower()

def cipher(text, shift, lang):



    res = ''

    if lang == 'ru':
        for c in text:
            if c.isalpha():
                res += ru_al_cifr[ru_alph.index(c) % 64]
            else:
                res = res + c
        return res

    elif lang == 'en':
        for c in text:
            if c.isalpha():
                res += en_al_cifr[en_alph.find(c) % 52]
            else:
                res = res + c
        return res


def decipher(text, shift, lang):
    res = ''

    if lang == 'ru':
        for c in text:
            if c.isalpha():
                res += ru_alph[ru_al_cifr.index(c) % 64]
            else:
                res = res + c
        return res

    elif lang == 'en':
        for c in text:
            if c.isalpha():
                res += en_alph[en_al_cifr.find(c) % 52]
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

    if lang == 'ru':
    #зашифрованный со сдвигом shift русский алфавит
        ru_al_cifr = ''
        for c in ru_alph:
            ru_al_cifr += ru_alph[(ru_alph.index(c) + shift) % 64]
    elif lang == 'en':
    #зашифрованный со сдвигом shift англ алфавит
        en_al_cifr = ''
        for c in en_alph:
            en_al_cifr += en_alph[(en_alph.index(c) + shift) % 52]


    if action == 'e':
        print(cipher(text, shift, lang))
    elif action == 'd':
        print(decipher(text, shift, lang))

    print('Do you want to continue? y/n')
    cont = input().strip()
print('Goodbye!')

