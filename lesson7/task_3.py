entire_list = [int(var) for var in input('Enter digits with separator space: ').split()]
entire_list2 = [int(var) for var in input('Enter digits with separator space: ').split()]
list3 = entire_list + entire_list2
result = []
d1 = set(list3)
for i in d1:
    if list3.count(i) == 1:
        result.append(i)
print(len(result))
