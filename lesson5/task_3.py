a = int(input('Enter number (zero exit): '))
count = 1
summary = minimum = maximum = a
count2 = 0
count3 = 0
if a % 2 == 0:
    count2 += 1
else:
    count3 += 1

while True:
    a = int(input('Enter number (zero exit): '))
    if a == 0:
        break
    count += 1
    summary += a
    if a > maximum:
        maximum = a
    if a < minimum:
        minimum = a
    if a % 2 == 0:
        count2 += 1
    else:
        count3 += 1

print('Summary = ', summary)
print('Average =', summary / count)
print('Minimum =', minimum, 'Maximum=', maximum)
print('Even: ', count2, 'Odd: ', count3)
