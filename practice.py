fhand = open('datatest.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('Meme'):
        continue
    words = line.split()
    print(words[2])
