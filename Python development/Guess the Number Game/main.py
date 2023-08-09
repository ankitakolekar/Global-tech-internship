import random

lownumber =  int(input("Enter the Lower Limit: "))
upnumber =  int(input("Enter the Upper Limit: "))

guessNumber = random.randrange(lownumber, upnumber)

print("You have 10 chances to Guess the Number. Let's Begin")
print("")

chances = 0

while chances <10:

    userNumber = int(input("Enter Your Guess: "))

    if guessNumber == userNumber :
        print("You Guess it Right.The Number is: ", guessNumber)
        print("Congratulations. You win ! in ", chances + 1, "try")
        print("")

    elif guessNumber < userNumber :
        print("You Guess a Little High. Try a smaller number.")
        print("")

    elif guessNumber > userNumber :
        print("You Guess a Little Low. Try a bigger number.")
        print("")

    chances = chances + 1

if chances>=10:
    print("The number was: ", guessNumber)
    print("You Lose !")
    print("")
