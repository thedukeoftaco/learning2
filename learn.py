def memes(coun):
    dreams = 'Here are your memes, sir.'
    if coun == 0:
        print(dreams)
        coun = coun + 1
    elif coun == 1:
        print(dreams + ' ...and an extra meme for you ;)')
        coun = coun + 1
    elif coun >= 2:
        print(dreams + ' ...and ' + str(coun) + ' extra memes for you ;)')
    print(coun)

def screams():
    print('REEEEEEEEEEE')
    print(coun)

coun = 2
mans = input('Would you like a meme, sir? Y/N ')
if mans == 'Y':
    memes(coun)
elif mans == 'N':
    screams()
else:
    print('lolwut')
    print(coun)