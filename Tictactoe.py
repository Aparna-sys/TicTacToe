def insertLetter(letter,pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

def printBoard(board):
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def IsWinner(b,l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l))

def playerMove():
    run = True
    while run:
        move = input("\nPlease select a position to enter the 'X' between 1 to 9: ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X' , move)
                else:
                    print(']\nSorry, this space is occupied!')
            else:
                print('\nPlease type a number between 1 and 9:')

        except:
            print('\nPlease type a number!')

def computerMove():
    possibleMoves = [x for x , letter in enumerate(board) if letter == ' ' and x != 0  ]
    move = 0

    for let in ['O' , 'X']:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if IsWinner(boardcopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1 , 3 , 7 , 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def main():
    while not(isBoardFull(board)):
        if not(IsWinner(board , 'O')):
            playerMove()
            printBoard(board)
        else:
            print("\nSorry you loose!")
            break
        
        if not(isBoardFull(board)):
            if not(IsWinner(board , 'X')):
                move = computerMove()
                if move == 0:
                    print(" ")
                else:
                    insertLetter('O' , move)
                    print("\nComputer placed an 'O' on position" , move , ':')
                    printBoard(board)
            else:
                print("\nCongratulations!! you win!")
                break

        else:
            print("\nTie game!")
if __name__ == "__main__":
    print("\n*****************Tic-Tac-Toe-Game****************************")
    board = [' ' for x in range(10)]
    printBoard(board)
    print("\nDo you want to play?")
    x=input("Press 'Y' for Yes 'N' for No: ").lower()
    while x != 'n':
        if x == 'y':
            board = [' ' for x in range(10)]
            print('\n--------------------------Welcome to the game!------------------------------')
            main()
            print("\nDo you want to play again?")
            x = input("Press 'Y' for Yes 'N' for No: ").lower()
        else:
            x = input("\nPlease Enter only 'Y' for Yes and 'N' for No: ").lower()
    else:
        print("\nThank you for giving your time!")
        print("Have a Nice day!")
