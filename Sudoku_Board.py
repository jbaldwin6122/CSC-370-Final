
class Cell:

    def __init__(self, id):
        self.id = id
        self.values = []

    def add_value(self, number):
        self.values.append(number)

    def get_values(self):
        return self.values
    

class Board:

    """
    Represents a Board in the form of an array list with 9 arrays
    """


    def __init__(self):

        rows = []

        row_1 = [Cell("A11"), Cell("A12" ) , Cell("A13") , Cell("A14"), Cell("A15"), Cell("A16"), Cell("A17"), Cell("A18"), Cell("A19")]
        rows.append(row_1)
        
        row_2 = [Cell("B11"), Cell("B12" ) , Cell("B13") , Cell("B14"), Cell("B15"), Cell("B16"), Cell("B17"), Cell("B18"), Cell("B19")]
        rows.append(row_2)

        row_3 = [Cell("C11"), Cell("C12" ) , Cell("C13") , Cell("C14"), Cell("C15"), Cell("C16"), Cell("C17"), Cell("C18"), Cell("C19")]
        rows.append(row_3)
        
        row_4 = [Cell("D11"), Cell("D12" ) , Cell("D13") , Cell("D14"), Cell("D15"), Cell("D16"), Cell("D17"), Cell("D18"), Cell("D19")]
        rows.append(row_4)

        row_5 = [Cell("E11"), Cell("E12" ) , Cell("E13") , Cell("E14"), Cell("E15"), Cell("E16"), Cell("E17"), Cell("E18"), Cell("E19")]
        rows.append(row_5)
        
        row_6 = [Cell("F11"), Cell("F12" ) , Cell("F13") , Cell("F14"), Cell("F15"), Cell("F16"), Cell("F17"), Cell("F18"), Cell("F19")]
        rows.append(row_6)

        row_7 = [Cell("G11"), Cell("G12" ) , Cell("G13") , Cell("G14"), Cell("G15"), Cell("G16"), Cell("G17"), Cell("G18"), Cell("G19")]
        rows.append(row_7)
        
        row_8 = [Cell("H11"), Cell("H12" ) , Cell("H13") , Cell("H14"), Cell("H15"), Cell("H16"), Cell("H17"), Cell("H18"), Cell("H19")]
        rows.append(row_8)

        row_9 = [Cell("I11"), Cell("I12" ) , Cell("I13") , Cell("I14"), Cell("I15"), Cell("I16"), Cell("I17"), Cell("I18"), Cell("I19")]
        rows.append(row_9)
       
        

        self.board = [[y for y in row] for row in rows]

    def fill_initial_board(self, str_board):
        
        count = 0
        for c in str_board:
            list1 = []
            row = count / 9
            col = count % 9
            if(c != "."):
                self.board[row][col].add_value(c)
            count = count + 1
        
        return self.board

    def board_pretty_print(self):

        for row in len(self.board):
            for col in len(self.board[0]):
                print(self.board[row][col].get_values)


def main():

    start_board = Board()

    filled_board = start_board.fill_initial_board("5..3.6.92.69...15....51.8.....69..2.67...8..99....2.8.....8.5.3..32.7..4.14.3....")

    for i in range(len(filled_board)):
        for j in range(len(filled_board[0])):
            print(filled_board[i][j].get_values()),
        print("")

    return

main()