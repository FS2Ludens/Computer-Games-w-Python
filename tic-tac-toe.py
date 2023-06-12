#Tic-Tac-Toe

import random

def DrawBoard(board):
    #This function prints out the board that it was passed

    #"board" is a list of 10 strings representing the board (ingnore index 0)
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def InputPlayerLetter():
    #Lets the player input the letter they want
    #Returns a list with the player's letter as the first item and the computer's letter as the second
    letter = ''
    while not (letter == 'X' or letter == '0'):
        print('Do you want to be X or 0?')
        letter = input().upper()

    #The first element in the list is the player's letter; the second is the computer's letter
    if letter == 'X':
        return ['X', '0']
    else:
        return ['0', 'X']

def WhoGoesFirst():
    #randomly choose which player goes first
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def MakeMove(board, letter, move):
    board[move] = letter

def IsWinner(bo, le):
    #Given a board and a player's letter, this function returns TRUE if that player has won
    #WE use "bo" instead of "Board" and "le" instead of "letter" so we don't have to type as much
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or #accross the top
        (bo[4] == le and bo[5] == le and bo[6] == le) or #accross the middle
        (bo[1] == le and bo[2] == le and bo[3] == le) or #accross the bottom
        (bo[7] == le and bo[4] == le and bo[1] == le) or #down the left side
        (bo[8] == le and bo[5] == le and bo[2] == le) or #down the middle
        (bo[9] == le and bo[6] == le and bo[3] == le) or #down the right side
        (bo[7] == le and bo[5] == le and bo[3] == le) or #diagonal top left to bottom right
        (bo[9] == le and bo[5] == le and bo[1] == le)) #diagonal from top right to bottom left

def GetBoardCopy(board):
    #make a copy of the board list and return it
    BoardCopy = []
    for i in board:
        BoardCopy.append(i)
    return BoardCopy

def IsSpaceFree(board, move):
    #return TRUE if the passed move is free on the passed board
    return board[move] == ' '

def GetPlayerMove(board):
    #let the player enter their move
    move = ' '
    while move not in ' 1 2 3 4 5 6 7 8 9'.split() or not IsSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def ChooseRandomMoveFromList(board, MovesList):
    #returns a valid move from the passed list from the passed board
    #returns none if there is no valid move
    PossibleMoves = []
    for i in MovesList:
        if IsSpaceFree(board, i):
            PossibleMoves.append(i)

    if len(PossibleMoves) != 0:
        return random.choice(PossibleMoves)
    else:
        return None

def GetComputerMove(board, ComputerLetter):
    #given a board and the computer's letter, determine where to move and return that move
    if ComputerLetter == 'X':
        PlayerLetter = '0'
    else:
        PlayerLetter = 'X'

    #here is the algorithm  for our tic-tac-toe AI:
    #first, check if we can win in the next move
    for i in range(1, 10):
        BoardCopy = GetBoardCopy(board)
        if IsSpaceFree(BoardCopy, i):
            MakeMove(BoardCopy, ComputerLetter, i)
            if IsWinner(BoardCopy, ComputerLetter):
                return i

    #check if the player can win on the next move and block them
    for i in range(1, 10):
        BoardCopy = GetBoardCopy(board)
        if IsSpaceFree(BoardCopy, i):
            MakeMove(BoardCopy, PlayerLetter, i)
            if IsWinner(BoardCopy, PlayerLetter):
                return i

    #try to take one of the corners if they are free
    move = ChooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    #try to take the center if it is free
    if IsSpaceFree(board, 5):
        return 5

    #move on one of the sides
    return ChooseRandomWordFromList(board, [2, 4, 6, 8])

def IsBoardFull(board):
    #return TRUE if every space on the board has been taken. Otherwise, return FALSE
    for i in range(1, 10):
        if IsSpaceFree(board, i):
            return False
    return True


print('Welcome to Tic-Tac-Toe')

while True:
    #reset the board
    TheBoard = [' '] * 10
    PlayerLetter, ComputerLetter = InputPlayerLetter()
    turn = WhoGoesFirst()
    print('The ' + turn + ' will go first.')
    GameIsPlaying = True

    while GameIsPlaying:
        if turn == 'player':
            #player's turn
            DrawBoard(TheBoard)
            move = GetPlayerMove(TheBoard)
            MakeMove(TheBoard, PlayerLetter, move)

            if IsWinner(TheBoard, PlayerLetter):
                DrawBoard(TheBoard)
                print('Hooray! You have won the game!')
                GameIsPlaying = False
            else:
                if IsBoardFull(TheBoard):
                    DrawBoard(TheBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'

        else:
            #computer's turn
            move = GetComputerMove(TheBoard, ComputerLetter)
            MakeMove(TheBoard, ComputerLetter, move)

            if IsWinner(TheBoard, ComputerLetter):
                DrawBoard(TheBoard)
                print('The computer has beaten you! You lose.')
                GameIsPlaying = False
            else:
                if IsBoardFull(TheBoard):
                    DrawBoard(TheBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break
