entire_list = [int(var) for var in input('Enter digits with separator space: ').split()]
index = int(input('Enter index: '))
for i in range(index + 1, len(entire_list)):
    entire_list[i - 1] = entire_list[i]
entire_list.pop()
print(' '.join([str(i) for i in entire_list]))
