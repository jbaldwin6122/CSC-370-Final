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
=============================================================================
"""

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
    
    """
        Check if board is solved
    """
    
    def board_is_solved(self):
        
        for i in range(len(self)):
            for j in range(len(self)):
                if (self[i,j].cur_val == 0 ):
                    return False
        
        return True
    
    """
        Solving just utilizing the constraints, no backtracking
    """
    
    def simple_AC3_min_val(self):

        while(not self.board_is_solved()):
            #find less values
            min_cell = self.find_less_poss()
            
            self.initial_values(min_cell.neighbors, min_cell)
            
            values = min_cell.values
            #find number to assign
            if (len(values) != 0):
                
                number = randrange(len(values))
                num_val = values[number]
                min_cell.set_current(num_val)
                for cell in min_cell.neighbors:
                    self.initial_values(cell.neighbors, cell)
                    
                if self.board_is_solved():
                    return 1
            else:
                return 0

            #loop through neighbors and remove that value
            #for n_cell in min_cell.neighbors:
             #   if(num_val in n_cell.values):
              #      n_cell.values.remove(num_val)

    #Create an "is consistent" function

    """
        Find unassigned cells and 
    """
    
    def find_unass(self):
       
        for i in range(9):
            for j in range(9):
                if (self[i,j].cur_val != 0):
                   return self[i,j]
        return false
    
    """
        Backtracking to solve a given sudoku puzzle
    """

    def backtrack_with_min_val(self, pcell):
        #Check if it solved
        if (self.board_is_solved()):
            #print(self[8,8].cur_val)
            
            return True

        #find the cell with least possible values
        min_cell = self.find_less_poss()

        #min_cell = self.find_unass()
        self.initial_values(min_cell.neighbors, min_cell)

        #for cell in pcell.neighbors:
        #    self.initial_values(cell.neighbors, cell)
        
        #if (len(min_cell.values) > 1):
        #    min_cell = least_constr_val(min_cell)

        #Loop through values
        for i in min_cell.values:
            #if(is_allowed(min_cell, i)):
                min_cell.set_current(int(i))
                
                
                sol = self.backtrack_with_min_val(min_cell)

                
                if (sol):
                    return sol
                
        min_cell.set_current(0)
        return False
    
    """
        MRV heuristic - finds the cell with the least available remaining values 

    """

    def find_less_poss(self): 

        min_len = 10
        min_cell = self[0,0]
        for i in range(len(self)):
            for j in range(len(self)):
                if (self[i,j].cur_val == 0 and len(self[i,j].values) < min_len):
                    min_len = len(self[i,j].values)
                    min_cell = self[i,j]

        return min_cell
    
"""
GENERAL METHODS
=================================================================================
"""

def solve_back(board):
    return board.backtrack_with_min_val(board[0,0])

"""
    Least Constraining Value Heuristic - Sorts teh values available according to their 
                                         the constraints they pose to otehr cells
"""
def is_allowed(cell , value):

    for i in cell.neighbors:
        if (i.cur_val == value):
            return False
            
    return True

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


def main():

    easy = []
    medium = []
    hard = []
    very_hard = []
    evil = []
    
    evil.append('.2.....7....5...4....1..........35...9..7..........1.81.5...6..4...2.......8.....')
    evil.append('8..........36......7..9.2...5...7.......457.....1...3...1....68..85...1..9....4..')
    evil.append('1.......2.9.4...5...6...7...5.9.3.......7.......85..4.7.....6...3...9.8...2.....1')
    
    

    import csv

    f = open('/Users/dimitris/Desktop/370_Final/1000Sudokus.csv')
    csv_f = csv.reader(f)

    for row in csv_f:
        if row[6] == "Easy":
            #print row[2]
            easy.append(row[2])
           
        if row[6] == "Medium":
            #print row[2]
            medium.append(row[2])
            
        if row[6] == "Hard":
            #print row[2]
            hard.append(row[2])
            
        if row[6] == "Very Hard":
            #print row[2]
            very_hard.append(row[2])
            
        if row[6] == "Evil":
            #print row[2]
            evil.append(row[2])
           
    print("Easy: ", len(easy), " Medium: ", len(medium), " Hard: ", len(hard), " Very Hard: ", len(very_hard))
    COUNT = 0
    counter = 0
    total_time = 0
    for puzzle in easy:
        counter = counter + 1
        
        start_board = Board()
        
        for i in range(len(start_board)):
            for j in range(len(start_board)):
                cell = start_board[i,j]
                neigh = start_board.find_neighbors(cell.id[0] , cell.id[1], cell.id[2])
                filled_board = start_board.fill_initial_board(puzzle)
                final = filled_board.initial_values(neigh, cell)
             
       
        start_back = time.time()
        COUNT = COUNT + filled_board.simple_AC3_min_val()
        #solve_back(filled_board)
        end_back = time.time()
        print("For this puzzle: ", (end_back - start_back), " seconds")
        total_time = total_time + (end_back - start_back)
        
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
        
    print("Backtracking Average Time is" , (total_time) / len(easy), "and COUNT = ", COUNT)
    
        
main()