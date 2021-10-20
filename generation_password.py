import random


def generation_passwort(lengh, chars):
    return random.sample(chars, lengh)


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
chars = ''

counter_password = int(input('Введите количество паролей для генерации: '))
lengh = int(input('Введите длину пароля: '))

num = input('Включать ли цифры 1234567890? Введите да или нет: ')
alpha = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? Введите да или нет: ')
alpha_lower = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? Введите да или нет:')
sim = input('Включать ли символы !#$%&*+-=?@^_? Введите да или нет: ')
iskl = input('Исключать ли неоднозначные символы il1Lo0O? Введите да или нет: ')

if num.lower() == 'да':
    chars += '1234567890'
if alpha.lower() == 'да':
    chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
if alpha_lower.lower() == 'да':
    chars += 'abcdefghijklmnopqrstuvwxyz'
if sim == 'да':
    chars += '!#$%&*+-=?@^_?'
if iskl == 'да':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')

for i in range(1, counter_password + 1):
    print(i, '  ', end=' ')
    print(*generation_passwort(lengh, chars), sep='')
