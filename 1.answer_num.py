import random

print('Добро пожаловать в числовую угадайку')


def max_range():
    while True:
        n = input('Назовите диапозон от 1 до какого числа хотите угадать: ')
        if not n.isdigit() or int(n) < 1:
            print('Введите число от 1')
            continue
        return int(n)


q = max_range()
num = random.randrange(1, q)


def get_num():
    while True:
        s = input(f'Угадайте число от 1 до {q}: ')
        if not s.isdigit() or int(s) < 1 or int(s) > q:
            print(f'Может введете все таки число от 1 до {q}?')
            continue
        return int(s)


def game():
    x, counter = 0, 1
    while x != num:
        x = get_num()
        if x < num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            counter += 1
            continue
        elif x > num:
            print('Ваше число больше загаданного, попробуйте еще разок')
            counter += 1
            continue
        print('Вы угадали, поздравляем!')
        print('Количество попыток', counter)


while True:
    game()
    print('Отлична игра еще разок?')
    answer = input("'Да' или 'Y' если хотите продолжить: ")
    if answer.lower() in ('да', 'y'):
        q = max_range()
        num = random.randrange(1, q)
        continue
    else:
        break

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
