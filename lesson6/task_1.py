words = str(input('Enter two words:'))
split_words = words.split()
var1 = split_words[0]
var2 = split_words[1]
if var1.isalpha() and var2.isalpha():
    pass
else:
    words = str(input('Please enter only two words:'))
print(var1[::-1].title() + ' ' + var2[::-1].title())
