print('ЗАШИФРУЙ ТЕКСТ ШИФРОМ ЦЕЗАРЯ')
def togo():
    to = input('Выберите направление шифрование или дештфрование. Введите шифрование("ш") или дешифрование("д": ')
    while to.lower() not in ('ш', 'д'):
        print('Введите ш или д')
        to = input('Выберите направление шифрование или дештфрование. Введите шифрование("ш") или дешифрование("д": ')
    return to


def lang():
    l = input('Язык русский или английский? Введите "ру" или "en": ')
    while l.lower() not in ('ру', 'en'):
        print('Введите ру или en')
        l = input('Язык русский или английский? Введите "ру" или "en": ')
    return l


def step():
    st = input('Количество сдвигов вправо? Введите целое число: ')
    while st.isdigit() == False:
        print('Введите число')
        st = input('Количество сдвигов вправо? Введите целое число: ')
    return int(st)


t = togo()
l1 = lang()
s1 = step()


s = input('Введите текст: ')


if t == 'ш' and l1 == 'ру':
    sp = []
    for i in s:
        if 1072 <= ord(i) <= 1103:
            shifr = ord(i) + s1
            if shifr > ord('я'):
                shifr = 1071 + (shifr - 1103)
            sp.append(chr(shifr))
        else:
            sp.append(i)
    print(''.join(sp))
if t == 'ш' and l1 == 'en':
    sp = []
    for i in s:
        if 97 <= ord(i) <= 122:
            shifr = ord(i) + s1
            if shifr > ord('z'):
                shifr = 96 + (shifr - 122)
            sp.append(chr(shifr))
        else:
            sp.append(i)
    print(''.join(sp))
if t == 'д' and l1 == 'ру':
    sp = []
    for i in s:
        if 1072 <= ord(i) <= 1103:
            shifr = ord(i) - s1
            if shifr > ord('я'):
                shifr = 1071 + (shifr - 1103)
            sp.append(chr(shifr))
        else:
            sp.append(i)
    print(''.join(sp))
if t == 'д' and l1 == 'en':
    sp = []
    for i in s:
        if 97 <= ord(i) <= 122:
            shifr = ord(i) - s1
            if shifr > ord('z'):
                shifr = 96 + (shifr - 122)
            sp.append(chr(shifr))
        else:
            sp.append(i)
    print(''.join(sp))


