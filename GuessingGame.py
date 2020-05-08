#This is a guessing game between 1 and 1000
# Each guess game tells if you are too high or too low.
#You start with 10 points


from random import randrange


def intro():
    print("****")
    print("Random Number here")
    print("Choose between 1-1000 Bro.")
    print("You got 10 guesses")
    print("Big Time Wrong")
    print("Play however times you want fam")
    print("*****")
    

def getName():
    name=input("What's your name")
    return name


def getRandom():
    number = randrange(1,1001)
    return number


def getGuess():
    guess=int(input("What's your guess: "))
    return guess

def evaluateGuess(number, guess):
    state=0
    if guess > number:
        print("too big bro #pause")

    elif guess < number:
        print("keep going")

    else:
        print("Yes Lawd you did that")
        state = 1
        
def play():
    number=getRandom()
    score=10
    for i in range (0,11):
        guess=getGuess()
        state = evaluateGuess(number, guess)
        if state==1:
            break
        score = score - 1
    return score

def game():
    choice='y'
    scores=[]
    while choice=='y':
        score=play()
        print ("You score was",score)
        scores.append(score)
        choice = input("Don't be weak play again bro:")
        choice.lower()
                    
    return scores

def getAverageScore(scores):
    total=0
    for item in scores:
        total += item
    average = total/len(scores)
    return average

def printAverage(average, name):
    print (name,", You average score is", average)
    
def main():
    intro() 
    name=getName()
    scores=game()
    average=GetAverageScore(scores)
    printAverage(average,name)

main()

    
