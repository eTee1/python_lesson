import random

N = int(input('Enter NxN positive value for matrix N= '))
matrix = [[random.randint(0, 99) for _ in range(N)] for _ in range(N)]
print('Random values for matrix below')
print(*matrix, sep='\n')

summary_d = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if i == j:
            summary_d += matrix[i][j]
print('Summary of numbers along the diagonal: ', summary_d)

print('Summary of last numbers in each row: ', sum(N[-1] for N in matrix))
