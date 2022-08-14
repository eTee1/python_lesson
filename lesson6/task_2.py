string = str(input('Enter a string: '))
character = str(input('Enter character for search in a string: '))
if len(character) == 1:
    pass
else:
    character = str(input('Enter only ONE character for search in a string: '))
count = 0
for i in string:
    if i == character:
        count += 1
print(count, 'characters found in a string.')
