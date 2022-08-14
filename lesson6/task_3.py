rows = int(input('Enter number from 3 to 9: '))
if 9 >= rows >= 3:
    pass
else:
    rows = int(input('Wrong number, Enter number from 3 to 9: '))
for count in range(1, rows + 2):
    for count2 in range(1, count - 1):
        print(count2, end="")
    for count2 in range(count - 1, 0, -1):
        print(count2, end="")
    print()
