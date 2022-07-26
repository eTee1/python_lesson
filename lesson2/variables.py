var1_int = 123
var2_int = 456
print(var1_int, var2_int)

var3_int = var1_int
var1_int = var2_int
var2_int = var3_int
print(var1_int, var2_int)

var1_int, var2_int = var2_int, var1_int
print(var1_int, var2_int)
