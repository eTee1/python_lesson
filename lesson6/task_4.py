string = str(input('Enter a string: '))
print('a. Third Symbol is: ', string[2])
print('b. Penultimate Symbol is: ', string[-2])
print('c. First Five Symbols is: ', string[:5])
print('d. All Symbols expect two last is: ', string[:-2])
print('e. All Symbols with Even index is: ', string[::2])
print('f. All Symbols with Odd index is: ', string[1::2])
print('g. All Symbols in reverse order is: ', string[::-1])
print('h. All Symbols 1 by 1 in reverse order from the last: ', string[::-2])
print('i. String length is: ', len(string))
