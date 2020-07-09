import random



def game():
    randomNumber = random.randint(1,10)
    life = 3
    
    print("\nGuess the number between [ 1 - 10 ]    Life:",life)
    while life > 0:
        
        life -= 1
        guess_number = int(input())
        
        if guess_number < randomNumber:
            print("\nToo Low    Life:",life)
            if life == 0:
                print("")
            else:
                print("Try again: ", end="")
            
        elif guess_number > randomNumber:
            print("\nToo High    Life:",life)
            if life == 0:
                print("")
            else:
                print("Try again: ", end="")
            
        else:
            life += 1
            print("\n/////YOU WIN/////    Life:",life)
            break

        
    if life == 0:
        print("/////Game Over/////")
        print("The number was",randomNumber)





while True:
    game()
    reStart = input("\nDo you want to play again? Y/N : ")
    if reStart=="Y" or reStart=="y" or reStart=="YES" or reStart=="yes" or reStart=="Yes":
        game()
    elif reStart=="N" or reStart=="n" or reStart=="NO" or reStart=="no" or reStart=="No":
        break
