print('Hello! Welcome to Charglemart!')
print('For a list of commands, please type "help"')

#default values
menustate = 'main'
buymess = False #Decides whether to display the buy help message
bucks = 100
inven = 'Legendary Orc Blade'

#main menu input function
def mainmen(mainin):
    if mainin == 'help':
        print('Input "buy" for a list of items for purchase; "sell" to attempt to sell items;')
        print('"look" to just kinda look around; or "chat" to strike up a conversation with Chargle.')
        print('You can also type "back" to go back or "main" to return to the main menu.')
    elif mainin == 'buy':
        print('Oh, you gon buy sum shit?')
        global menustate #I have a feeling this isn't the proper way to do this...
        menustate = 'buy'
        global buymess
        buymess = False
    else:
        print('REEEEEE')

#buy menu input function
def buymen1(buyin1):
    if buyin1 == 'food':
        print('Input item number to buy.')
        print('Available items:'
              '1 - Bordo meat sandwich [$6]'
              '2 - Fried scrub beast haunch [$8]'
              '3 - Bowl of Chargle-Os [$4]')
    elif buyin1 == 'drinks':
        print('Input item number to buy.')
        print('Available items:'
              '1 - Blue drink [$2]'
              '2 - Red juice [$3]'
              '3 - Potion of minor mining [$4]')
    elif buyin1 == 'oddities':
        print('Input item number to buy.')
        print('Available items:'
              '1 - Charglemart hat [$10]'
              '2 - Dozen ninja stars [$12]'
              '3 - Orb of Orc [$25]')
    elif buyin1 == 'help':
        print('Type "food", "drinks", or "oddities".')
        print('You can also type "back" to go back or "main" to return to main menu.')
    elif buyin1 == 'back':
        global buymess
        buymess = False
        global menustate
        menustate = 'main'
    elif buyin1 == 'main':
        buymess = False
        menustate = 'main'

#buy menu main prompt
while menustate == 'buy':
    if buymess == False:
        print('There are many things to buy at Charglemart! Type "food", "drinks", or "oddities".')
        buymess = True
        buyin1 = input('> ')
        buymen1(buyin1)
    else:
        buyin1 = input('> ')
        buymen1(buyin1)

#main menu prompt
while menustate == 'main':
    mainin = input('> ')
    mainmen(mainin)