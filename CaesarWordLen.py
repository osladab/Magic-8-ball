#Шифрование Цезарем со сдвигом на длину каждого слова без знаков препинания
en_al_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
en_al_lo = 'abcdefghijklmnopqrstuvwxyz'
def cifr(word):
    word_lst = [w for w in word if w.isalpha()]# список из только букв в word
    word_len = ''.join(word_lst)# слово только из букв

    #шифрование алфавита со сдвигом на длину слова
    en_al_cifr_up = ''
    for c in en_al_up:
        en_al_cifr_up += en_al_up[(en_al_up.index(c) + len(word_len)) % 26]
    en_al_cifr_lo = ''
    for c in en_al_lo:
        en_al_cifr_lo += en_al_lo[(en_al_lo.index(c) + len(word_len)) % 26]

    res = ''
    for c in word:
        if c.isalpha():#если "с" буква то шифруется и плюсуетсяк возвращаемому значению
            if c.isupper():
                res += en_al_cifr_up[en_al_up.index(c) % 26]
            elif c.islower():
                res += en_al_cifr_lo[en_al_lo.index(c) % 26]
        else:#если не буква - плюс к возврату
            res = res + c
    return res

text = input()

txt_lst = text.split()
for w in txt_lst:
    print(cifr(w), end = ' ')