import random


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
chars = ''


def counter_password():
    counter_password = input('Введите количество паролей для генерации: ')
    while counter_password.isdigit() == False:
        print('Нужно ввести цифру')
        counter_password = input('Введите количество паролей для генерации: ')
    return int(counter_password)


def lengh():
    lengh = input('Введите длину пароля: ')
    while lengh.isdigit() == False:
        print('Нужно ввести цифру')
        lengh = input('Введите длину пароля: ')
    return int(lengh)


def num():
    num = input('Включать ли цифры 1234567890? Введите да или нет: ')
    while num.lower() not in ('да','нет'):
        print('Нужно ввести да или нет')
        num = input('Включать ли цифры 1234567890? Введите да или нет: ')
    return num


def alpha():
    alpha = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? Введите да или нет: ')
    while alpha.lower() not in ['да', 'нет']:
        print('Введите да или нет')
        alpha = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? Введите да или нет: ')
    return alpha


def alpha_lower():
    alpha_lower = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? Введите да или нет:')
    while alpha_lower.lower() not in ('да', 'нет'):
        print('Введите да или нет')
        alpha_lower = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? Введите да или нет:')
    return alpha_lower


def sim():
    sim = input('Включать ли символы !#$%&*+-=?@^_? Введите да или нет: ')
    while sim.lower() not in ('да', 'нет'):
        print('Введите да или нет')
        sim = input('Включать ли символы !#$%&*+-=?@^_? Введите да или нет: ')
    return sim


def iskl():
    iskl = input('Исключать ли неоднозначные символы il1Lo0O? Введите да или нет: ')
    while iskl.lower() not in ('да', 'нет'):
        print('Введите да или нет')
        iskl = input('Исключать ли неоднозначные символы il1Lo0O? Введите да или нет: ')
    return iskl


def generation_passwort(lengh, chars):
    return random.sample(chars, lengh)


#СТАРТ ПРОГРАММЫ


c = counter_password()
l = lengh()
n = num()
a = alpha()
a1 = alpha_lower()
s = sim()
i = iskl()


if n == 'да':
    chars += '1234567890'
if a == 'да':
    chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
if a1 == 'да':
    chars += 'abcdefghijklmnopqrstuvwxyz'
if s == 'да':
    chars += '!#$%&*+-=?@^_?'
if i == 'да':
    for j in 'il1Lo0O':
        chars = chars.replace(j, '')


for i in range(1, c+1):
    print(i, '  ', end=' ')
    print(*generation_passwort(l, chars), sep='')
