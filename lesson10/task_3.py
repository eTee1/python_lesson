paper = set(range(1, 76))
journal = set(range(77, 104))
total = (paper | journal)
pj = set(range(1, 14))
families = total - pj
print(len(families), 'families lives in a house')
