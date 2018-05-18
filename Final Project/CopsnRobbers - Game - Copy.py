# COMMENTS:
# Impressive looking operation.
# Missing logical core and design of main program.
# So for logical core + program, grade total: 80
# On coding, important issue:
# - Want to break up program in an object-oriented way,
#   but this program has only one class.
# - Break up long involved coding steps into more smaller steps
#   (with more methods, and more classes)

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

        
        frame = LabelFrame(self, text="Command")
        frame.pack(side=TOP, padx=10, pady=10, fill=X)
        status = LabelFrame(self, text="Status")
        status.pack(side=TOP, padx = 10)
        copstatus = LabelFrame(status, text="Cop")
        copstatus.pack(side=LEFT, padx = 5, pady = 10)
                    
    def create_lines(self,event):

        '''
        Creates the lines of selected nodes
        '''
        
        #hides pop up message
        self.canvas.itemconfig(self.canvas_frame, state = HIDDEN)

        #checks which node has been clicked and colors it green to indicate it
        for node in self.nodes:

            if event.x > self.canvas.coords(node)[0] and \
               event.x < self.canvas.coords(node)[2] and \
               event.y > self.canvas.coords(node)[1] and \
               event.y < self.canvas.coords(node)[3]:

                if self.createline[0] == 0:
                    self.createline[0] = node
                    self.canvas.itemconfig(node, fill='green')
                    

                elif self.createline[1] == 0 and self.createline[0] != node:
                    self.createline[1] = node
                    self.canvas.itemconfig(node, fill='green')

                else:
                    #pop up message comes up
                    self.messageLabel.config(text = 'Cannot select same node, select another one.', foreground = 'red')
                    self.popMessage()

            #checks if selected nodes are already selected or not        
            if self.createline[0] != 0 and self.createline[1] != 0:
                
                node1 = self.createline[0]
                node2 = self.createline[1]

                #error check if line already exists
                if (node1,node2) in self.lines or (node2,node1) in self.lines:
                    #pop up message comes up
                    self.messageLabel.config(text = 'Cannot create same line again, select new node.', foreground = 'red')
                    self.popMessage()
                                             

                else:
                    #adds line to the dictionary
                    self.lines[node1, node2] = self.canvas.create_line((self.canvas.coords(node1)[2] + \
                                        self.canvas.coords(node1)[0])/2,
                                        (self.canvas.coords(node1)[3] + \
                                        self.canvas.coords(node1)[1])/2,
                                        (self.canvas.coords(node2)[2] + \
                                        self.canvas.coords(node2)[0])/2,
                                        (self.canvas.coords(node2)[3] + \
                                        self.canvas.coords(node2)[1])/2 ,width = 4)

                self.canvas.itemconfig(node1, fill='white')
                self.canvas.itemconfig(node2, fill='white')
                self.createline = [0,0]

        #Position Player button becomes available for next step
        if len(self.lines.values()) >= len(self.nodes) - 1:
            self.button_PositionPlayers.config(state = NORMAL)

        #lifts up all nodes so the lines are under the nodes
        for node in self.nodes:
            self.canvas.lift(node)
    
    def position_player(self,event):

        '''
        Position players in selected nodes
        '''

        self.canvas.itemconfig(self.canvas_frame, state = HIDDEN)

        #checks for node selected to position player
        for node in self.nodes:

            #positions cop to selected node
            if event.x > self.canvas.coords(node)[0] and \
               event.x < self.canvas.coords(node)[2] and \
               event.y > self.canvas.coords(node)[1] and \
               event.y < self.canvas.coords(node)[3] and self.player == 'Cop':

                # the game starts once both players are position, this checks if the game started to begin substracting the remaining turns
                if self.isGameStart == True:

                    if (node,self.playerPosition[0]) in self.lines or \
                       (self.playerPosition[0],node) in self.lines:
                        self.remainingTurns = self.remainingTurns - 1

                    #error check for clicking current node player is in
                    elif self.playerPosition[1] == node:
                        self.messageLabel.config(text = 'Cannot stay in same node.', foreground = 'red')
                        self.popMessage()
                        break

                    #error check for clicking any other node that is not adjacent to the current node player is positioned
                    else:
                        self.messageLabel.config(text = 'Cannot select nodes that are not adjacent.', foreground = 'red')
                        self.popMessage()
                        break

                    
                #changes node to white when leaving the node    
                if self.playerPosition[0] != 0:                
                    self.canvas.itemconfig(self.playerPosition[0], fill='white')
                    
                self.playerPosition[0] = node
                self.canvas.lift(node)
                self.canvas.itemconfig(node, fill='blue')
                self.player = 'Robber'
                self.playerTurnLabel.config(text='Turn: Robber')

            #position robber to selected node
            elif event.x > self.canvas.coords(node)[0] and \
               event.x < self.canvas.coords(node)[2] and \
               event.y > self.canvas.coords(node)[1] and \
               event.y < self.canvas.coords(node)[3] and self.player == 'Robber':

                self.button_giveUp.config(state=NORMAL)

                if self.isGameStart == True:
                    
                    if (node,self.playerPosition[1]) in self.lines or \
                       (self.playerPosition[1],node) in self.lines:
                        self.remainingTurns = self.remainingTurns - 1

                    elif self.playerPosition[1] == node:
                        self.messageLabel.config(text = 'Cannot stay in same node.', foreground = 'red')
                        self.popMessage()
                        break

                    else:
                        self.messageLabel.config(text = 'Cannot select nodes that are not adjacent.', foreground = 'red')
                        self.popMessage()
                        break

                elif self.isGameStart == False and self.playerPosition[0] == node:
                    self.messageLabel.config(text = 'Cop already in that node, select another node.', foreground = 'red')
                    self.popMessage()
                    break

                if self.playerPosition[1] != 0:
                    self.canvas.itemconfig(self.playerPosition[1], fill='white')
                
                self.playerPosition[1] = node
                self.canvas.lift(node)
                self.canvas.itemconfig(node, fill='red')
                self.player = 'Cop'
                self.playerTurnLabel.config(text='Turn: Cop')

        #check if both players are positioned to start game
        if self.playerPosition[0] != 0 and self.playerPosition[1] != 0:
            
            self.isGameStart = True

            #pop up message indicated the game started
            if self.startingEvent == 0:

                self.canvas.itemconfig(self.canvas_frame, state = NORMAL)
                self.messageLabel.config(text = 'Game Start!')

                for n in range(5):

                    if n % 2 == 0:
                        self.messageLabel.config(foreground = 'blue')

                    else:
                        self.messageLabel.config(foreground = 'red')

                    self.update()
                    sleep(0.15)

                self.startingEvent = 1

            self.canvas.itemconfig(self.canvas_frame, state = HIDDEN)

        self.remainingTurnsLabel.config(text=str(self.remainingTurns))
        self.checkWinner()

    def createlineButtonOnClick(self):

        '''
        Button command
        '''

        #takes players to next phase of creating the map
        self.button_connectNodes.config(state = DISABLED)
        self.canvas.unbind("<Button-1>")
        self.canvas.bind("<Button-1>", self.create_lines)
        

    def positionButtonOnClick(self):

        '''
        Button command
        '''

        #takes players to positioning
        self.button_connectNodes.config(state = DISABLED)
        self.button_PositionPlayers.config(state = DISABLED)
        self.canvas.unbind("<Button-1>")
        self.canvas.bind("<Button-1>", self.position_player)

    def giveUp(self):

        '''
        Button command
        '''

        self.button_retryGame.config(state = NORMAL)

        #gives up and opponent wins
        if self.player == 'Cop':
            self.coploses = self.coploses + 1
            self.coplosesLabel.config(text = 'Loses = ' + str(self.coploses))
            self.robberwins = self.robberwins + 1
            self.robberwinsLabel.config(text = 'Wins = ' + str(self.robberwins))
            self.canvas.unbind("<Button-1>")
            self.messageLabel.config(text = 'Cop Gives Up!', foreground = 'blue')
            self.popMessage()
            
        elif self.player == 'Robber':
            self.robberloses = self.robberloses + 1
            self.robberlosesLabel.config(text = 'Loses = ' + str(self.robberloses))
            self.copwins = self.copwins + 1
            self.copwinsLabel.config(text = 'Wins = ' + str(self.copwins))
            self.canvas.unbind("<Button-1>")
            self.messageLabel.config(text = 'Robber Gives Up!', foreground = 'red')
            self.popMessage()
        
    def checkWinner(self):

        '''
        Checks for winner
        '''

        
        #checks for winner
        if self.playerPosition[0] != 0 and self.playerPosition != 0:

            if self.playerPosition[0] == self.playerPosition[1]:

                self.copwins = self.copwins + 1
                self.copwinsLabel.config(text = 'Wins = ' + str(self.copwins))
                self.robberloses = self.robberloses + 1
                self.robberlosesLabel.config(text = 'Loses = ' + str(self.robberloses))
                self.canvas.unbind("<Button-1>")
                self.button_giveUp.config(state=DISABLED)
                self.button_retryGame.config(state=NORMAL)
                self.messageLabel.config(text = 'Cop Wins', foreground = 'blue')
                self.popMessage()
                self.isRetry = False

                while self.isRetry == False:
                    self.canvas.itemconfig(self.playerPosition[0], fill='blue')
                    self.update()
                    sleep(0.2)
                    self.canvas.itemconfig(self.playerPosition[0], fill='red')
                    self.update()
                    sleep(0.2)

            elif self.remainingTurns == 0:

                self.robberwins = self.robberwins + 1
                self.robberwinsLabel.config(text = 'Wins = ' + str(self.robberwins))
                self.coploses = self.copwins + 1
                self.coplosesLabel.config(text = 'Loses = ' + str(self.coploses))
                self.canvas.unbind("<Button-1>")
                self.button_giveUp.config(state=DISABLED)
                self.button_retryGame.config(state=NORMAL)
                self.messageLabel.config(text = 'Robber Wins', foreground = 'red')
                self.popMessage()

    def retryGame(self):

        '''
        Button command
        '''

        #restarts game using the same map
        self.canvas.itemconfig(self.canvas_frame, state = HIDDEN)
        self.canvas.itemconfig(self.playerPosition[0], fill='white')
        self.canvas.itemconfig(self.playerPosition[1], fill='white')
        self.playerPosition = {0:0, 1:0}
        self.player = 'Cop'
        self.playerTurnLabel.config(text='Turn: Cop')
        self.remainingTurns = 25
        self.remainingTurnsLabel.config(text=str(self.remainingTurns))
        self.isGameStart = False
        self.isRetry = True
        self.button_retryGame.config(state=DISABLED)
        self.startingEvent = 0
        self.canvas.bind("<Button-1>", self.position_player)
            
    def recreateGame(self):

        '''
        Button command
        '''

        #lets players recreate a new map
        self.canvas.itemconfig(self.canvas_frame, state = HIDDEN)
        
        for nodes in self.nodes:

            self.canvas.delete(nodes)

        for lines in self.lines:

            self.canvas.delete(self.lines[lines])

        self.nodes = []
        self.lines = {}
        self.playerPosition = {0:0, 1:0}
        self.player = 'Cop'
        self.playerTurnLabel.config(text='Turn: Cop')
        self.remainingTurns = 25
        self.remainingTurnsLabel.config(text=str(self.remainingTurns))
        self.isGameStart = False
        self.isRetry = True
        self.button_connectNodes.config(state = DISABLED)
        self.button_PositionPlayers.config(state = DISABLED)
        self.button_retryGame.config(state = DISABLED)
        self.button_giveUp.config(state=DISABLED)
        self.startingEvent = 0
        self.canvas.unbind("<Button-1>")
        self.canvas.bind("<Button-1>", self.create_nodes)

    def popMessage(self):

        '''
        Pops up a message for specific events
        '''

        #pops up messages for speciific events
        for n in range(5):

            if n % 2 == 0:
                self.canvas.itemconfig(self.canvas_frame, state = NORMAL)

            else:
                self.canvas.itemconfig(self.canvas_frame, state = HIDDEN)

            self.update()
            sleep(0.1)

App = CopsNRobbers()
App.mainloop()
