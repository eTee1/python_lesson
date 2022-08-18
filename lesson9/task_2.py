import random

dict_1 = {x: random.randint(0, 99) for x in range(1, 21)}
print(dict_1)
var = 1
for key in dict_1:
    var = var * dict_1[key]
print(var)
