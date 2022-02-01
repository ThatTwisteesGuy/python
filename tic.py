## initialisations ######################################
plays = 0                                                
grid = [" ", " ", " "], [" ", " ", " "], [" ", " ", " "] 
gridr = [" ", " ", " "], [" ", " ", " "], [" ", " ", " "]
#########################################################

def restart():
    
    print("\n"*10)
    print("New Game!\n\n")
    global current, plays, grid, gridr

    current = "O"
    plays = 0
    grid  = [" ", " ", " "], [" ", " ", " "], [" ", " ", " "]
    gridr = [" ", " ", " "], [" ", " ", " "], [" ", " ", " "]

    show_grid()
    play()

def show_grid():
    # Draws lines and places the symbol in each tile
    print("     |     |     ")
    print(" ", grid[0][0], " | ", grid[0][1], " | ", grid[0][2])
    print("-----|-----|-----")
    print(" ", grid[1][0], " | ", grid[1][1], " | ", grid[1][2])
    print("-----|-----|-----")
    print(" ", grid[2][0], " | ", grid[2][1], " | ", grid[2][2])
    print("     |     |     ")

def play():
    global current
    global plays
    # Tries and catches if input is not an integer from 1-9
    try:
        print("\nIt is now player "+current+"'s turn!\n")
        place = int(input("\nenter the tile you want to play (1-9)"))-1
        # Divides and takes modulo to determine the x and y coordinates on the grid
        y = int(place/3)
        x = int(place % 3)
        # Checks if the tile selected is empty
        if grid[y][x] == " ":

            grid[y][x] = current
            gridr[2 - x][y] = current
            plays = plays + 1
        else:
            print("\nThere is already something in this tile!\n")
    except:
        print("\nInvalid input!\n")
        
    show_grid()
    victoryCheck()

def victoryCheck():
    global current
    # Checks for both players if there are any 3 Os or Xs in a row, horizontally, vertically or diagonally
    for i in range(3):
        if ("O" in grid[i] and (" " not in grid[i]) and ("X" not in grid[i])) or ("O" in gridr[i] and (" " not in gridr[i]) and ("X") not in gridr[i]) or (grid[0][0] == ("O") and grid[1][1] == ("O") and grid[2][2] == ("O")) or (grid[0][2] == ("O") and grid[1][1] == ("O") and grid[2][0] == ("O")):
            print("Player 1 wins!")
            restart()
    for i in range(3):
        if ("X" in grid[i] and (" " not in grid[i]) and ("O" not in grid[i])) or ("X" in gridr[i] and (" " not in gridr[i]) and ("O") not in gridr[i]) or (grid[0][0] == ("X") and grid[1][1] == ("X") and grid[2][2] == ("X")) or (grid[0][2] == ("X") and grid[1][1] == ("X") and grid[2][0] == ("X")):
            print("Player 2 wins!")
            restart()
    # Given that all 9 tiles are filled with no victory, it is set as a tie
    if plays >= 9:
        print("Tie!")
        restart()
    # Changes turns between the players
    if current == "X":
        current = "O"
    elif current == "O":
        current = "X"
    # Calls play()
    play()

restart()
