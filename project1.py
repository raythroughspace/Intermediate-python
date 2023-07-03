from tkinter import *
from tkinter import messagebox
import random 

class MinesweeperCell(Label):
    """represents a minesweeper cell"""
    colorList = ["gray", "blue", "green", "red", "purple","pink", "cyan", "black", "gray"]
    
    def __init__(self, master, coord, isBomb = False):
        """MinesweeperCell(master, coord, isBomb)-> MinesweeperCell
        initializes a minesweeper cell with (row, column) coord"""
        
        Label.__init__(self, master, height=1, width=2,text='', \
                       bg='white', fg = 'black', font=('Arial', 16), relief = RAISED)
        
        self.isRevealed = False
        self.coord = coord
        self.isBomb = isBomb
        self.isMarked = False
        self.number = 0 #0 means blank
        self.adj = [] #adjacent cells
        
        self.bind('<Button-1>', self.reveal)
        self.bind('<Button-2>', self.toggle_mark)
        
    def set_adj(self, cells):
        """MinesweeperCell(cells) -> None
        sets adjacent cells that will auto-expose once this cell is revealed"""
        self.adj = cells
        
    def set_number(self, num):
        """MinesweeperCell.set_number(num) -> None
        set number of this cell"""
        self.number = num
        
    def reveal(self, event, mainCell = True):
        """MinesweeperCell.reveal() -> None
        reveal this cell to user and auto-expose adj cells
        mainCell is used to track the main call to reveal, only main cell 
        checks whether the game was won"""
        if (self.isBomb and not self.isMarked):
            self.master.end_game(win = False)
            return
        if (not self.isRevealed and not self.isMarked):
            self.isRevealed = True
            self['bg'] = "gray"
            self['relief'] = SUNKEN
            self['fg'] = MinesweeperCell.colorList[self.number]
            self['text'] = str(self.number)
            if (self.number == 0):
                for cell in self.adj: #recursively reveal adj cells
                    cell.reveal(event, False)
        if (mainCell):
            self.master.check_win() 
        
    def is_bomb(self):
        """MinesweeperCell.is_bomb() -> bool
        returns True if this cell contains a bomb, False otherwise"""
        return self.isBomb
        
    def toggle_mark(self, event):
        """MinesweeperCell.toggle_mark() -> None
        toggles bomb marking on this cell"""
        if (not self.isRevealed):
            if (not self.isMarked and self.master.marksLeft >0):
                self['text'] = "*"
                self.master.marksLeft -=1
                self.isMarked = True
            elif (self.isMarked):
                self['text'] = ""
                self.master.marksLeft +=1
                self.isMarked = False
        self.master.update_display()
        
    def highlight_red(self):
        """MinesweeperCell.highlight_red() -> None
        highlights this cell red if this cell is a bomb"""
        if (self.isBomb):
            self['bg'] = "red"
            self['text'] = "*"
            
    def is_revealed(self):
        """MinesweeperCell.is_revealed() -> bool
        returns True if this cell has been revealed, False otherwise"""
        return self.isRevealed
        
        
class MinesweeperGrid(Frame):
    """represents a minesweeper grid"""
    
    def __init__(self, master, width, height, numBombs):
        """MinesweeperGrid(master, width, height, numBombs) -> MinesweeperGrid
        initializes a minesweeper grid with dimensions widthxheight and
        numBombs bombs"""
        Frame.__init__(self, master, bg = 'white')
        self.grid()
        
        self.numBombs = numBombs
        self.marksLeft = numBombs
        self.width = width
        self.height = height
        
        #self.columnconfigure(column, minsize = )
        #Button args: master, text=, command=, 
        #grid() args: row =, column=, columnspan=
        #Label args: master, height = , width=, text=, bg= ,font = 
        
        #put in lines between cells
        for i in range(width-1):
            self.rowconfigure(2*i+1, minsize=1)
        for i in range(height-1):
            self.columnconfigure(2*i+1, minsize=1)
        #make cells, pick bombs
        self.cells = []
        bombCoords = self.pick_bombs()
        for x in range(width):
            columnCells = []
            for y in range(height):
                isBomb = (x,y) in bombCoords
                cell = MinesweeperCell(self, (x,y), isBomb)
                columnCells.append(cell)
                cell.grid(column = x, row = y)
            self.cells.append(columnCells)
        #set numbers and adj cells
        for x in range(width):
            for y in range(height):
                adj = []
                for i in [-1,0,1]:
                    for j in [-1,0,1]:
                        if (i==0 and j==0):
                            continue
                        if (self.check_bounds(x+i, y+j)):
                            adj.append(self.cells[x+i][y+j])
                self.cells[x][y].set_adj(adj)
                adjBombs = 0
                for cell in adj:
                    if (cell.is_bomb()):
                        adjBombs +=1
                self.cells[x][y].set_number(adjBombs)
        #Add marking counter
        self.markingLabel = Label(self, height = 1, width=2, text = str(self.marksLeft), bg = "white", font = ("Arial", 20))
        self.markingLabel.grid(row = 2*height, columnspan = 2*(width-1))
        
    def check_bounds(self, x,y):
        """MinesweeperGrid.check_bounds(x,y) -> bool
        returns True if x,y is a valid index into self.cells, False otherwise"""
        return x>=0 and x<self.width and y>=0 and y<self.height
    
    def pick_bombs(self):
        """MinesweeperGrid.pick_bombs() -> list
        returns a random list of coordinates containing
        self.numBombs picked  bombs"""
        bombCoords = []
        left = self.numBombs
        while (left >0):
            x = random.randrange(self.width)
            y = random.randrange(self.height)
            if (x,y) not in bombCoords:
                left -=1
                bombCoords.append((x,y))
        return bombCoords
        
    def end_game(self, win = True):
        """MinesweeperGrid.end_game(win) -> None
        end this game and display results"""
        if (win):
            messagebox.showinfo("Minesweeper", "Congratulations -- you won!", parent = self)
        else:
            messagebox.showerror("Minesweeper", "KABOOM! You lose.", parent = self)
            for x in range(self.width):
                for y in range(self.height):
                    self.cells[x][y].highlight_red()
                
    def check_win(self):
        """MinesweeperGrid.check_win() -> None
        checks whether the game has been won after revealing cells
        triggers end_game if won"""
        for x in range(self.width):
            for y in range(self.height):
                if (not self.cells[x][y].is_bomb() and not self.cells[x][y].is_revealed()):
                    return      
        self.end_game()
        
    def update_display(self):
        """MinesweeperGrid.update_display() -> None
        updates the number of marks left to use"""
        self.markingLabel['text'] = str(self.marksLeft)
                    

def play_minesweeper(width, height, numBombs):
    """play_minesweeper(width, height, numBombs) -> None
    starts a minesweeper game with dimension width x height and 
    numBombs bombs"""
    root = Tk()
    root.title("Minesweeper")
    game = MinesweeperGrid(root, width, height, numBombs)
    root.mainloop()
        
play_minesweeper(10,10,50)   
    
"""TESTS
Bombs:
    correct number of bombs in the game
    clicking on bomb leads to loss and highlights red
Non-bombs:
    blank cells auto-expose
    cells labelled with correct numbers
Flags:
    number of flags left shown
    flagged cells can't reveal
    can toggle between flagged and unflagged
Other:
    checked different dimensions and numbombs (up to 30x30)
"""  
        