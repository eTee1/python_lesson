matrix = int(input('Enter positive value size of matrix NxN N= '))
for row in range(1, matrix + 1):
    for col in range(1, matrix + 1):
        if row % 2 == 0:
            print('%4d' % row, end=' ')  # использовал 4 для длинны учитывая "-", тк матрицу N=999 строит минуту
        else:
            print('%4d' % (col - 1 - matrix), end=' ')
    print()
