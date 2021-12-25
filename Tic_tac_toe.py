#dashboard
dboard = [
  "-","-","-",
  "-","-","-",
  "-","-","-"]

gameIsGoingOn = True
winner = None
activePlayer = "X"

#display dashboard on the screen
def dispDashBoard():
    print(dboard[0] + " | " + dboard[1] + " | " + dboard[2])
    print(dboard[3] + " | " + dboard[4] + " | " + dboard[5])
    print(dboard[6] + " | " + dboard[7] + " | " + dboard[8])


#then we can start playing game

def playingGame():
    #display the dashboard at first
    dispDashBoard()
    
    while gameIsGoingOn:
         nextPlayersTurn(activePlayer)

         #check if the game is over
         checkIfGameIsOver()

         #then next player
         nextPlayer()

   #when the loop ended
    if winner == "X" or winner == "O":
       print(winner + "won .")
    elif(winner == None):
        print("stop")

def nextPlayersTurn(player):

    print(player + "'s turn.")
    numInput = input("choose number from 1 through 9: ")
    
    valid = False
    while not valid:

        while numInput not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            numInput = input("invalid input, plz choose a number from 1 through 9:")

        numInput = int(numInput) - 1

        if dboard[numInput] != "-":
            valid = True

            print("not allowed to go there, go again")

    dboard[numInput] = player

    dispDashBoard()
#check if the game is over 
def checkIfGameIsOver():
    #check if win
    checkForTheWinner()
    #check if there is a restriction 
    checkAnyRestriction()

def checkForTheWinner():
    global winner
    #check rows
    rowWinner = checkRows()
    #check columns
    columnWinner = checkColums()
    #check diagonals
    diagonalWinner = checkDiagonals()
    return

    if rowWinner:
        #on row there is a win
        winner = rowWinner
    elif columnWinner:
        #on column there is a win
        winner = columnWinner
    elif diagonalWinner:
        #on diagonal there is a win
        winner = diagonalWinner
    else:
        winner = None

def checkRows():
    global gameIsGoingOn

    firstRow = dboard[0] == dboard[1] == dboard[2] != "-"
    secondRow = dboard[3] == dboard[4] == dboard[5] != "-"
    thirdRow = dboard[6] == dboard[7] == dboard[8] != "-"

    #check if any of the row matches the conditions
    if firstRow or secondRow or thirdRow:
        gameIsGoingOn = False

    if firstRow:
        return dboard[0]
    elif secondRow:
        return dboard[3]
    elif thirdRow:
        return dboard[6]         

    return
    
def checkColums():
    #some code here
    global gameIsGoingOn

    firstColumn = dboard[0] == dboard[3] == dboard[6] != "-"
    secondColumn = dboard[1] == dboard[4] == dboard[7] != "-"
    thirdColumn = dboard[2] == dboard[5] == dboard[8] != "-"

    if firstColumn or secondColumn or thirdColumn:
        gameIsGoingOn = False
    
    if firstColumn:
        return dboard[0]
    elif secondColumn:
        return dboard[1]
    elif thirdColumn:
        return dboard[2]

    return    

def checkDiagonals():
    #some code here
    global gameIsGoingOn

    firstDiagonal = dboard[0] == dboard[4] == dboard[8] != "-"
    secondDiagonal = dboard[2] == dboard[4] == dboard[6] != "-"

    if firstDiagonal or secondDiagonal:
        gameIsGoingOn = False
    
    if firstDiagonal:
        return dboard[0]
    elif secondDiagonal:
        return dboard[2] 

    return             
   
def checkAnyRestriction():
    global gameIsGoingOn

    #return sthing
    if "-" not in dboard:
        gameIsGoingOn = False
        return True
    else:
         return False

def nextPlayer():
    global activePlayer

    if activePlayer == "X":
        activePlayer = "O"

    elif activePlayer == "O":
        activePlayer = "X"

    return        

playingGame()    
 