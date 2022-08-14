num = int(input('input number:'))
while num > 9:
    var1 = num // 10
    var2 = num % 10
    num //= 10
    while var1 != 0:
        if var2 == var1 % 10:
            print('YES')
            exit(0)
        var1 //= 10
print('NO')
