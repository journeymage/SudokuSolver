from Puzzle import puzzle
import time
import threading


def generatePossible(puz: puzzle) -> list:
    """
    This function takes in a puzzle and returns a 2D list of all the valid moves for a space.
    :param puz: puzzle
    :return: list
    """
    poss = []
    for row in range(9):
        poss.append([])
        for col in range(9):
            poss[row].append([])
            for val in range(1, 10):
                if not puz.checkSpot(row, col, val):
                    poss[row][col].append(val)
    return poss


def findNextEmpty(puz: puzzle, i: int, j: int) -> tuple:
    """
    This function goes through a puzzle and returns a tuple of the coordinates of the next empty cell, if none found
    then -1,-1 is returned.
    :param puz: puzzle
    :param i: int
    :param j: int
    :return: tuple
    """
    for row in range(i, 9):
        for col in range(j, 9):
            if not puz.getValue(row, col):
                return row, col
    for row in range(9):
        for col in range(9):
            if not puz.getValue(row, col):
                return row, col
    return -1, -1


def eliminateSingles(puz: puzzle) -> None:
    """
    This function iterates through a puzzle and if only one value is possible for a cell it fills it with that value.
    :param puz: puzzle
    :return:
    """
    poss = generatePossible(puz)
    for row in range(9):
        for col in range(9):
            if len(poss[row][col]) == 1:
                puz.setValue(row, col, poss[row][col][0])
                poss = generatePossible(puz)


def solveSingles(puz: puzzle) -> None:
    """
    This function goes through and solves all the singles of a puzzle until none are left.
    :param puz: puzzle
    :return:
    """
    poss1 = []
    poss2 = generatePossible(puz)
    while not puz.solved() and poss2 != poss1:
        poss1 = poss2
        eliminateSingles(puz)
        poss2 = generatePossible(puz)


def eliminateHidden(puz: puzzle) -> None:
    """
    This function takes in a puzzle and solves all the hidden singles one time.
    :param puz: puzzle
    :return:
    """
    # Checking for hidden singles in rows
    for row in range(9):
        for val in range(1, 10):
            count = 0
            poss = generatePossible(puz)
            for col in range(9):
                if val in poss[row][col]:
                    count += 1
                    rowPoss = row
                    colPoss = col
            if count == 1:
                puz.setValue(rowPoss, colPoss, val)
    # Checking for hidden singles in columns
    for col in range(9):
        for val in range(1, 10):
            count = 0
            poss = generatePossible(puz)
            for row in range(9):
                if val in poss[row][col]:
                    count += 1
                    rowPoss = row
                    colPoss = col
            if count == 1:
                puz.setValue(rowPoss, colPoss, val)
    # Checking for hidden singles in blocks
    for block in range(9):
        for val in range(1, 10):
            count = 0
            poss = generatePossible(puz)
            for row in range(3):
                for col in range(3):
                    if val in poss[row + block // 3 * 3][col + block % 3 * 3]:
                        count += 1
                        rowPoss = row
                        colPoss = col
            if count == 1:
                puz.setValue(rowPoss, colPoss, val)


def solveHidden(puz: puzzle) -> None:
    """
    Loops through the puzzle until all the hidden have been solved.
    :param puz: puzzle
    :return:
    """
    poss1 = []
    poss2 = generatePossible(puz)
    while not puz.solved() and poss2 != poss1:
        poss1 = poss2
        eliminateHidden(puz)
        poss2 = generatePossible(puz)


def bruteForce(puz: puzzle, row: int = 0, col: int = 0) -> bool:
    """
    Systematically goes through the puzzle and back tracks on dead end until puzzle is solved.
    :param puz: puzzle
    :param col: int
    :param row: int
    :return: bool
    """
    poss = generatePossible(puz)
    row, col = findNextEmpty(puz, row, col)
    if row == -1:
        return True
    for val in poss[row][col]:
        if puz.setValue(row, col, val):
            if bruteForce(puz, row, col):
                return True
        puz.clearValue(row, col)
    return False


def solve(puz: puzzle) -> None:
    """
    Main code for solving a single puzzle.
    :param puz:
    :return:
    """
    poss1 = []
    poss2 = generatePossible(puz)
    # Makes sure all single and hidden solved
    while not puz.solved() and poss2 != poss1:
        poss1 = poss2
        solveSingles(puz)
        solveHidden(puz)
        poss2 = generatePossible(puz)
    # If it is not solved move into brute forcing the solution
    if puz.validPuzzle():
        if not puz.solved():
            print('Some brute force required.')
            try:
                # Opens thread to run brute force on
                thread = threading.Thread(target=bruteForce, args=[puz], daemon=True)
                thread.start()
                count = 0
                # Counts how much time has passed to make sure not to long has gone, and that the thread is still alive
                while not puz.solved() and count < 300 and thread.is_alive():
                    time.sleep(.5)
                    count += 1
            except:
                print('Threading error.')
        if not puz.solved():
            print('Puzzle was unable to be solved.')
    else:
        print('Invalid puzzle')


if __name__ == '__main__':
    puzzle1 = puzzle()
    fileName = 'puzzle5'
    puzzle1.setPuzzle(f'{fileName}.txt')
    if puzzle1.validPuzzle():
        print(puzzle1.toString())
        print('Solving...')
        solve(puzzle1)
        print(puzzle1.toString())
        puzzle1.toFile(f'{fileName}.sln.txt')
    else:
        print('Puzzle not a valid puz.')
