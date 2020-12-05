import random

PlayerOne = "Eric"
PlayerTwo = "Kelly"

EricScore = 0
KellyScore = 0

# each dice contains six numbers
diceOne = [1, 2, 3, 4, 5, 6]
diceTwo = [1, 2, 3, 4, 5, 6]

def playDiceGame():
    """#Both Eric and Kelly will roll both the dices using shuffle method"""

    for i in range(5):
        #shuffle both the dice 5 times
        random.shuffle(diceOne)
        random.shuffle(diceTwo)
    firstNumber = random.choice(diceOne) # use choice method to pick one number randomly
    SecondNumber = random.choice(diceTwo)
    return firstNumber + SecondNumber

print("Dice game using a random module\n")

#Let's play Dice game three times
for i in range(3):
    # let's do toss to determine who has the right to play first
    EricTossNumber = random.randint(1, 100) # generate random number from 1 to 100. including 100
    KellyTossNumber = random.randrange(1, 101, 1) # generate random number from 1 to 100. dosen't including 101

    if( EricTossNumber > KellyTossNumber):
        print("Eric won the toss")
        EricScore = playDiceGame()
        KellyScore = playDiceGame()
    else:
        print("Kelly won the toss")
        KellyScore = playDiceGame()
        EricScore = playDiceGame()

    if(EricScore > KellyScore):
        print ("Eric is winner of dice game. Eric's Score is:", EricScore, "Kelly's score is:", KellyScore, "\n")
    else:
        print("Kelly is winner of dice game. Kelly's Score is:", KellyScore, "Eric's score is:", EricScore, "\n")

