# 10 / 10
# COMMENT: Nice object oriented design!

from random import *

class SwitchOrStay:

    def __init__(self):

        self.UI = UserInterface()
        self.Cards = SetOfCards()
        self.Statistics = Statistics()
        self.isGameContinue = True
        
    def run(self):

        self.UI.Intro()

        while self.isGameOver() == False:

            self.PlayRound()

            self.isGameContinue = self.UI.getGameContinue()


        else:
            self.UI.getGameResult()

    def PlayRound(self):

        self.Cards._setCards()
        self.Cards.setChosenCard(self.UI.getChooseCard())
        self.Cards.RemoveCard()

        result = self.UI.getRoundResult(self.Cards.SwitchOrStay(self.UI.getSwitchOrStay()))
        self.Statistics.Update(result)

    def isGameOver(self):

        if self.isGameContinue == False:
  
            return True
  
        else:
            return False

class UserInterface:

    def __init__(self):
        pass

    def Intro(self):
        print("Welcome to Switch or Stay Game \n" )

    def getChooseCard(self):

        print("Pick one of the the Three cards\n         [1] [2] [3]\n")
        return eval(input("Card: "))

    def getSwitchOrStay(self):

        ans = eval(input("\nOne card removed. Would you like to [1] Switch or [2] Stay? - "))
            
        return ans
    
    def getRoundResult(self, result):
        
        if result[1] == 1:

            print("\nYou won")              

        else:
            print("\nYou lost")

        return result

    def getGameResult(self):

        print(game.Statistics)
        
    def getGameContinue(self):
        
        ans = input("\nDo you want to play again? - ")
 
        if ans == "":
 
            return True
  
        else:
            if ans[0] in ['y','Y']:
                return True
 
            else:
                return False

class SetOfCards:

    def __init__(self):

        self.cards = []
        self.ChosenCard = 0

    def _setCards(self):

        while len(self.cards) < 3:

            if 1 not in self.cards:

                if len(self.cards) < 2:

                    self.cards.append(randint(0,1))

                else:
                    self.cards.append(1)

            else:
                self.cards.append(0)

        return self.cards

    def RemoveCard(self):

        return self.cards.remove(0)

    def setChosenCard(self, ChosenCard):

        self.ChosenCard = self.cards[ChosenCard - 1]

        return self.ChosenCard

    def getChosenCard(self):

        return self.ChosenCard

    def getCards(self):

        return self.cards

    def SwitchOrStay(self, ans):

        if ans == 1:

            if self.ChosenCard == 1:

                self.ChosenCard = 0

                return ans,self.ChosenCard               

            else:
                self.ChosenCard = 1

            return ans,self.ChosenCard

        elif ans == 2:
            
            return ans,self.ChosenCard 

class Statistics:

    def __init__(self):
        self.winsbyswitch = 0
        self.losesbyswitch = 0
        self.winsbystay = 0
        self.losesbystay = 0

    def Update(self, result):

        ans = result[0]
        ChosenCard = result[1]
        
        if ans == 1 and ChosenCard == 1:

            self.winsbyswitch = self.winsbyswitch + 1

            return True

        elif ans == 1 and ChosenCard == 0:

            self.losesbyswitch = self.losesbyswitch + 1

            return False

        elif ans == 2 and ChosenCard == 1:

            self.winsbystay = self.winsbystay + 1

            return True

        elif ans == 2 and ChosenCard == 0:

            self.losesbystay = self.losesbystay + 1

            return False
            

    def __str__(self):

        print("\nGame Ended\nHere are the Game Statistics:")

        return "\n[Switch]\n" + \
               "Wins: " + str(self.winsbyswitch) + \
               " Loses: " + str(self.losesbyswitch) + \
               "\nTotal: " + str(self.winsbyswitch + self.losesbyswitch) + \
               "\n\n[Stay]\n" + \
               "Wins: " + str(self.winsbystay) + \
               " Loses: " + str(self.losesbystay) + \
               "\nTotal: " + str(self.winsbystay + self.losesbystay)


game = SwitchOrStay()
game.run()
    
