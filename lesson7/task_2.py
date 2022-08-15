entire_list = [int(var) for var in input('Enter digits with separator space: ').split()]
index, ind_value = [int(var) for var in input('Enter index and index value with separator space: ').split()]
entire_list.append(0)
for i in range(len(entire_list) - 1, index, -1):
    entire_list[i] = entire_list[i - 1]
entire_list[index] = ind_value
print(' '.join([str(i) for i in entire_list]))
