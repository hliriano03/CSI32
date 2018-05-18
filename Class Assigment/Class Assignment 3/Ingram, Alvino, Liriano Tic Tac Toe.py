# For Tkinter practice, create a tic-tac-toe board where pieces can
# be placed or moved.

from tkinter import *


class BoardSquare:


    def __init__(self, root):

        self.size = 150
        self.sq = Canvas(root, width = self.size, height = self.size)
        self.sq.create_rectangle(2, 2, self.size-1, self.size-1)
        self.val = ''


    def clear(self):

        self.sq.delete("all")

    def bind(self, F):

        self.sq.bind("<Button-1>", F)

    def grid(self, r, c):

        self.sq.grid(row = r, column = c)

    def drawX(self):

        self.sq.create_line(2, 2, self.size-1, self.size-1)
        self.sq.create_line(2,self.size-1, self.size-1, 2)
        self.val = 'X'

    def drawO(self):

        self.sq.create_oval(2,2,self.size-1,self.size-1)
        self.val = 'O'

    def getVal(self):

        return self.val



        


class TicTacToe:

    def __init__(self, root):

        #Button(root, text = "Board").grid(row = 0,column = 0, columnspan = 6)

        self.gameOver = False
        self.turn = 'X'
        self.board = {}
        self.status = 0

        
        for i in range(3):
            for j in range(3):
                #Label(r, text = str(i) + str(j)).grid(row = i, column = j)

                b = BoardSquare(root)
                b.grid(i, j)
                b.bind(lambda event, arg = b: self._clicked(arg))
                self.board[(i,j)] = b

        #Creates Labels
        self.winner = Label(root, text =("Player {} won!".format(self.status)))
        self.TurnLabel = Label(root, text = ("Player {} Turn".format(self.turn)))
        self.TurnLabel.grid(row=3, column=0)
    def _clicked(self, b):
        if b.getVal() == '' and not(self.gameOver):
            if self.turn == 'X':
                b.drawX()
                self._toggleTurn()
            else:
                b.drawO()
                self._toggleTurn()

        self.status = self.checkGameStatus()

        self.TurnLabel.config(text = ("Player {} Turn".format(self.turn)))
        if self.status != '':
            #Update Labels
            self.winner.config(text = "Player {} won!".format(self.status))
            self.winner.grid(row=3, column=2)
            self.gameOver = True


    def _toggleTurn(self):

        if self.turn == 'X':
            self.turn = 'O'
        else:
            self.turn = 'X'
        

    def checkGameStatus(self):

        # check rows
        for i in range(3):
            xCount = 0
            oCount = 0
            for j in range(3):
                if self.board[(i,j)].getVal() == 'X':
                    xCount = xCount + 1
                elif self.board[(i,j)].getVal() == 'O':
                    oCount = oCount + 1
            if xCount == 3:
                return 'X'
            elif oCount == 3:
                return 'O'

            

        # check columns
        for j in range(3):
            xCount = 0
            oCount = 0
            for i in range(3):
                if self.board[(i,j)].getVal() == 'X':
                    xCount = xCount + 1
                elif self.board[(i,j)].getVal() == 'O':
                    oCount = oCount + 1
            if xCount == 3:
                return 'X'
            elif oCount == 3:
                return 'O'




        # check diagonals
       # Third, check if one of 2 diagonals is a win
    
        # Diagonal the starts in top left
        xCount = 0
        oCount = 0
        for k in range(3):
            if self.board[(k,k)].getVal() == 'X':
                xCount = xCount + 1
            if self.board[(k,k)].getVal() == 'O':
                oCount = oCount + 1

        if xCount == 3:
            return 'X'
        elif oCount == 3:
            return 'O'

        # Diagonal that starts at bottom left
        xCount = 0
        oCount = 0
        for k in range(3):
            if self.board[(2-k,k)].getVal() == 'X':
                xCount = xCount + 1
            if self.board[(2-k,k)].getVal() == 'O':
                oCount = oCount + 1

        if xCount == 3:
            return 'X'
        elif oCount == 3:
            return 'O'

        

        return '' # for no winner

root = Tk()


game = TicTacToe(root)


root.mainloop()
root.destroy()















