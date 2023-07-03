from tkinter import *
from tkinter import messagebox

class CheckerSquare(Canvas):
    """Represents a single checker square"""
    
    def __init__(self, master, coord, color):
        """CheckerSquare(master, coord, color) -> CheckerSquare
        initializes a checker square with coord = (r,c) position
        and background color color"""
        Canvas.__init__(self, master, height = 50, width = 50,  bg = color, highlightbackground= color)
        self.grid(row = coord[0], column = coord[1])
        self.coord = coord
        self.bind("<Button-1>", master.get_click)
    
    def get_position(self):
        """CheckerSquare.get_position() -> tuple
        returns the position of this square"""
        return self.coord
            
    def make_color(self, color = None, isKing = False):
        """CheckerSquare.make_color(color, isKing) -> None
        displays a checker piece of color, if color == None
        then no piece displayed, if piece is a king,
        piece is labelled with an asterisk"""
        ovals = self.find_all()
        for oval in ovals:
            self.delete(oval)
        if (color is not None):
            oval = self.create_oval(10, 10, 44, 44, fill = color)
            if (isKing):
                self.create_text(27,27, text = "*", font = ("Arial", 18))
            else:
                self.create_text(27,27, text = "", font = ("Arial", 18))
    
class CheckerBoard:
    """Represents a checker board"""
    
    def __init__(self):
        """CheckerBoard() -> CheckerBoard
        initializes a checker board"""
        self.player = 0 #player 0, red goes first
        self.highlightCoord = None #highlighted coord
        self.jumpInProgress = False 
        self.board = {} 
        for row in range(8):
            for column in range(8):
                self.board[(row, column)] = (None,None)
                if (row<3 and (row + column)%2 == 1):
                    #player 0 and isKing = False
                    self.board[(row, column)] = (0, False) 
                elif (row > 4 and (row + column)%2 == 1):
                    self.board[(row,column)] = (1, False)
        
        self.winner = None #whether game has ended
        
    def next_player(self):
        """CheckerBoard.next_player() -> None
        move to next player's turn"""
        self.player = 1- self.player
    
    def get_board(self):
        """CheckerBoard.get_board() -> dict
        returns this board"""
        return self.board
    
    def get_highlight(self):
        """CheckerBoard.get_highlight() -> tuple
        returns the coordinate of highlighted square"""
        return self.highlightCoord
    
    def get_player(self):
        """CheckerBoard.get_player() -> int
        returns current player"""
        return self.player
    
    def get_jumpInProgress(self):
        """CheckerBoard.get_jumpInProgress() -> bool
        returns the jumpInProgress status"""
        return self.jumpInProgress
    
    def get_winner(self):
        """CheckerBoard.get_winner() -> int or None
        returns the winner of the game, None if no winners"""
        return self.winner
    
    def valid_moves(self):
        """CheckerBoard.valid_moves() -> dict
        returns a dictionary of valid moves current player can make
        keys are highlighted coords
        values are a list of valid moves highlighted coord can perform"""
        #loop through squares with player, check for jumps
        #if no jumps then loop again, valid moves going up/down in diag unless jumpInProgress
        valid = {}
        directions = [[(1,1), (1,-1)], [(-1, -1), (-1, 1)]] #player directions
        otherPlayer = 1- self.player
        for highlighted in self.board: #loop through highlighted coords
            if (self.jumpInProgress and highlighted != self.highlightCoord):
                #only the highlighted coord can keep jumping
                continue
            if (self.board[highlighted][0] == self.player): #square must be current player's
                playerdrs = directions[self.player][:]
                if (self.board[highlighted][1]):
                    #isKing is True, can go backwards
                    playerdrs += directions[otherPlayer][:]
                for dr in playerdrs:
                    oneStep = (dr[0] + highlighted[0], dr[1] + highlighted[1])
                    twoStep = (2*dr[0] + highlighted[0], 2*dr[1] + highlighted[1])
                    if (oneStep in self.board and twoStep in self.board \
                        and self.board[oneStep][0] == otherPlayer and self.board[twoStep][0] == None):
                        valid[highlighted] = valid.get(highlighted, []) + [twoStep] #this coord can jump to twoStep
        
        if (len(valid) == 0 and not self.jumpInProgress):
            for highlighted in self.board:
                if (self.board[highlighted][0] == self.player):
                    playerdrs = directions[self.player][:]
                    if (self.board[highlighted][1]):
                        #isKing is True, can go backwards
                        playerdrs += directions[otherPlayer][:]
                    for dr in playerdrs:
                        oneStep = (dr[0] + highlighted[0], dr[1] + highlighted[1])
                        if (oneStep in self.board and self.board[oneStep][0] == None):
                            valid[highlighted] = valid.get(highlighted, []) + [oneStep]
        return valid
    
    def move(self, coord):
        """CheckerBoard.move(coord) -> None
        move piece from self.highlightedCoord to coord, capturing if necessary"""
        if (self.is_jump(coord)):
            dr = ((coord[0] - self.highlightCoord[0])//2, (coord[1] - self.highlightCoord[1])//2)
            self.board[(self.highlightCoord[0] + dr[0], self.highlightCoord[1] + dr[1])] = (None, None)
        self.board[coord] = self.board[self.highlightCoord]
        self.board[self.highlightCoord] = (None, None)
    
    def print_info(self):
        """CheckerBoard.print_info()
        for testing and debugging"""
        valid = self.valid_moves()
        print(f"{self.highlightCoord} with moves: ")
        print(valid.get(self.highlightCoord, []))
        print(self.board[self.highlightCoord])
        
        
    def try_move(self, coord):
        """CheckerBoard.try_move(coord) -> bool
        try to move current highlighted square to coord"""
        valid = self.valid_moves()
        if (self.highlightCoord in valid and coord in valid[self.highlightCoord]):
            #it's a valid move, move piece
            self.move(coord)
            if (self.is_jump(coord)):
                self.jumpInProgress = True
                self.highlightCoord = coord
                if (len(self.valid_moves()) == 0):
                    #can't keep jumping, end turn
                    self.jumpInProgress = False
                    self.next_player()
                    
            else:
                #not a jump, end turn
                self.next_player()
            promotionRow = 7 - 7*(1-self.player)
            if (coord[0] == promotionRow):
                self.board[coord] = (self.board[coord][0], True)
                
        if (not self.jumpInProgress):
            #new highlighted coord is coord except if user must keep jumping
            self.highlightCoord = coord
            
        #for debugging and testing
        self.print_info()
        
        
    def is_jump(self, coord):
        """CheckerBoard.is_jump(coord) -> bool
        identify whether a valid move to coord is a jump"""
        if ((self.highlightCoord[0] - coord[0], self.highlightCoord[1] - coord[1]) \
            not in [(1,1), (-1,-1), (1,-1), (-1, 1)]):
            return True
        return False            
    
    def check_win(self):
        """CheckerBoard.check_win() -> None
        check whether the game was won a player"""
        currPlayer = self.player
        otherPlayer = 1- self.player
        #check if currPlayer lost
        outOfPieces = True
        for coord in self.board:
            if (self.board[coord][0] == currPlayer):
                outOfPieces = False
        if (outOfPieces):
            self.winner = otherPlayer #otherPlayer won
        #check if otherPlayer lost
        outOfPieces = True
        for coord in self.board:
            if (self.board[coord][0] == otherPlayer):
                outOfPieces = False
        if (outOfPieces):
            self.winner= currPlayer
                
class CheckerGame(Frame):
    """Represents a checker game"""
    
    def __init__(self, master):
        """CheckerGame(master) -> CheckerGame
        initializes a game of checkers"""
        Frame.__init__(self, master)
        self.grid()
        self.checkerBoard = CheckerBoard()
        self.colors = ["red", "white"] #player colors
        #Checker squares
        self.squares = {}
        for row in range(8):
            for col in range(8):
                coord = (row, col)
                if ((row + col) % 2 == 1): #green square
                    self.squares[coord] = CheckerSquare(self, coord, "green")
                    if (row <3):
                        self.squares[coord].make_color("red")
                    elif (row > 4):
                        self.squares[coord].make_color("white")
                else:
                    self.squares[coord] = CheckerSquare(self, coord, "beige")
                    self.squares[coord].unbind("<Button-1>")
                    
        #Label turn at the bottom
        self.rowconfigure(8, minsize= 3)
        Label(self, text = "Turn:", font = ("Arial", 18)).grid(row = 8, column = 1)
        self.turnOval = CheckerSquare(self, (8, 2), color = "gray")
        self.turnOval.make_color("red")
        self.turnOval.unbind("<Button-1>")
        self.jumpLabel = Label(self, text = "", font = ("Arial", 18))
        self.jumpLabel.grid(row=8, column=4, columnspan = 4)
    
    def get_click(self, event):
        """CheckerGame(event) -> None
        processes a click on the board"""
        coord = event.widget.get_position()
        self.checkerBoard.try_move(coord)
        self.checkerBoard.check_win()
        self.update_display()
        
    def update_display(self):
        """CheckerGame.update_display() -> None
        updates the display of the game"""
        if (self.checkerBoard.get_winner() != None):
            self.end_game()
        board = self.checkerBoard.get_board()
        highlightCoord = self.checkerBoard.get_highlight()
        for coord in board:
            if (board[coord][0] != None):
                self.squares[coord].make_color(self.colors[board[coord][0]], board[coord][1])
            else:
                self.squares[coord].make_color() #empty square
            if (coord == highlightCoord):
                self.squares[coord]['highlightbackground'] = "black"
            else:
                if (self.squares[coord]['bg'] == "green"): 
                    self.squares[coord]['highlightbackground'] = "green"
        self.turnOval.make_color(self.colors[self.checkerBoard.get_player()])
        
        if (self.checkerBoard.get_jumpInProgress()):
            self.jumpLabel['text'] = "Must continue to jump!"
        else:
            self.jumpLabel['text'] = ""   
            
    def end_game(self):
        """CheckerGame.end_game() -> None
        end game and announce winner"""
        winner= self.checkerBoard.get_winner()
        messagebox.showinfo("Checkers", f"Congratulations {self.colors[winner]}-- you won!", parent = self)
        for coord in self.squares:
            self.squares[coord].unbind("<Button-1>")
            
root = Tk()
root.title("Checkers")
game = CheckerGame(root)
game.mainloop()
    
"""TESTING
1. if a jump is possible, player must jump (also tested with king)
2. if a jump is possible, player must jump and keep jumping if possible (also tested with king)
3. king can go backwards, other pieces can only go forward
4. if a player runs out of pieces, the other player wins 
5. if a player jumps to a king promotion, it will stop jumping
6. turns correctly alternate
7. if multiple jumps possible, can pick which one to jump
"""
        
    
        
    