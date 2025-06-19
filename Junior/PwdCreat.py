import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
similar_chars = 'il1Lo0O'
chars = ''

def generate_passwords(length, chars):
    pwd = ''
    for i in range(length):
        pwd += random.choice(chars)
    return pwd

def similar_chars_replace(text):
    for c in text:
        if c in similar_chars:
            text = text.replace(c, '')
            return text

print('Welcome to password generator!')
print('--------------------------------')
print('Please, select options:')


contin = 'y'

while contin == 'y':


    print('How many passwords do you want to generate?')
    count_pwd = int(input())

    print ('How long do they need to be?')
    pwd_len = int(input())

    print('Do you want to use lowercase letters? y/n')
    use_L_let = input().lower()
    if use_L_let == 'y':
        chars += lowercase_letters

    print('Do you want to use upppercase letters? y/n')
    use_U_let = input().lower()
    if use_U_let == 'y'.lower():
        chars += uppercase_letters

    print('Do you want to use numbers? y/n')
    use_nums = input().lower()
    if use_nums == 'y':
        chars += digits

    print('Do you want to use special characters? y/n')
    use_punct = input().lower()
    if use_punct == 'y':
        chars += punctuation

    print('Do you want to exclude similar characters (il1Lo0O)? y/n?')
    use_similar = input().lower()
    if use_similar == 'y':
        chars = similar_chars_replace(chars)

    for i in range(count_pwd):
        print(generate_passwords(pwd_len, chars))

    print('Do you want to repeat? y/n')
    contin = input().lower()
    if contin == 'n':
        print('Goodbye!')






