class SwitchOrStay:

    def __init__(self):
        '''
        Sets all classes into variables to use within class
        '''

    def run(self):
        '''
        runs game until player decides not to play any more
        '''

    def PlayRound(self):
        '''
        Calls all function needed to play the round
        '''

    def isGameOver(self):
        '''
        Checks if isGameContinue is false, if it is then game continues
        otherwise game ends
        '''

class UserInterface:
    '''
    Displays game process
    '''

    def __init__(self):
        '''
        Stores wins by switch and stay, and loses by switch and stay
        '''

    def Intro(self):
        '''
        prints a welcoming message to start the game
        '''

    def getChosenCard(self):
        '''
        Asks player to choose a card from the set
        '''

    def getSwitchOrStay(self):
        '''
        Asks player if they want to switch or stay
        '''

00    def getRoundResult(self, result):
        '''
        Takes in a result variable which determines whether the player witns
        or looses, printing the result
        '''

    def getGameResult(self):
        '''
        Displays the amount of wins and loses by switching and the wins and
        loses by staying
        '''

    def getGameContinue(self):
        '''
        Asks if player wants to continue playing
        '''

class SetOfCards:
    '''
    Stores a set of 3 cards in which theres always a 1 and a two 0, the one
    represents winning cards, the 0 represents losing cards, 
    '''

    def __init__(self):
        '''
        Initializes the set of cards to no cards, and ChosenCard to 0
        '''



    def _setCards(self):
        '''
        sets a list containing always one 1 and two 0
        '''
        

    def RemoveCard(self):
        '''
        Removes one loosing card from the set
        '''


    def setChosenCard(self, ChosenCard):
        '''
        Takes a the chosen card and sets the chosen card 
        '''

    def getCards(self):
        '''
        Returns the current set of cards
        '''

    def SwitchOrStay(self, ans):
        '''
        Checks whether the player chose to switch or stay
        '''

class Statistics:

    def __init__(self):
        '''
        Sets up statistics variable, wins and loses by stays or switch
        '''

    def Update(self, ans, ChosenCard):
        '''
        Update statistics information
        '''

    def __str__(self):
        '''
        prints out current statistics
        '''
