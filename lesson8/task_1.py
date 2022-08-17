matrix = int(input('Enter positive value size of matrix NxN N= '))
for row in range(1, matrix + 1):
    for col in range(1, matrix + 1):
        if row % 2 == 0:
            print('%4d' % row, end='\t') #матрицы N > 999+ долго строит, ограничил включая минус
        else:
            print('%4d' % (col - 1 - matrix), end='\t')
    print()
