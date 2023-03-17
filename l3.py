counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)

# line 4 is idiom for checking if item is in dict, then adding a new key with value 0 or adding 1 to that key's value
