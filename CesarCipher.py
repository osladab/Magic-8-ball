def cipher(text, shift, lang):
    res = ''
    
    if lang == 'ru':
        for c in text:
            if c.isalpha():
                res = res + chr((ord(c) + shift) % 32)
            else:
                res = res + c
        return res
        
    elif lang == 'en':
        for c in text:
            if c.isalpha():
                res = res + chr((ord(c) + shift) % 26)
            else:
                res = res + c
        return res

def decipher(text, shift, lang):
    res = ''
    
    if lang == 'ru':
        for c in text:
            if c.isalpha():
                res = res + chr((ord(c) - shift) % 32)
            else:
                res = res + c
        return res
        
    elif lang == 'en':
        for c in text:
            if c.isalpha():
                res = res + chr((ord(c) - shift) % 26)
            else:
                res = res + c
        return res

def lang_detect(text):
    #ru = 'ru'
    #en = 'en'
    for c in text:
        if ord(c.upper()) in range(65, 91):
            return 'en'
        elif ord(c.ypper()) in range(1040, 1072):
            return 'ru'
        else:
            continue

print('Welcome to Caesar CIpher machine!')
cont = 'y'
while cont.lower == 'y':
    print('Do you want to encode or decode text? For encode enter "e", for decode enter "d"')
    action = input()
    print('What text do you want to encode/decode?')
    text = input()
    print('Enter shift for coding.')
    shift = int(input())

    lang = lang_detect(text)

    if action.lower == 'e':
        print(cipher(text, shift, lang))
    elif action.lower == 'd':
        print(decipher(text, shift, lang))

    print('Do you want to continue? y/n')
    cont = input()
