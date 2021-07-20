import random
print ("The Guessing game")
number = random.randint(1,9)
chances = 0
while chances < 5:
    guess = int (input ("Enter your guess :- "))
    if guess ==  number :
        print("CONGRATULATIONS YOU WON!!!")
        break
    elif guess < number :
        print("Your guess was too low")
        break
    else : 
        print("your guess was too high")

    chances +=1
if not chances < 5:
    print("You lose the number is ",number)
