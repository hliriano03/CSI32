from tkinter import *
from random import *
from time import *
 
class CopsNRobbers(Tk):

    '''
    Game of cops and robbers
    '''
 
    def __init__(self):
        #initates Tk and sets up all settings
        Tk.__init__(self)
        self.title("Cops and Robbers")
        #list for all nodes in game
        self.nodes = []
        self.createline = [0,0]
        #dictionary for all lines connecting 2 nodes
        self.lines = {}
        self.player = 'Cop'
        self.copwins = 0
        self.coploses = 0
        self.robberwins = 0
        self.robberloses = 0
        self.playerPosition = {0:0, 1:0}
        self.remainingTurns = 25
        self.isGameStart = False
        self.startingEvent = 0
        self.isRetry = False
        self.GUI()

    def GUI(self):

        '''
        Creates GUI of game
        '''

    def create_nodes(self,howmanynodes):

        '''
        Creates nodes in game
        '''

        #stores nodes
        for node in range(howmanynodes):

            self.nodes.append(node + 1)
                
    def create_lines(self,node1, node2):

        '''
        Creates the lines of selected nodes
        '''
            
        node1 = self.createline[0]
        node2 = self.createline[1]

        #error check if line already exists
        if (node1,node2) in self.lines or (node2,node1) in self.lines:
            #pop up message comes up
            self.messageLabel.config(text = 'Cannot create same line again, select new node.', foreground = 'red')
            self.popMessage()
                                     

        else:
            #adds line to the dictionary and it gives it an ID
            self.lines[node1, node2] = max(self.nodes) + 1
    
    def position_player(self,node):

        '''
        Position players in selected nodes
        '''

            #check if both players are positioned to start game
            if self.playerPosition[0] != 0 and self.playerPosition[1] != 0:
                
                self.isGameStart = True
                print('Game Start')
                movePlayer(node)

            #positions cop to selected node
            if self.player == 'Cop':
                    
                self.playerPosition[0] = node
                self.player = 'Robber'

            #position robber to selected node
            elif self.player == 'Robber':

                if self.isGameStart == False and self.playerPosition[0] == node:
                    print('Cop already in that node, select another node.')
                    self.popMessage()
                    break

                self.playerPosition[1] = node
                self.player = 'Cop'

    def movePlayer(self,node):

        if self.player == 'Cop':

                # the game starts once both players are position, this checks if the game started to begin substracting the remaining turns
                if self.isGameStart == True:

                    if (node,self.playerPosition[0]) in self.lines or \
                       (self.playerPosition[0],node) in self.lines:
                        self.remainingTurns = self.remainingTurns - 1

                    #error check for clicking current node player is in
                    elif self.playerPosition[0] == node:
                        print('Cannot stay in same node.')
                        break

                    #error check for clicking any other node that is not adjacent to the current node player is positioned
                    else:
                        print('Cannot select nodes that are not adjacent.')
                        break
                    
                self.playerPosition[0] = node
                self.player = 'Robber'
                print('Turn: Robber')

            #position robber to selected node
            elif self.player == 'Robber':

                if self.isGameStart == True:
                    
                    if (node,self.playerPosition[1]) in self.lines or \
                       (self.playerPosition[1],node) in self.lines:
                        self.remainingTurns = self.remainingTurns - 1

                    elif self.playerPosition[1] == node:
                        print('Cannot stay in same node.')
                        break

                    #error check for clicking any other node that is not adjacent to the current node player is positioned
                    else:
                        print('Cannot select nodes that are not adjacent.')
                        break

                if self.playerPosition[1] != 0:
                    self.canvas.itemconfig(self.playerPosition[1], fill='white')
                
                self.playerPosition[1] = node
                self.player = 'Cop'
                print('Turn: Cop')

        print(self.remainingTurns)
        self.checkWinner()
        
    def checkWinner(self):

        '''
        Checks for winner
        '''

        
        #checks for winner
        if self.playerPosition[0] != 0 and self.playerPosition != 0:

            if self.playerPosition[0] == self.playerPosition[1]:

                print('Cop Wins')

            elif self.remainingTurns == 0:

                print('Robber Wins')

    def retryGame(self):

        '''
        Button command
        '''

            
    def recreateGame(self):

        '''
        Button command
        '''

    def popMessage(self):

        '''
        Pops up a message for specific events
        '''


App = CopsNRobbers()
App.mainloop()
