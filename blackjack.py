##MATTHEW_FIOTT_20220105
## V1.2 OFFICIAL BLACKJACK

from random import randint
cardSymbols = ["♠", "⯁", "♥", "♣"]
cardNumbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
cardValues = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

totalpoints = 0
currentHand = []
Aces = 0

def roll():

    global NumberIndex
    Success = 0

    while (Success == 0):

        NumberIndex = randint(0, 12)
        SymbolIndex = randint(0, 3)
        Card = (cardNumbers[NumberIndex] + cardSymbols[SymbolIndex])

        if (Card not in currentHand):
            Success = 1
            currentHand.append(Card)
        else:
            Success = 0

    print("\n", currentHand, "\n\n")
    calculatePoints(cardValues[NumberIndex])

def movechoice():
    select = input("Will you take or hold?\n1: Take\n2: Hold\n")
    if (select == "1"):
        take()
    if (select == "2"):
        hold()
    else:
        movechoice()

def take():
    roll()

def hold():
    endgame(totalpoints)

def calculatePoints(points):
    global totalpoints
    global Aces

    if points == 11:
        Aces += 1
    totalpoints += points
    if totalpoints > 21 and Aces > 0:
        Aces -= 1
        totalpoints -= 10

    elif totalpoints > 21 or totalpoints == 21:
        print("Game Over!")
        endgame(totalpoints)

def endgame(playerpoints):
    enemypoints = randint(12, 21)

    if (playerpoints == 21 or (21 > playerpoints >= enemypoints)):
        print("\nYou won!\n\n Your points: ", playerpoints, "\nopponent's points: ", enemypoints)
    elif (playerpoints > 21 or playerpoints < enemypoints):
        print("\nYou lost :( \n\n Your points: ", playerpoints, "\nopponent's points: ", enemypoints)
    else: #debugging block
        print("\nan error has occurred\n")
        print(totalpoints)
        print(currentHand)
        print(Aces)
    initgame()

def initgame():
    global totalpoints
    global currentHand
    global Aces
    global NumberIndex

    totalpoints = 0
    currentHand = []
    Aces = 0

    print("\n\nNEW GAME\n\n")
    take()
    movechoice()

initgame()
