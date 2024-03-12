print('Крестики-Нолики')
print('_______________')

import random

res = None

a = [1, '-', '-', '-']
b = [2, '-', '-', '-']
c = [3, '-', '-', '-']
field = f'   1 2 3\n {a[0]} {a[1]} {a[2]} {a[3]}\n {b[0]} {b[1]} {b[2]} {b[3]}\n {c[0]} {c[1]} {c[2]} {c[3]}'
def hod_x(p):
    if p // 10 == 1 and a[p % 10] != '-':
        print('поле занято!')
        hod_player_1 = int(input(f'{name_player_1}, введите номер поля для "x": '))
        hod_x(hod_player_1)
    elif p // 10 == 1 and a[p % 10] == '-':
        a[p % 10] = 'x'
        field = f'   1 2 3\n {a[0]} {a[1]} {a[2]} {a[3]}\n {b[0]} {b[1]} {b[2]} {b[3]}\n {c[0]} {c[1]} {c[2]} {c[3]}'
        print(field)
    if p // 10 == 2 and b[p % 10] != '-':
        print('поле занято!')
        hod_player_1 = int(input(f'{name_player_1}, введите номер поля для "x": '))
        hod_x(hod_player_1)
    elif p // 10 == 2 and b[p % 10] == '-':
        b[p % 10] = 'x'
        field = f'   1 2 3\n {a[0]} {a[1]} {a[2]} {a[3]}\n {b[0]} {b[1]} {b[2]} {b[3]}\n {c[0]} {c[1]} {c[2]} {c[3]}'
        print(field)
    if p // 10 == 3 and c[p % 10] != '-':
        print('поле занято!')
        hod_player_1 = int(input(f'{name_player_1}, введите номер поля для "x": '))
        hod_x(hod_player_1)
    elif p // 10 == 3 and c[p % 10] == '-':
        c[p % 10] = 'x'
        field = f'   1 2 3\n {a[0]} {a[1]} {a[2]} {a[3]}\n {b[0]} {b[1]} {b[2]} {b[3]}\n {c[0]} {c[1]} {c[2]} {c[3]}'
        print(field)

def hod_o(p):
    if p // 10 == 1 and a[p % 10] != '-':
        print('поле занято!')
        hod_player_2 = int(input(f'{name_player_2}, введите номер поля для "o": '))
        hod_o(hod_player_2)
    elif p // 10 == 1 and a[p % 10] == '-':
        a[p % 10] = 'o'
        field = f'   1 2 3\n {a[0]} {a[1]} {a[2]} {a[3]}\n {b[0]} {b[1]} {b[2]} {b[3]}\n {c[0]} {c[1]} {c[2]} {c[3]}'
        print(field)
    if p // 10 == 2 and b[p % 10] != '-':
        print('поле занято!')
        hod_player_2 = int(input(f'{name_player_2}, введите номер поля для "o": '))
        hod_o(hod_player_2)
    elif p // 10 == 2 and b[p % 10] == '-':
        b[p % 10] = 'o'
        field = f'   1 2 3\n {a[0]} {a[1]} {a[2]} {a[3]}\n {b[0]} {b[1]} {b[2]} {b[3]}\n {c[0]} {c[1]} {c[2]} {c[3]}'
        print(field)
    if p // 10 == 3 and c[p % 10] != '-':
        print('поле занято!')
        hod_player_2 = int(input(f'{name_player_2}, введите номер поля для "o": '))
        hod_o(hod_player_2)
    elif p // 10 == 3 and c[p % 10] == '-':
        c[p % 10] = 'o'
        field = f'   1 2 3\n {a[0]} {a[1]} {a[2]} {a[3]}\n {b[0]} {b[1]} {b[2]} {b[3]}\n {c[0]} {c[1]} {c[2]} {c[3]}'
        print(field)

def proverka_1():
    global res
    if player_1 > player_2:
        a_chk = 'x' in a and 'o' not in a and '-' not in a
        b_chk = 'x' in b and 'o' not in b and '-' not in b
        c_chk = 'x' in c and 'o' not in c and '-' not in c
        row_1_chk = a[1] == b[1] == c[1] == 'x'
        row_2_chk = a[2] == b[2] == c[2] == 'x'
        row_3_chk = a[3] == b[3] == c[3] == 'x'
        d_1_chk = a[1] == b[2] == c[3] == 'x'
        d_2_chk = a[3] == b[2] == c[1] == 'x'
        if a_chk or b_chk or c_chk or row_1_chk or row_2_chk or row_3_chk or d_1_chk or d_2_chk:
            res = True
            print(f'{name_player_1}, вы выиграли!')
        elif '-' not in field:
            print('ничья')
            print('ʕ ᵔᴥᵔ ʔ')
        else:
            hod_player_2 = int(input(f'{name_player_2}, введите номер поля для "o": '))
            hod_o(hod_player_2)
    else:
        a_chk = 'x' in a and 'o' not in a and '-' not in a
        b_chk = 'x' in b and 'o' not in b and '-' not in b
        c_chk = 'x' in c and 'o' not in c and '-' not in c
        row_1_chk = a[1] == b[1] == c[1] == 'x'
        row_2_chk = a[2] == b[2] == c[2] == 'x'
        row_3_chk = a[3] == b[3] == c[3] == 'x'
        d_1_chk = a[1] == b[2] == c[3] == 'x'
        d_2_chk = a[3] == b[2] == c[1] == 'x'
        if a_chk or b_chk or c_chk or row_1_chk or row_2_chk or row_3_chk or d_1_chk or d_2_chk:
            res = True
            print(f'{name_player_2}, вы выиграли!')
        elif '-' not in field:
            print('ничья')
            print('ʕ ᵔᴥᵔ ʔ')
        else:
            hod_player_2 = int(input(f'{name_player_1}, введите номер поля для "o": '))
            hod_o(hod_player_2)

def proverka_2():
    global res
    if player_1 > player_2:
        a_chk = 'o' in a and 'x' not in a and '-' not in a
        b_chk = 'o' in b and 'x' not in b and '-' not in b
        c_chk = 'o' in c and 'x' not in c and '-' not in c
        row_1_chk = a[1] == b[1] == c[1] == 'o'
        row_2_chk = a[2] == b[2] == c[2] == 'o'
        row_3_chk = a[3] == b[3] == c[3] == 'o'
        d_1_chk = a[1] == b[2] == c[3] == 'o'
        d_2_chk = a[3] == b[2] == c[1] == 'o'
        if a_chk or b_chk or c_chk or row_1_chk or row_2_chk or row_3_chk or d_1_chk or d_2_chk:
            res = True
            print(f'{name_player_2}, вы выиграли!')
        elif '-' not in field:
            print('ничья')
            print('ʕ ᵔᴥᵔ ʔ')
        else:
            hod_player_1 = int(input(f'{name_player_1}, введите номер поля для "х": '))
            hod_x(hod_player_1)
    else:
        a_chk = 'o' in a and 'x' not in a and '-' not in a
        b_chk = 'o' in b and 'x' not in b and '-' not in b
        c_chk = 'o' in c and 'x' not in c and '-' not in c
        row_1_chk = a[1] == b[1] == c[1] == 'o'
        row_2_chk = a[2] == b[2] == c[2] == 'o'
        row_3_chk = a[3] == b[3] == c[3] == 'o'
        d_1_chk = a[1] == b[2] == c[3] == 'o'
        d_2_chk = a[3] == b[2] == c[1] == 'o'
        if a_chk or b_chk or c_chk or row_1_chk or row_2_chk or row_3_chk or d_1_chk or d_2_chk:
            res = True
            print(f'{name_player_1}, вы выиграли!')
        elif '-' not in field:
            print('ничья')
            print('ʕ ᵔᴥᵔ ʔ')
        else:
            hod_player_1 = int(input(f'{name_player_2}, введите номер поля для "х": '))
            hod_x(hod_player_1)

name_player_1 = input('Введите имя первого игрока: ')
name_player_2 = input('Введите имя второго игрока: ')
player_1 = 0
player_2 = 0
while player_1 == player_2:
    player_1 = random.randint(1,100)
    player_2 = random.randint(1,100)
if player_1 > player_2:
    print(f'{name_player_1} играет за крестики.')
    print(f'{name_player_2} играет за нолики.')
    print(field)
    while '-' in field:
        proverka_2()
        field = f'   1 2 3\n {a[0]} {a[1]} {a[2]} {a[3]}\n {b[0]} {b[1]} {b[2]} {b[3]}\n {c[0]} {c[1]} {c[2]} {c[3]}'
        if res:
            break
        proverka_1()
        if res:
            break
        field = f'   1 2 3\n {a[0]} {a[1]} {a[2]} {a[3]}\n {b[0]} {b[1]} {b[2]} {b[3]}\n {c[0]} {c[1]} {c[2]} {c[3]}'
elif player_2 > player_1:
    print(f'{name_player_2} играет за крестики.')
    print(f'{name_player_1} играет за нолики.')
    print(field)
    while '-' in field:
        proverka_2()
        field = f'   1 2 3\n {a[0]} {a[1]} {a[2]} {a[3]}\n {b[0]} {b[1]} {b[2]} {b[3]}\n {c[0]} {c[1]} {c[2]} {c[3]}'
        if res:
            break
        proverka_1()
        field = f'   1 2 3\n {a[0]} {a[1]} {a[2]} {a[3]}\n {b[0]} {b[1]} {b[2]} {b[3]}\n {c[0]} {c[1]} {c[2]} {c[3]}'
        if res:
            break