def restart():
    # Reset all values
    print("\n" * 10)
    print("New Game!\n\n")

    turns = 0
    counts = [0, 0, 0, 0, 0, 0, 0]
    current_player = "O"
    global grid
    grid = [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " "]

    show_display()
    play(current_player, counts, turns)


def show_display():
    for i in range(6):
        for x in range(7):
            print(" ", grid[x][5-i], " |", end="")
        print("")
        for x in range(7):
            print("-----|", end="")
        print("")


def play(current_player, counts, turns):
    try:
        placement = int(input("Enter the column you want to drop in: "))
        placement -= 1
        if 0 <= placement <= 6:
            if counts[placement] <= 5:
                grid[placement][counts[placement]] = current_player
                counts[placement] = counts[placement]+1
                turns += 1
                victory_check(current_player, counts, placement, turns)

            else:
                print("That column is not available")
                show_display()
                play(current_player, counts, turns)
        else:
            print("out of range")
            play(current_player, counts, turns)
    except :
        print("unknown error", counts)
        play(current_player, counts, turns)


def victory_check(current_player, counts, placement, turns):
    show_display()
    current_location = [placement, counts[placement]-1]
    total1 = check_angle_0(current_location, current_player)
    total2 = check_angle_1(current_location, current_player)
    total3 = check_angle_2(current_location, current_player)
    total4 = check_angle_3(current_location, current_player)

    truetotal = max(total1, total2, total3, total4)
    if truetotal >= 4:
        print("Player "+current_player+" Wins!")
        restart()

    current_player = "X" if current_player == "O" else "O"
    if turns >= 42:
        print("Tie!")
        restart()
    play(current_player, counts, turns)

def check_angle_0(current_location, current_player):
    new_location = [0,0]
    new_location[0] = current_location[0]
    new_location[1] = current_location[1]
    total_linked = 1

    for i in range(4):
        try:
            new_location[1] = new_location[1]-1
            new_location[0] = new_location[0]
            if isInbound(new_location) == False:
                break
            if grid[new_location[0]][new_location[1]] == current_player:
                total_linked = total_linked + 1
            else:
                break
        except:
            break

    #print(total_linked)
    #print(current_location)
    return total_linked

def check_angle_1(current_location, current_player):
    new_location = [0,0]
    new_location[0] = current_location[0]
    new_location[1] = current_location[1]
    total_linked = 1

    for i in range(4):
        try:
            new_location[1] = new_location[1] + 1
            new_location[0] = new_location[0] + 1
            #print(new_location)
            if isInbound (new_location) == False:
                break

            if grid[new_location[0]][new_location[1]] == current_player:
                total_linked = total_linked + 1
            else:
                break
        except:
            break

    new_location[0] = current_location[0]
    new_location[1] = current_location[1]

    for i in range(4):
        try:
            new_location[1] = new_location[1] - 1
            new_location[0] = new_location[0] - 1
            #print(new_location)
            if isInbound (new_location) == False:
                break

            if grid[new_location[0]][new_location[1]] == current_player:
                total_linked = total_linked + 1
            else:
                break
        except:
            break

    #print(total_linked)
    #print(current_location)
    return total_linked

def check_angle_2(current_location, current_player):
    new_location = [0,0]
    new_location[0] = current_location[0]
    new_location[1] = current_location[1]
    total_linked = 1

    for i in range(4):
        try:
            new_location[1] = new_location[1] + 0
            new_location[0] = new_location[0] + 1
            #print(new_location)
            if isInbound (new_location) == False:
                break

            if grid[new_location[0]][new_location[1]] == current_player:
                total_linked = total_linked + 1
            else:
                break
        except:
            break

    new_location[0] = current_location[0]
    new_location[1] = current_location[1]

    for i in range(4):
        try:
            new_location[1] = new_location[1] - 0
            new_location[0] = new_location[0] - 1
            #print(new_location)
            if isInbound (new_location) == False:
                break

            if grid[new_location[0]][new_location[1]] == current_player:
                total_linked = total_linked + 1
            else:
                break
        except:
            break

    #print(total_linked)
    #print(current_location)
    return total_linked


def check_angle_3(current_location, current_player):
    new_location = [0,0]
    new_location[0] = current_location[0]
    new_location[1] = current_location[1]
    total_linked = 1

    for i in range(4):
        try:
            new_location[1] = new_location[1] - 1
            new_location[0] = new_location[0] + 1
            #print(new_location)
            if isInbound (new_location) == False:
                break

            if grid[new_location[0]][new_location[1]] == current_player:
                total_linked = total_linked + 1
            else:
                break
        except:
            break

    new_location[0] = current_location[0]
    new_location[1] = current_location[1]

    for i in range(4):
        try:
            new_location[1] = new_location[1] + 1
            new_location[0] = new_location[0] - 1
            #print(new_location)
            if isInbound (new_location) == False:
                break

            if grid[new_location[0]][new_location[1]] == current_player:
                total_linked = total_linked + 1
            else:
                break
        except:
            break

    #print(total_linked)
    #print(current_location)
    return total_linked

def isInbound(subject_location):
    if (0 <= subject_location[0] <= 6) and (0 <= subject_location[1] <= 5):
        #print(subject_location, " = In Bound")
        return True
    else:
        #print(subject_location, " = Out Bound")
        return False

restart()
