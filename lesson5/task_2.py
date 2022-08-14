num = int(input('Write natural number N: '))
for i in range(1, num):
    d = 10
    while i >= d:
        d = d * 10
    if (i * i % d) == i:
        print(i, '*', i, '=', i * i)
