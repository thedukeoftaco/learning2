counts = {'memes': 1, 'dreams': 23, 'screams': 300}
for key in counts:
    print(key, counts[key])

# 2 different ways to print dict
print(list(counts))
print(counts.keys())

# get values only (no predictable order) using "dictvar".values()
print(counts.values())

# get items using "dictvar".items()
print(counts.items())
