#определяем размеры поля
size = int(input('Введите размер поля: '))
field = [['-'] * size for i in range(size)]

#рисуем поле в консоли
def show_field():
    x = []
    y = 0
    for i in range(0, size):
        x.append(str(i))
    x_str = ' '.join(x)
    print('  ' + x_str)
    for i in range(len(field)):
        print(y, end = ' ')
        y += 1
        for j in range(len(field[i])):
            print(field[i][j], end = ' ')
        print()

#проверяем на условия победы, аргументом будет 'player', в зависимости от номера хода
def win(who_is_winner):
    # проверка построчно
    for i in range(size):
        count = 0
        for j in range(size):
            if field[i][j] == who_is_winner:
                count += 1
            if count == size:
                return True
    # проверка по столбцам
    for i in range(size):
        count = 0
        for j in range(size):
            if field[j][i] == who_is_winner:
                count += 1
            if count == size:
                return True
    # проверка по диагонали
    count = 0
    for i in range(size):
        if field[i][i] == who_is_winner:
            count += 1
        if count == size:
            return True
    # проверка по обратной диагонали
    count = 0
    for i in range(size):
        if field[i][size - 1 - i] == who_is_winner:
            count += 1
        if count == size:
            return True

#собственно, сама игра
def game():
    turn_number = 1
    while True:
        player = None
        if turn_number % 2 == 1:
            player = 'X'
        else:
            player = '0'
        print(f'---------------\nХод номер {turn_number}!\nХодит игрок {player}.\n---------------')
        show_field()
        row = input('Введите номер строки: ')
        column = input('Введите номер столбца: ')
        #предотвращаем три варианта некорректного ввода
        if not (row.isdigit()) or not(column.isdigit()):
            print('\nВведите числа!')
            continue
        row, column = int(row), int(column)
        if 0 > row or row > (size - 1) or 0 > column or column > (size - 1):
            print('\nВведите числа в игровом диапазоне!')
            continue
        if field[row][column] != '-':
            print('\nКлетка занята!')
            continue
        field[row][column] = player
        if win(player) is True:
            show_field()
            print(f'\nПобедил игрок {player}!')
            break
        if turn_number == size ** 2:
            show_field()
            print('\nНичья!')
            break
        turn_number += 1

game()





