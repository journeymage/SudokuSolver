import re


class puzzle:
    puzzleList = []
    isSet = []
    columns = []
    blocks = []

    def __init__(self):
        """
        Creates puzzle.
        """
        self.puzzleList = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                           ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                           ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                           ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                           ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]
        self.isSet = [[False, False, False, False, False, False, False, False, False],
                      [False, False, False, False, False, False, False, False, False],
                      [False, False, False, False, False, False, False, False, False],
                      [False, False, False, False, False, False, False, False, False],
                      [False, False, False, False, False, False, False, False, False],
                      [False, False, False, False, False, False, False, False, False],
                      [False, False, False, False, False, False, False, False, False],
                      [False, False, False, False, False, False, False, False, False],
                      [False, False, False, False, False, False, False, False, False]]
        self.columns = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]
        self.blocks = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                       ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                       ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                       ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
                       ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]

    def setPuzzle(self, file):
        """
        Adds values to puzzle from file.
        :param file: str
        :return:
        """
        openFile = open(file, 'r')
        count = 0
        puzzleList1 = []
        for line in openFile:
            if len(list(line.strip())) == 9:
                puzzleList1.append(list(line.strip()))
                count += 1
            else:
                openFile.close()
                return
        openFile.close()
        if len(puzzleList1) != 9:
            return
        self.puzzleList = puzzleList1
        for row in range(9):
            for col in range(9):
                if re.match('[0-9]', self.puzzleList[row][col]):
                    self.isSet[row][col] = True
        self.columns = []
        for col in range(9):
            self.columns.append([])
            for row in range(9):
                self.columns[col].append(self.puzzleList[row][col])
        self.blocks = []
        for block in range(9):
            self.blocks.append([])
            for row in range(3):
                for col in range(3):
                    self.blocks[block].append(self.puzzleList[row + block // 3 * 3][col + block % 3 * 3])

    def checkRow(self, row, val):
        """
        Checks to see if a value is in a row returns True if the value is in the row.
        :param row: int
        :param val: int
        :return: bool
        """
        if row < 0 or row >= 9:
            return False
        elif val < 1 or val > 9:
            return False
        else:
            return str(val) in self.puzzleList[row]

    def checkCol(self, col, val):
        """
        Checks to see if a value is in a col returns True if the value is in the row.
        :param col: int
        :param val: int
        :return: bool
        """
        if col < 0 or col >= 9:
            return False
        elif val < 1 or val > 9:
            return False
        else:
            return str(val) in self.columns[col]

    def checkBlock(self, row, col, val):
        """
        Checks to see if a value is in a block if it is it returns True.
        :param row: int
        :param col: int
        :param val: int
        :return: bool
        """
        if row < 0 or row >= 9:
            return False
        elif col < 0 or col >= 9:
            return False
        elif val < 1 or val > 9:
            return False
        else:
            if row < 3 and col < 3:
                return str(val) in self.blocks[0]
            elif row < 3 and 2 < col < 6:
                return str(val) in self.blocks[1]
            elif row < 3 and 5 < col < 9:
                return str(val) in self.blocks[2]
            elif row < 6 and col < 3:
                return str(val) in self.blocks[3]
            elif row < 6 and 2 < col < 6:
                return str(val) in self.blocks[4]
            elif row < 6 and 5 < col < 9:
                return str(val) in self.blocks[5]
            elif row < 9 and col < 3:
                return str(val) in self.blocks[6]
            elif row < 9 and 2 < col < 6:
                return str(val) in self.blocks[7]
            else:
                return str(val) in self.blocks[8]

    def checkSpot(self, row, col, val):
        """
        Checks to see if row, col, block, set, or occupied and returns true if any conditions are met.
        :param row: int
        :param col: int
        :param val: int
        :return: bool
        """
        if row < 0 or row >= 9:
            return False
        elif col < 0 or col >= 9:
            return False
        elif val < 1 or val > 9:
            return False
        return (self.checkRow(row, val) or self.checkCol(col, val) or self.checkBlock(row, col, val) or self.isSet[row][
            col] or not self.occupied(row, col))

    def isDefined(self, row, col):
        """
        Tells if a cell is predefined.
        :param row: int
        :param col: int
        :return: bool
        """
        if row < 0 or row >= 9:
            return False
        elif col < 0 or col >= 9:
            return False
        return self.isSet[row][col]

    def setValue(self, row, col, val):
        """
        Sets the value of a cell if and only if it is valid. Returns True if successful.
        :param row: int
        :param col: int
        :param val: int
        :return: bool
        """
        val = int(val)
        if row < 0 or row >= 9:
            return False
        elif col < 0 or col >= 9:
            return False
        elif val < 1 or val > 9:
            return False
        elif self.isSet[row][col]:
            return False
        elif not (self.checkSpot(row, col, val)):
            self.puzzleList[row][col] = str(val)
            self.columns[col][row] = str(val)
            if row < 3 and col < 3:
                self.blocks[0][row % 3 * 3 + col % 3] = str(val)
            elif row < 3 and col < 6:
                self.blocks[1][row % 3 * 3 + col % 3] = str(val)
            elif row < 3 and col < 9:
                self.blocks[2][row % 3 * 3 + col % 3] = str(val)
            elif row < 6 and col < 3:
                self.blocks[3][row % 3 * 3 + col % 3] = str(val)
            elif row < 6 and col < 6:
                self.blocks[4][row % 3 * 3 + col % 3] = str(val)
            elif row < 6 and col < 9:
                self.blocks[5][row % 3 * 3 + col % 3] = str(val)
            elif row < 9 and col < 3:
                self.blocks[6][row % 3 * 3 + col % 3] = str(val)
            elif row < 9 and col < 6:
                self.blocks[7][row % 3 * 3 + col % 3] = str(val)
            else:
                self.blocks[8][row // 3 * 3 + col % 3] = str(val)
            return True
        else:
            return False

    def __copyValue(self, row, col, val):
        """
        For internal use to make a copy of a puzzle.
        :param row: int
        :param col: int
        :param val: int
        :return: bool
        """
        self.puzzleList[row][col] = val
        self.columns[col][row] = val
        if row < 3 and col < 3:
            self.blocks[0][row % 3 * 3 + col % 3] = val
        elif row < 3 and col < 6:
            self.blocks[1][row % 3 * 3 + col % 3] = val
        elif row < 3 and col < 9:
            self.blocks[2][row % 3 * 3 + col % 3] = val
        elif row < 6 and col < 3:
            self.blocks[3][row % 3 * 3 + col % 3] = val
        elif row < 6 and col < 6:
            self.blocks[4][row % 3 * 3 + col % 3] = val
        elif row < 6 and col < 9:
            self.blocks[5][row % 3 * 3 + col % 3] = val
        elif row < 9 and col < 3:
            self.blocks[6][row % 3 * 3 + col % 3] = val
        elif row < 9 and col < 6:
            self.blocks[7][row % 3 * 3 + col % 3] = val
        else:
            self.blocks[8][row // 3 * 3 + col % 3] = val

    def clearValue(self, row, col):
        """
        Removes value if it is not set by the file.
        :param row: int
        :param col: int
        :return:
        """
        if row < 0 or row >= 9:
            return False
        elif col < 0 or col >= 9:
            return False
        else:
            if not self.isSet[row][col]:
                self.puzzleList[row][col] = 'X'
                self.columns[col][row] = 'X'
                if row < 3 and col < 3:
                    self.blocks[0][row % 3 * 3 + col % 3] = 'X'
                elif row < 3 and col < 6:
                    self.blocks[1][row % 3 * 3 + col % 3] = 'X'
                elif row < 3 and col < 9:
                    self.blocks[2][row % 3 * 3 + col % 3] = 'X'
                elif row < 6 and col < 3:
                    self.blocks[3][row % 3 * 3 + col % 3] = 'X'
                elif row < 6 and col < 6:
                    self.blocks[4][row % 3 * 3 + col % 3] = 'X'
                elif row < 6 and col < 9:
                    self.blocks[5][row % 3 * 3 + col % 3] = 'X'
                elif row < 9 and col < 3:
                    self.blocks[6][row % 3 * 3 + col % 3] = 'X'
                elif row < 9 and col < 6:
                    self.blocks[7][row % 3 * 3 + col % 3] = 'X'
                else:
                    self.blocks[8][row // 3 * 3 + col % 3] = 'X'

    def solved(self):
        """
        Checks to see if the puzzle is solved.
        :return: bool
        """
        for row in self.puzzleList:
            if 'X' in row:
                return False
        return True

    def getValue(self, row, col):
        """
        Returns the value of a cell if it is set else returns false.
        :param row: int
        :param col: int
        :return:
        """
        if row < 0 or row >= 9:
            return False
        elif col < 0 or col >= 9:
            return False
        else:
            if re.match('[0-9]', self.puzzleList[row][col]):
                return self.puzzleList[row][col]
            else:
                return False

    def occupied(self, row, col):
        """
        Returns whether a cell is occupied.
        :param row: int
        :param col: int
        :return: bool
        """
        if row < 0 or row >= 9:
            return False
        elif col < 0 or col >= 9:
            return False
        else:
            if self.getValue(row, col) == False:
                return True
            else:
                return False

    def toString(self):
        """
        Coverts puzzle to a string.
        :return: str
        """
        stringOut = ''
        for row in range(9):
            if row % 3 == 0 and row != 0: stringOut += '\n' + '-' * 11
            stringOut += '\n'
            for col in range(9):
                if col % 3 == 0 and col != 0: stringOut += '|'
                if self.getValue(row, col):
                    stringOut += self.getValue(row, col)
                else:
                    stringOut += 'X'
        return stringOut.strip()

    def makeCopy(self):
        """
        Makes a copy of the puzzle.
        :return: puzzle
        """
        newPuzzle = puzzle()
        for row in range(9):
            for col in range(9):
                newPuzzle.__copyValue(row, col, self.puzzleList[row][col])
        return newPuzzle

    def validPuzzle(self):
        """
        Checks to see if the puzzle is valid. No repeating numbers.
        :return: bool
        """
        for row in self.puzzleList:
            for val in range(1, 10):
                count = 0
                for cell in row:
                    if str(val) == cell:
                        count += 1
                if count > 1:
                    return False
        for col in self.columns:
            for val in range(1, 10):
                count = 0
                for cell in col:
                    if str(val) == cell:
                        count += 1
                if count > 1:
                    return False
        for block in self.blocks:
            for val in range(1, 10):
                count = 0
                for cell in block:
                    if str(val) == cell:
                        count += 1
                if count > 1:
                    return False
        return True

    def toFile(self, fileName):
        """
        Outputs the puzzle to a file.
        :param fileName: str
        :return:
        """
        openFile = open(fileName, 'w')
        for row in self.puzzleList:
            openFile.write(''.join(row) + '\n')
        openFile.close()
