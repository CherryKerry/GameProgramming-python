'''
Created on 21/07/2014

A simple game where each player get 2 dice rolls, if there
is a double, the player with the highest doubles wins, else
the highest total wins. This game is rigged for the computer
to win 70% of the time

@author: Kerry Powell
'''
from random import randint

def num(s):
    """Convert a string into an int
    
    Keyword arguments:
    s -- string to be converted
    """
    try:
        return int(s)
    except ValueError:
        return 0

def rollDice(rolls):
    """Create an array with dice rolls of 1-6 for each roll
    requested
    
    Keyword arguments:
    rolls -- number of rolls requested
    """
    result = []
    while (rolls > 0):
        result.append(randint(1,6))
        rolls -= 1
    result.sort(reverse=True)
    return result

def playTurn(humanFirst):
    """Plays a turn of the dice off game
    
    Keyword arguments:
    humanFirst -- if the human should go first
    """
    human = rollDice(2)
    computer = rollDice(3)
    if (computer[0] != computer[1] and computer[1] == computer[2]):
        computer[0] = computer[2]
        
    if (humanFirst):
        printDice("Player1", human, "Computer", computer)
    else:
        printDice("Computer", computer, "Player1", human)
    diceResult = compareDice(human, computer)
    if (diceResult < 0):
        return "Computer"
    elif (diceResult > 0):
        return "Player1"
    return "Draw"

def compareDice(human, computer):
    """Determines who the winner of a dice roll off is by returning
    the human score minus the computers score
    
    Keyword arguments:
    human -- the human players dice rolls
    computer -- the computer players dice rolls
    """
    if (human[0] == human[1] and computer[0] == computer[1]):
        return human[0] - computer[0]
    elif (computer[0] == computer[1]):
        return -1
    elif (human[0] == human[1]):
        return 1
    return (human[0] + human[1]) - (computer[0] + computer[1])

def printDice(name1, dice1, name2, dice2):
    """Prints the results of the dice rolls
    
    Keyword arguments:
    name1 -- the first name to print
    dice1 -- the dice to print for the first name
    name2 -- the second name to print
    dice2 -- the dice to print for the second name
    """
    print(" "+name1,"D1="+str(dice1[0]),"D2="+str(dice1[1]))
    print(" "+name2,"D1="+str(dice2[0]),"D2="+str(dice2[1]))
    return

turns = 0
results = []
humanFirst = True
debug = input("Type YES to enter debug mode: ").lower() == "yes"

if (debug):
    "Get the debug rounds number"
    while (not isinstance(turns, int) or turns < 1):
        print("Invalid input!!")
        turns = num(input("How many rounds(positive int): "))
    turns -= 1

while (turns > 0):
    results.append(playTurn(humanFirst))
    if (results[-1] == "Draw"): 
        print("Round was a Draw")
    else:
        print(results[-1],"was the winner")
    turns -= 1
    humanFirst = not humanFirst
    if (not debug):
        if (input("Type STOP to finish the game: ").lower() != "stop"):
            turns = 0
        
if (debug):
    total = len(results)
    human = results.count("Player1")
    computer = results.count("Computer")
    print("Total rounds played="+str(total))
    print("Player1 won",human,"rounds with a winning average of",str(int(human/total*100))+"%")
    print("Computer won",computer,"rounds with a winning average of",str(int(computer/total*100))+"%")