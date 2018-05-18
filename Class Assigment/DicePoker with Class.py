from random import *
 
class DicePoker:
 
    def __init__(self):
 
        self.money = 100 # may change
        self.UI = UserInterface()
        self.dice = SetOfDice()
        self.getResult = GameResult()
        self.GameContinue = True
 
    # First try at run method.
    def run(self):
 
        # introduce and set up game.
        self.UI.Intro()
        self.money = self.UI.getMoney()
        self.initialMoney = self.money
 
         
        while self.isGameOver() == False:
 
            # plays player round
            self.playRound()
            # check for game result
            self.money = self.getResult.CheckGameResult(self.dice.getValue(), self.money)
 
            #check Game Status
            self.GameContinue = self.UI.getGameStatus()
 
 
        #check if GameOver
        else:
            self.UI.Score(self.initialMoney, self.money)
 
    def playRound(self):
        #Charges Entry Fee
        self.money = self.UI.ChargeGameFee(self.money)
        #Initial Roll
        self.dice.roll()
        #Outputs the Initial Roll
        self.UI.outputRollResults( self.dice.getValue() )
 
        # We have 2 re-rolls
        for r in range(2):
            #Rerolls selected die/dice
            self.dice.reRoll( self.UI.getReRoll() )
            #UI outputs the result
            self.UI.outputRollResults( self.dice.getValue() )
                     
 
    # Returns True or False
    def isGameOver(self):
         
 
        if self.GameContinue == False or self.money < 10:
 
            return True
 
        else:
            return False
         
        # return True only if self.GameContinue it True
        # and amount of money is at least 10
 
class UserInterface:
 
    def __init__(self):
        pass
 
    def Intro(self):
        print("Welcome to Dice Pocker \n" )
 
 
    #sets self.money to the amount inputed
    def getMoney(self):
 
        M = eval(input("How much money do you want to start with? - "))
        return M
 
    #charges game fee        
    def ChargeGameFee(self,money):
 
        fee = 10
        money = money - fee
 
        print("\nCharging Game Fee: $10 \nCurrent Money: $" + str(money) + "\n")
         
        return money
 
    def outputRollResults(self, result):

        print(result, "\n") # start cheap!
 
    def getReRoll(self):
 
        return input("Which Die/Dice would you like to reroll Ex: 1,3: ")
 
    def getGameStatus(self):
 
        ans = input("\nDo you want to play again? - ")

        if ans == "":

            return True
 
        else:
            if ans[0] in ['y','Y']:
                return True

            else:
                return False
 
    #outputs the scores when game ends
    def Score(self,initialMoney, money):
 
        if money > initialMoney:
 
            print("\nCongratulations you Won $" + str(money - initialMoney))
            print("Current Money: $" + str(money) + "\n")
            print("Thanks for Playing!")
 
        elif money < initialMoney:
 
            print("\nSorry! you Lost $" + str(money - initialMoney))
            print("Current Money: $" + str(money) + "\n")
            print("Thanks for Playing!")
 
 
        else:
            print("\nWon and Lost the Same Amount")
            print("Current Money: $" + str(money) + "\n")
            print("Thanks for Playing!")
 
 
class SetOfDice:
 
    def __init__(self):
        self.dice = [0,0,0,0,0]
     
    def roll(self):
 
        for die in range(len(self.dice)):
 
            self.dice[die] = randint(1,6)
 
        return self.dice
 
    def reRoll(self,diceToReRoll):
 
        if diceToReRoll == "":
 
            pass
 
        else:
            diceToReRoll = list(map(int, sorted(diceToReRoll.split(','))))
 
            for die in diceToReRoll:
 
                self.dice[die - 1] = randint(1,6)
 
        return self.dice
 
    def getValue(self):
 
        return self.dice
             
class GameResult():
 
    def __init__(self):
        pass
 
    def CheckGameResult(self, dice, money):
 
        dice = {x:dice.count(x) for x in dice}
 
        if len(dice.values()) == 1:
 
            print("**Five of the Kind +$50**\n")
            money = money + 50
            print("Current Money: $" + str(money))
 
            return money
 
        elif 2 <= len(dice.values()) <= 3:
 
            if 4 in dice.values():
 
                print("**Four of the Kind +$40**\n")
                money = money + 40
                print("Current Money: $" + str(money))
 
                 
                return money
 
            elif 3 in dice.values():
 
                if 2 in dice.values():
 
                    print("**Full House +$30**\n")
                    money = money + 30
                    print("Current Money: $" + str(money))
                     
                    return money
 
                else:
                    print("**Three of the Kind +$20**\n")
                    money = money + 20
                    print("Current Money: $" + str(money))
                 
                    return money
 
            elif 2 in dice.values():
 
                if 1 in dice.values():
 
                    print("**Two Pairs +$15**\n")
                    money = money + 15
                    print("Current Money: $" + str(money))
                 
                    return money        
 
        elif len(dice.values()) == 4:
 
            if 2 in dice.values():
 
                print("**One Pairs +$5**\n")
                money = money + 5
                print("Current Money: $" + str(money))
             
                return money
 
        elif len(dice.values()) == 5:

            if 1 not in dice.keys() or 6 not in dice.keys():
                print("**Straight +$25**\n")
                print("Current Money: $" + str(money))
                 
                return money 
 
            else:
 
                print("**Bust +$0**\n")
                print("Current Money: $" + str(money))
                 
                return money


        
