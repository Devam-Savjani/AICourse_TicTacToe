"""
Tic Tac Toe Player
"""

import math
import copy
import sys
import numpy as np

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    numOfX = 0
    numOfO = 0
    for row in board:
        for cell in row:
            if cell == X:
                numOfX += 1
            elif cell == O:
                numOfO += 1
    
    if (numOfX > numOfO):
        return O
    else :
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    res = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                res.add((i,j))
    
    return res



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i = action[0]
    j = action[1]

    if board[i][j] != EMPTY:
        raise Exception("Invalid Action")

    res = copy.deepcopy(board)
    res[i][j] = player(board)
    return res


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    #Checks Horizonally
    for r in rows(board):
        if check_same(r) and r[0] != EMPTY:
            return r[0]

    #Checks Vertically
    for c in cols(board):
        if check_same(c) and c[0] != EMPTY:
            return c[0]
    
    #Checks Diagonals
    for d in diags(board):
        if check_same(d) and d[0] != EMPTY:
            return d[0]
    
    return None


def check_same(array):
    return all(x == array[0] for x in array)
       
  
def rows(board):
    """
    Returns an array of all the rows 
    """
    res = []
    for row in board:
        res.append(row)
    return res

def cols(board):
    """
    Returns an array of all of the columns
    """
    res = []
    for n in range(len(board[0])):
        col = []
        for m in range(len(board)):
            col.append(board[m][n])
        res.append(col)
    return res

def diags(board):
    res = []
    diag1 = []
    diag2 = []
    for n in range(len(board)):
        diag1.append(board[n][n])
        diag2.append(board[n][len(board) - n - 1])
    res.append(diag2)
    res.append(diag1)
    return res


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    else:
        return is_full(board)

def is_full(board):
    """
    Returns True of False depending if the board is full
    """
    numpyBoard = np.array(board)
    emptCount = np.count_nonzero(numpyBoard == EMPTY)
    if (emptCount == 0):
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winnerP = winner(board)
    if winnerP == X:
        return 1
    if winnerP == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if (terminal(board)):
        return None
    else:
        curr_player = player(board)
        if curr_player == X:
            return max_value(board)[1]
        else:
            return min_value(board)[1]
        


def max_value(board):
    #if the board is a terminal board then None to avoid this action
    if terminal(board):
        return (utility(board), None)

    #intitialise the best action and value
    best_action = None
    val = -sys.maxsize - 1

    #for every action that can be made
    for action in actions(board):
        #get the minimum score that can be made by taking such action
        potentialRes = min_value(result(board, action))
        #if this action is better update the best action and the new value 
        if potentialRes[0] > val:
            val = potentialRes[0]
            best_action = action
        if val == 1:
            break
    return (val, best_action)



def min_value(board):

    if terminal(board):
        return (utility(board), None)

    best_action = None
    val = sys.maxsize
    for action in actions(board):
        potentialRes = max_value(result(board, action))
        if potentialRes[0] < val:
            val = potentialRes[0]
            best_action = action
        if val == -1:
            break
    return (val, best_action)
