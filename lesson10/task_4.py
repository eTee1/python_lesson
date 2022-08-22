total = 52
pins = set(range(1, 24))
marks = set(range(25, 60))
pm = set(range(1, 17))
pins_ok = len((pins | marks) - pm)
pins_not_ok = total - pins_ok
print(pins_not_ok, 'pupils not like collecting')
