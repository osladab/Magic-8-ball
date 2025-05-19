
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