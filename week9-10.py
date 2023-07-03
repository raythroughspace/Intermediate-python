from tkinter import *
from tkinter import filedialog 

class SudokuCell(Label):
    """represents a Sudoku cell"""
    
    def __init__(self, master, coord):
        """SudokuCell(master, coord) -> SudokuCell
        creates a new blank SudokuCell with (row, column) coord"""
        Label.__init__(self, master, height = 1, width = 2, text = '', \
                       bg = "white", font = ("Arial", 24))
        self.coord = coord 
        self.number = 0
        self.readOnly = False
        self.highlighted = False
        
        self.bind("<Button-1>", self.highlight)
        self.bind("<Key>", self.change)
        
    def get_coord(self):
        """SudokuCell.get_coord() -> tuple
        returns the (row, column) coordinate of the cell"""
        return self.coord

    def get_number(self):
        """SudokuCell.get_number() -> int
        returns the number in the cell (0 if empty)"""
        return self.number
    
    def is_read_only(self):
        """SudokuCell.is_read_only() -> bool
        returns True if the cell is read-only, False if not"""
        return self.readOnly
    
    def is_highlighted(self):
        """SudokuCell.is_highlighted() -> bool
        return True if the cell is highlighted, False if not"""
        return self.highlighted
    
    def set_number(self, number, readOnly=False):
        """SudokuCell.set_number(number, [readOnly])
        sets the number in the cell and unhighlights 
        readOnly = True sets the cell to be read-only"""
        self.readOnly = readOnly
        self.number = number
        self.unhighlight()
        self.master.update_cells()
    
    def update_display(self, badCell = False):
        """SudokuCell.update_display() 
        displays the number in the cell 
        displays as:
            empty if its value is 0
            black if user-entered and legal
            gray if read-only and legal
            red when badCell is True"""
        if self.number == 0:
            self['text'] = ""
        else:
            self['text'] = str(self.number)
            if badCell:
                self['fg'] = "red"
            elif self.readOnly:
                self['fg'] = 'dim gray'
            else:
                self['fg'] = "black"
                
    def highlight(self, event):
        """SudokuCell.highlight(event)
        handler function for mouse click
        highlights the cell if it can be edited (non-read-only)"""
        if (not self.readOnly):
            self.master.unhighlight_all()
            self.focus_set()
            self.highlighted = True
            self['bg'] = 'lightgrey'
        
    def unhighlight(self):
        """SudokuCell.unhighlight()
        unhighlights the cell (changes background to white)"""
        self.highlighted = False
        self['bg'] = 'white'
        
    def change(self, event):
        """SudokuCell.change(event)
        handler function for key press
        only works on editable (non-read-only) and highlighted cells
        if a number key was pressed: sets cell to that number
        if a backspace/delete key was pressed: deletes the number"""
        if (not self.readOnly and self.highlighted):
            if "1" <= event.char <= "9":
                self.set_number(int(event.char))
            elif event.keysym in ["BackSpace", "Delete"]:
                self.set_number(0)
                
class SudokuUnit:
    """represents a Sudoku unit (row, column, or box)"""
    
    def __init__(self, cells):
        """SudokuUnit(cells) -> SudokuUnit
        creates a new SudokuUnit with the SudokuCells in dict cells"""
        self.cells = cells
    
    def get_coord_list(self):
        """SudokuUnit.get_coord_list() -> list
        returns list of (row, column) tuples for cells"""
        return list(self.cells.keys())
    
    def get_cell_list(self):
        """SudokuUnit.get_cell_list() -> list
        returns list of SudokuCells"""
        return list(self.cells.values())
    
    def contains_coord(self, coord):
        """SudokuUnit.contains_coord(coord) -> bool
        returns True if (row, column) tuple is in unit, otherwise False"""
        return coord in self.cells

class SudokuGrid(Frame):
    """object for a Sudoku grid"""
    
    def __init__(self,master):
        """SudokuGrid(master)
        creates a new blank Sudoku grid"""
        #initialize a new Frame
        Frame.__init__(self, master, bg = "black")
        self.grid()
        #put in lines between the cells
        # (odd numbered rows and columns in the grid)
        for n in range(1,17,2):
            self.rowconfigure(n, minsize=1)
            self.columnconfigure(n, minsize=1)
        # thicker lines between 3x3 boxes and at the bottom
        self.columnfigure(5, minsize=3)
        self.columnfigure(11, minsize=3)
        self.rowconfigure(5, minsize=3)
        self.rowconfigure(11, minsize=3)
        self.rowconfigure(17, minsize=1)
        
        self.buttonFrame = Frame(self, bg = 'white')
        Button(self.buttonFrame, text = "Load Grid", command = self.load_grid).grid(row=0, column = 0)
        Button(self.buttonFrame, text = "Save Grid", command = self.save_grid).grid(row =0, column=1)
        Button(self.buttonFrame, text = "Solve", command = self.solve).grid(row=0, column=2)
        Button(self.buttonFrame, text = "Reset", command = self.reset).grid(row=0, column=3)
        self.buttonFrame.grid(row=18, column=0, columnspan=17)
        
        self.cells = {}
        for row in range(9):
            for column in range(9):
                coord = (row, column)
                self.cells[coord] = SudokuCell(self, coord)
                #cells go in even-numbered rows/columns of the grid
                self.cells[coord].grid(row = 2*row, column=2*column)
        #set up units
        self.units = []
        #do rows and columns at the same time
        for m in range(9):
            rowCells = {}
            columnCells = {}
            for n in range(9):
                rowCells[(m,n)] = self.cells[(m,n)]
                columnCells[(n,m)] = self.cells[(n,m)]
            self.units.append(SudokuUnit(rowCells))
            self.units.append(SudokuUnit(columnCells))
        
        for row in [0,3,6]:
            for column in [0,3,6]:
                boxCells = {}
                for i in range(3):
                    for j in range(3):
                        boxCells[(row+i, column+j)] = self.cells[(row+i, column+j)]
                    self.units.append(SudokuUnit(boxCells))
                    
    def unhighlight_all(self):
        """SudokuGrid.unhighlight_all()
        unhighlight all the cells in the grid"""
        for cell in self.cells:
            cell.unhighlight()
        
    def update_cells(self):
        """SudokuGrid.update_cells()
        check for good/bad cells and update their color"""
        for coord in self.cells:
            cell = self.cells[coord]
            number = cell.get_number()
            foundBad = False
            if (number ==0):
                cell.update_display(False)
                continue
            for unit in self.find_units(coord):
                for otherCoord in unit.get_coord_list():
                    if otherCoord == coord:
                        continue
                    if self.cells[otherCoord].get_number() == number:
                        foundBad = True
            cell.update_display(foundBad)
            
    def find_units(self,coord):
        """SudokuGrid.find_units(coord) -> list
        returns a list SudokuUnit's containing (row, column) tuple coord"""
        return [unit for unit in self.units if unit.contains_coord(coord)]
        
    def load_grid(self):
        """SudokuGrid.load_grid() 
        loads a Sudoku grid from a file"""
        filename = filedialog.askopenfilename(defaultextension = '.txt')
        if filename:
            sodokufile = open(filename, "r")
            rowList = sudokufile.readlines()
            sudokufile.close()
            for row in range(9):
                for column in range(9):
                    value = int(rowList[row][column])
                    self.cells[(row,column)].set_number(value, value!= 0)
        
    def save_grid(self):
        """SudokuGrid.save_grid()
        saves the Sudoku grid to a file"""
        filename = filedialog.asksaveasfilename(defaultextension = '.txt')
        if filename:
            sudokufile = open(filename, "w")
            for row in range(9):
                for column in range(9):
                    sudokufile.write(str(self.cells[(row,column)].get_cell()))
                sudokufile.write("\n")
            sudokufile.close()
        
    def reset(self):
        """SudokuGrid.reset() 
        clears all non-read-only cells"""
        for cell in self.cells:
            if not self.cells[cell].is_read_only():
                self.cells[cell].set_number(0)
        
    def solve(self):
        """SudokuGrid.solve()
        solves the Sudoku grid (if possible)
        pops up dialog box at the end indicating the solved status"""
        pass