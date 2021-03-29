import math
import copy

max_player = 'X'
min_player = 'O'


def player(player):
    #define player function
    if player=='X':
        player = 'O'
    else:
        player = 'X'
        
    return player


def actions(state):
    actionList = []
    for r in range(0,3):
        for c in range(0,3):
            if state[r][c] == '-':
                actionList.append((r,c))
    return actionList


def result(state, action, mark):            
    state[action[0]][action[1]] = mark
    return state

def terminal(state):
    
    #Row and Column Check
    for i in range(0,3):
        if state[i][0] == state[i][1] == state[i][2] and state[i][0] != '-':
            return True
        elif state[0][i] == state[1][i] == state[2][i] and state[0][i] != '-':
            return True
    
    #Diagonal Check
    if  state[0][0] == state[1][1] == state[2][2] and state[0][0] != '-':
        return True
    elif state[0][2] == state[1][1] == state[2][0] and state[0][2] != '-':
        return True
    
    #Draw Check
    isTerminal = Truexx
    for row in state:
        for item in row:
            if item == '-':
                isTerminal = False
    
    return isTerminal
    

def utility(state):
    player = ''
    #Row and Column Check
    for i in range(0,3):
        if state[i][0] == state[i][1] == state[i][2] and state[i][0] != '-':
            player = state[i][0]
        elif state[0][i] == state[1][i] == state[2][i] and state[0][i] != '-':
            player = state[0][i]
    
    #Diagonal Check
    if  state[0][0] == state[1][1] == state[2][2] and state[0][0] != '-':
        player = state[0][0]
    elif state[0][2] == state[1][1] == state[2][0] and state[0][2] != '-':
        player = state[0][2]
  
    
    if player == 'X':
        return 1
    elif player == 'O':
        return -1
    
    player = 'Draw'
    #Draw Check
    for row in state:
        for item in row:
            if item == '-':
                player = 'Error::Not a Terminal State'
    

    if player == 'Draw':
        return 0
    else:
        return player



def max_value(state):
    
    if terminal(state):
        return (utility(state), (-1,-1))
        
    v = -math.inf
    nextAction = (-1,-1)
    for action in actions(state):
        temp_v, temp_a = min_value(result(state, action, max_player))
        if v < temp_v:
            v = temp_v
            nextAction = action
            
    return (v, nextAction) 


def min_value(state):

    if terminal(state):
        return (utility(state), (-1,-1))
        
    v = math.inf
    nextAction = (-1,-1)
    for action in actions(state):
        temp_v, temp_s = max_value(result(state, action, min_player))
        
        if v > temp_v:
            v = temp_v
            nextAction = action

    return (v, nextAction)



def printBoard(board):
    for row in board:
        print(row)
            


def tic_tac_toe():

    board = [['-','-','-'],
             ['-','-','-'],
             ['-','-','-']]



    player = input("Choose a player[X/O]: ")
    

    if player == 'X' or player == 'x':
        while True: 
            printBoard(board)
            winner = utility(board)
            if winner == 1:
                print('X is winner')
                break
            elif winner == -1:
                print('O is winner')
                break
            elif winner == 0:
                print('Game Draw')
                break
            r = int(input("Choose Row: "))
            c = int(input("Choose column: "))
            board[r][c] = 'X'
            nextAction = min_value(copy.deepcopy(board))[1]
            board[nextAction[0]][nextAction[1]] = 'O'
            
    elif player == 'O' or player == 'o':
        board[1][1] = 'X'
        while True:
            printBoard(board)
            winner = utility(board)
            if winner == 1:
                print('X is winner')
                break
            elif winner == -1:
                print('O is winner')
                break
            elif winner == 0:
                print('Game Draw')
                break
            r = int(input("Choose Row: "))
            c = int(input("Choose column: "))
            board[r][c] = 'O'
            nextAction = max_value(copy.deepcopy(board))[1]
            board[nextAction[0]][nextAction[1]] = 'X'    

tic_tac_toe()
    
    
    
    
    
    
