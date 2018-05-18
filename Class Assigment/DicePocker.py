# COMMENT: Nice looking program.
# Some comments to improve ...
# But even beyond that we also want to think in an "Object-Oriented Way"
# so breaking up the program into objects.
# Your program is using a legitimate, but non-objected oriented approach:
# breaking up tasks into functions.

from random import *

def main():
    money = 100
    dice = [1,1,1,1,1]
    quitGame = 1 # COMMENT: Better form is to use Boolean, so set True.
    userInterface(money, dice, quitGame)
    '''
    COMMENT: The name "userInterface" is deceptive, since really this
    is a run of the game. It is more than just the interface
    In fact my main criticism of the style of this program is that
    the functionality of the user interface is not separate from
    the functionality of the underlying game.
    The user-interface being a collection of functions (like intro,
    and asking what the user wants to re-roll, etc) could be
    written as a collection of related functions.  But in the object
    oriented way, the related functions get grouped into a single
    object; many (including me!) believe this give a better organization.
    And an alternative organization will more easilly scale up to larger
    progjects.
    '''

def roll(dice):

    print("*Initial Roll*")

    for die in range(len(dice)):

        dice[die] = randint(1,6)

    return dice

def reroll(dice):
    
    dieAmount = input("Which Die/Dice would you like to reroll Ex: 1,3: ")

    if dieAmount == "":

        dieAmount = []

    else:
        dieAmount = list(map(int, sorted(dieAmount.split(','))))

        for die in dieAmount:

            dice[die - 1] = randint(1,6)

    return dice

def checkGame(dice, money):

    dice = {x:dice.count(x) for x in dice}

    if len(dice.values()) == 1:

        print("\n**Five of the Kind +$50**\n")
        money = money + 50

        return money

    elif 2 <= len(dice.values()) <= 3:

        if 4 in dice.values():

            print("\n**Four of the Kind +$40**\n")
            money = money + 40
            
            return money

        elif 3 in dice.values():

            if 2 in dice.values():

                print("\n**Full House +$30**\n")
                money = money + 30
            
                return money

            else:
                print("\n**Three of the Kind +$20**\n")
                money = money + 20
            
                return money

        elif 2 in dice.values():

            if 1 in dice.values():

                print("\n**Two Pairs +$15**\n")
                money = money + 15
            
                return money        

    elif len(dice.values()) == 4:

        if 2 in dice.values():

            print("\n**One Pairs +$5**\n")
            money = money + 5
        
            return money

    elif len(dice.values()) == 5:

        if 1 in dice.values():

            print("\n**Bust +$0**\n")

            return money
        
def userInterface(money, dice, quitGame):

    while 0 <= money and quitGame == 1:

        print("*Paying Game Entry*\n-$10\n")

        print("Initial Money: $" + str(money))

        money = money - 10
        
        print("Current Money: $" + str(money) + "\n")
        roll(dice)
        print(dice)
        
        print("\n*First Reroll*\n")
        reroll(dice)
        print(dice)

        print("\n*Second Reroll*\n")
        reroll(dice)
        print(dice)
        money = checkGame(dice, money)

        quitGame = input("Want to continue? Yes or No: ")

        if quitGame == 'Yes':

            quitGame = 1

        elif quitGame == 'No':
            quitGame = 0

main()
