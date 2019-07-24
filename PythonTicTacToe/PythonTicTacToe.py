
#Practice: Logic, namespace, and syntax
#TICTACTOE
#EWH @7.24.19

#random number generator for determining who goes first
import random
#our board
board = ['A','Z','Z','Z','Z','Z','Z','Z','Z','Z']
#our turn keeper
turnkeeper = True


#calling this will draw our board
def DrawTheBoard(board):
	print(board[7]+'|'+board[8]+'|'+board[9])
	print(board[4]+'|'+board[5]+'|'+board[6])
	print(board[1]+'|'+board[2]+'|'+board[3])

#determines who goes first, using the FirstBool
def whoGoesFirst():
		randomint = random.randint(0,1)
		if randomint == 0:
			print("Player X goes first")
			return True
		else:
			print("Player O goes first")
			return False

#assign the players from input (first come first serve)
def PlayerAssignment():
	playerletter=""
	while not (playerletter == "X" or playerletter == "O"):
		print("Please Select Your Token (O or X)")
		playerletter = input().upper()
	
	if playerletter == "X":
		return ["X","O"]
	else:
		return ["O","X"]

#check all the possible 3 in a rows
def whoHasWon(B, L):
    if ((B[7] == L and B[8] == L and B[9] == L) or #across the top
	  (B[4] == L and B[5] == L and B[6] == L) or #across the mid
	  (B[1] == L and B[2] == L and B[3] == L) or #across the bottom
	  (B[7] == L and B[4] == L and B[1] == L) or #down the right
	  (B[8] == L and B[5] == L and B[2] == L) or #down the middle
	  (B[9] == L and B[6] == L and B[3] == L) or #down the right
	  (B[7] == L and B[5] == L and B[3] == L) or #diagonal backslash
	  (B[1] == L and B[5] == L and B[9] == L)): #diagonal forwardslash
         print("Player "+ L +" has won the game!")
         DrawTheBoard(board)
         return True



#check to see if there is a freespace
def FreeSpace(board, move):
    if board[move] == "Z":
        return True
    else:
        return False

def BoardFull(board):
    if "Z" in board:
            return False
    else: return True

#turnkeeper flips every time enforcing the turn order
def PlayerMove():
    global turnkeeper
    global board

    playerinput = int(input())


    if (BoardFull(board) == False and FreeSpace(board, playerinput) == True):
        if turnkeeper == True:
            board[playerinput] = "X"
        else:
            board[playerinput] = "O"
    elif (BoardFull(board) == True):
        DrawTheBoard(board)
        print("Board is Full")
        return
    else:
        print("Invalid Input")
    turnkeeper = not turnkeeper
    return


DrawTheBoard(board)

Playersymbols = PlayerAssignment()

turnkeeper = whoGoesFirst()


for i in range(0,11):
    DrawTheBoard(board)
    PlayerMove()
    if turnkeeper == True:
        if whoHasWon(board, "O"):
            input()
            break
    else:
        if whoHasWon(board, "X"):
            input()
            break
    if BoardFull(board) == True:
        print("The Game is a Tie")
        input()
        break
    i+=1

