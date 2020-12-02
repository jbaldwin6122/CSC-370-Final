import random

from random import randrange
import time
import collections
from collections import Counter
import copy

"""
Cell object that represents each square in a Sudoku puzzle

"""

class Cell:

    def __init__(self, id):
        self.id = id
        self.cur_val = 0
        self.values = []
        self.neighbors = []

    def add_value(self, number):
        self.values.append(number)

    def get_values(self):
        return self.values

    def set_current(self, number):
        self.cur_val = number

    
        
"""
Board object that represents a Sudoku puzzle. It includes cells and various functions.
"""

class Board:

    """
    Represents a Board in the form of an array list with 9 arrays
    """


    def __init__(self):

        rows = []

        row_1 = [Cell("A11"), Cell("A12" ) , Cell("A13") , Cell("B14"), Cell("B15"), Cell("B16"), Cell("C17"), Cell("C18"), Cell("C19")]
        rows.append(row_1)
        
        row_2 = [Cell("A21"), Cell("A22" ) , Cell("A23") , Cell("B24"), Cell("B25"), Cell("B26"), Cell("C27"), Cell("C28"), Cell("C29")]
        rows.append(row_2)

        row_3 = [Cell("A31"), Cell("A32" ) , Cell("A33") , Cell("B34"), Cell("B35"), Cell("B36"), Cell("C37"), Cell("C38"), Cell("C39")]
        rows.append(row_3)
        
        row_4 = [Cell("D41"), Cell("D42" ) , Cell("D43") , Cell("E44"), Cell("E45"), Cell("E46"), Cell("F47"), Cell("F48"), Cell("F49")]
        rows.append(row_4)

        row_5 = [Cell("D51"), Cell("D52" ) , Cell("D53") , Cell("E54"), Cell("E55"), Cell("E56"), Cell("F57"), Cell("F58"), Cell("F59")]
        rows.append(row_5)
        
        row_6 = [Cell("D61"), Cell("D62" ) , Cell("D63") , Cell("E64"), Cell("E65"), Cell("E66"), Cell("F67"), Cell("F68"), Cell("F69")]
        rows.append(row_6)

        row_7 = [Cell("G71"), Cell("G72" ) , Cell("G73") , Cell("H74"), Cell("H75"), Cell("H76"), Cell("I77"), Cell("I78"), Cell("I79")]
        rows.append(row_7)
        
        row_8 = [Cell("G81"), Cell("G82" ) , Cell("G83") , Cell("H84"), Cell("H85"), Cell("H86"), Cell("I87"), Cell("I88"), Cell("I89")]
        rows.append(row_8)

        row_9 = [Cell("G91"), Cell("G92" ) , Cell("G93") , Cell("H94"), Cell("H95"), Cell("H96"), Cell("I97"), Cell("I98"), Cell("I99")]
        rows.append(row_9)
       
        

        self.board = [[y for y in row] for row in rows]

    def __len__(self):
        return 9

    def __getitem__(self, tup):
        y, x = tup
        return self.board[y][x]

    def fill_initial_board(self, str_board):
        
        count = 0
        for c in str_board:
            list1 = []
            row = count / 9
            col = count % 9
            if(c != "."):
                self[row,col].set_current(int(c))
            count = count + 1
        
        return self

    def board_pretty_print(self):

        for row in len(self.board):
            for col in len(self.board[0]):
                print(self.board[row][col].get_values)

    def find_neighbors(self , box , row , col):
        #modify this to find all neighbors for all cells or do it in the main 

        neighbors = []
        
        
        for i in range(len(self)):
            for j in range(len(self)):

                if (self.board[i][j].id[0] == box and (self.board[i][j].id[1] != row or self.board[i][j].id[2] != col)):
                    neighbors.append(self.board[i][j])
                elif(self.board[i][j].id[0] != box and self.board[i][j].id[1] == row):
                    neighbors.append(self.board[i][j])
                elif(self.board[i][j].id[0] != box and self.board[i][j].id[2] == col):
                    neighbors.append(self.board[i][j])
        
        r = int(row) - 1
        c = int(col) - 1

  
        self[r,c].neighbors = neighbors

        return neighbors

    def initial_values(self, neighbors, cell):

        all_poss = [1,2,3,4,5,6,7,8,9]
        neigh_values = []

        #loop through neighbors and append their values to list
        for i in neighbors: # i is a cell
            val = int(i.cur_val)
            if (val in all_poss):
                all_poss.remove(val) #gives all neighbor values
            
        #compare 2 lists and set values = to what missing from neighbors

        cell.values = all_poss

      

        return cell.values


    #loop through cells, find cells with no curr_val and less possible
    def find_less_poss(self): 

        min_len = 10
        min_cell = self[0,0]
        for i in range(len(self)):
            for j in range(len(self)):
                if (self[i,j].cur_val == 0 and len(self[i,j].values) < min_len):
                    min_len = len(self[i,j].values)
                    min_cell = self[i,j]

        return min_cell


    def board_is_solved(self):
        
        for i in range(len(self)):
            for j in range(len(self)):
                if (self[i,j].cur_val == 0 ):
                    return False
        
        return True


    def simple_AC3_min_val(self):

        while(not self.board_is_solved()):
            #find less values
            min_cell = self.find_less_poss()
            
            values = min_cell.values
            print(min_cell.id)
            print(min_cell.values)
            #find number to assign
            if (len(values) != 0):
                
                number = randrange(len(values))
                num_val = values[number]
                min_cell.set_current(num_val)
                for cell in min_cell.neighbors:
                    self.initial_values(cell.neighbors, cell)
            else:
                return self

            #loop through neighbors and remove that value
            #for n_cell in min_cell.neighbors:
             #   if(num_val in n_cell.values):
              #      n_cell.values.remove(num_val)

    #Create an "is consistent" function

    def find_unass(self):
       
        for i in range(9):
            for j in range(9):
                if (self[i,j].cur_val != 0):
                   return self[i,j]
        return false

    def backtrack_with_min_val(self, pcell):
        #Check if it solved
        if (self.board_is_solved()):
            #print(self[8,8].cur_val)
            
            return True

        #find the cell with least possible values
        min_cell = self.find_less_poss()

        #min_cell = self.find_unass()
        self.initial_values(min_cell.neighbors, min_cell)

        for cell in pcell.neighbors:
            self.initial_values(cell.neighbors, cell)
        
        if (len(min_cell.values) > 1):
            min_cell = least_constr_val(min_cell)

        #Loop through values
        for i in min_cell.values:
            if(is_allowed(min_cell, i)):
                min_cell.set_current(int(i))

                #remove that value as possible for the neighbors
               # for n_cell in min_cell.neighbors:
               #     if(i in n_cell.values):
               #         n_cell.values.remove(i)
                #contraint_propagation(min_cell, i , 0)
            
                #Recursive call
                
                
                sol = self.backtrack_with_min_val(min_cell)

                
                if (sol):
                    return sol
               

                #contraint_propagation(min_cell, i , 1)
               # for n_cell in min_cell.neighbors:
                #    n_cell.values.append(i)
                #min_cell.values.remove(i)
        min_cell.set_current(0)
            
        
        return False

"""
    End of the Board class, beggining of independent methods
"""

def contraint_propagation(cell, value, flag):

    if (flag == 0):
        for n_cell in cell.neighbors:
                if(value in n_cell.values):
                    n_cell.values.remove(value)
        
    else:
        for n_cell in cell.neighbors:
            n_cell.values.append(value)
            

def least_constr_val(cell):

    lista = []

    for i in cell.values:
        lista.append(i)
        for neigh in cell.neighbors:
            if (i in neigh.values):
                lista.append(i)
            

    counts = collections.Counter(lista)
    
    lista = sorted(lista, key=lambda x: counts[x])
   

    cell.values = set(lista)

    return cell

def is_allowed(cell , value):

    for i in cell.neighbors:
        if (i.cur_val == value):
            return False
            
    return True

def solve_back(board):
    return board.backtrack_with_min_val(board[0,0])

def non_empty_squares(board):

    non_empty_cells = []

    for i in range(9):
        for j in range(9):
            if (board[i,j].cur_val != 0):
                non_empty_cells.append(board[i,j])
    
    return non_empty_cells

def sudoku_generator(board):
    
    non_empty_cells = non_empty_squares(board)
    num_non_empty = len(non_empty_cells)

    rounds = 5

    while (round > 0 and  num_non_empty > 17):

        cur_cell = random.choice(non_empty_cells)

        non_empty_cells.remove(cur_cell)

        num_non_empty -= 1
        value_to_delete = cur_cell.cur_val

        cur_cell.cur_val = "."

        if not solve_back(board):
            rounds -= 1
            cur_cell.cur_val = value_to_delete
            num_non_empty += 1

    return board
    

def read_sudoku(board):

    grid = ""

    for i in range(9):
        for j in range(9):
            grid = grid + str(board[i,j].cur_val)

    return grid



def main():


    start_board = Board()

    #Initialize all neighbors
    for i in range(len(start_board)):
        for j in range(len(start_board)):
             cell = start_board[i,j]
             neigh = start_board.find_neighbors(cell.id[0] , cell.id[1], cell.id[2])
             filled_board = start_board.fill_initial_board("1....7.9..3..2...8..96..5....53..9...1..8...26....4...3......1..4......7..7...3..")
             final = filled_board.initial_values(neigh, cell)
             #Easy Puzzles
             #5..3.6.92.69...15....51.8.....69..2.67...8..99....2.8.....8.5.3..32.7..4.14.3....
             #...4..67........84....12.5..51.29...94..63....7....5....289...6....4..1........4.
             #.2.638..98........3.52.16..47......2...4...3...6.7....5..9.431.71.....4...4......
             #.....9571.7...3..4...8.2..698.32....2..6.8...4.......8...1...3..94.....58.17.....
             #1........8..2.4.........14.58....7..4...5921..2.....68.....23....7936...94.....5.
             #.8.......9.....6.4..6..817.3...71..8..5.2.46....3..5.7..29.....5.....9...19..7...
             #........7.1....893.......244.781...5.23.4...1......3.....9.5.3.7....4...9.4.2..1.

             #Medium Puzzles
             #.....4.....12....9.....5.6..59....81...8.32...7.........4.92.....8.4....36......2
             #.2....9.......678.34...9..29....8.7....3...41.38.......1.8....6...7...5......1...
             

             #Hard Puzzles
             #.....6....59.....82....8....45........3........6..3.54...325..6..................

             #Very Difficult Sudoku
             #.......39....1...5..3..58....8..9..6.7..2....1..4.......9..8.5..2....6..4..7.....   ----> 3 seconds
             #1.......2.9.4...5...6...7...5.9.3.......7.......85..4.7.....6...3...9.8...2.....1   ----> 5 seconds
             #4...3.......6..8..........1....5..9..8....6...7.2........1.27..5.3....4.9........   ----> 2 seconds

             #Evil Puzzles
             #.2.....7....5...4....1..........35...9..7..........1.81.5...6..4...2.......8.....   ----> 18-20 seconds
             #8..........36......7..9.2...5...7.......457.....1...3...1....68..85...1..9....4..   ----> 8
             #.....5.8....6.1.43..........1.5........1.6...3.......553.....61........4.........   ----> Norvig 1439 seconds, for us 0.06
             #..3......8.946.7.22...186.......6.7...8...4...7.8.......294....54.6.328.7......2..


            # print(final)

    counter = 0


    count = 0
    for i in range(len(filled_board)):
        if (count % 3 == 0):
            print("===============================")
        count = count + 1
        count_col = 0
        for j in range(len(filled_board)):
            
            if (count_col % 3 == 0):
                print(" | "),
            print(filled_board[i,j].cur_val),
           
            count_col = count_col + 1
            
        print("")
    print("===============================")



    #start = time.time()
    #filled_board.simple_AC3_min_val()
    #end = time.time()

    #print("Naive AC-3 End Time is" , end - start)

    start_back = time.time()
    #filled_board.simple_AC3_min_val()
    solve_back(filled_board)
    end_back = time.time()
    print("Backtracking End Time is" , end_back - start_back)

    print("INITIAL BOARD")

    count = 0
    for i in range(len(filled_board)):
        if (count % 3 == 0):
            print("===============================")
        count = count + 1
        count_col = 0
        for j in range(len(filled_board)):
            
            if (count_col % 3 == 0):
                print(" | "),
            print(filled_board[i,j].cur_val),
           
            count_col = count_col + 1
            
        print("")
    print("===============================")

    """

    sudoku_list = []
    for i in range(100):
        filled_copy = copy.deepcopy(filled_board) 
        new_board = sudoku_generator(filled_copy)
        grid = read_sudoku(new_board)
        sudoku_list.append(grid)

   

    print(len(sudoku_list))
    sudoku_list = set(sudoku_list)
    print(len(sudoku_list))

    with open('Sudokus.txt', 'w') as f:
        for item in sudoku_list:
            f.write("%s\n" % item)
    
    print(grid)
    
    
    new_start = Board()


    for i in range(len(new_start)):
        for j in range(len(new_start)):
             cell = new_start[i,j]
             neigh = new_start.find_neighbors(cell.id[0] , cell.id[1], cell.id[2])
             filled_board = new_start.fill_initial_board(grid)
             final = filled_board.initial_values(neigh, cell)

   # print("Backtracking End Time is" , end_back - start_back)

    solve_back(filled_board)

    print("LAST ONE PRINTED")

    count = 0
    for i in range(len(filled_board)):
        if (count % 3 == 0):
            print("===============================")
        count = count + 1
        count_col = 0
        for j in range(len(filled_board)):
            
            if (count_col % 3 == 0):
                print(" | "),
            print(filled_board[i,j].cur_val),
           
            count_col = count_col + 1
            
        print("")
    print("===============================")
    
    new_board = sudoku_generator(filled_board)
    print("Backtracking End Time is" , end_back - start_back)

    """
    return

main()