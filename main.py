# A game called Rock Paper Scissors
import random

# Stating the rule of the game
print("WELCOME TO ROCK PAPER SCISSORS GAME!")
print("""
      The rule of the game is:
      > Rock beats scissors
      > Scissors beats paper
      > Paper beats rock """)

# Creating the players function to make a choice
def Choose_Option():
    player_choice = input("Choose Rock, Paper or Scissors: ")
    if player_choice in ["Rock", "rock", "r", "R", "ROCK"]:
        player_choice = "r"
    elif player_choice in ["Paper", "paper", "p", "P", "PAPER"]:
        player_choice = "p"
    elif player_choice in ["Scissors", "scissors", "s", "S", "SCISSORS"]:
        player_choice = "s"
    else:
        print("Error... try again!")
        Choose_Option()
    return player_choice

# Creating a function for the computer with the random module
def Computer_Option():
    comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice = "r"
    elif comp_choice == 2:
        comp_choice = "p"
    else:
        comp_choice = "s"
        Computer_Option()
    return comp_choice


while True:
    print("")
    
    player_choice = Choose_Option()
    comp_choice = Computer_Option()
    
    if player_choice == "r":
        if comp_choice == "r":
            print(player_choice)
            print("Player(Rock) : CPU(Rock) ")
            print("It's a tie.")
        
        elif comp_choice == "p":
            print(player_choice)
            print(" Player(Rock) : CPU(Paper) ")
            print("You lose!")
            
        elif comp_choice == "s":
            print(player_choice)
            print("Player(Rock) : CPU(Scissors)")
            print("You win!")

    elif player_choice == "p":
        if comp_choice == "r":
            print(player_choice)
            print("Player(Paper) : CPU(Rock) ")
            print("You win!")
        
        elif comp_choice == "p":
            print(player_choice)
            print("Player(Rock): CPU(Paper) ")
            print("It's a tie!")
            
            
        elif comp_choice == "s":
            print(player_choice)
            print("Player(Paper) : CPU(Scissors) ")
            print("You lose!")

    elif player_choice == "s":
        if comp_choice == "r":
            print(player_choice)
            print("Player(Scissors) : CPU(Rock)") 
            print("You lose!")
        
        elif comp_choice == "p":
            print(player_choice)
            print("Player(Scissors) : CPU(Paper) ")
            print("You win!")
            
        elif comp_choice == "s":
            print(player_choice)
            print("Player(Scissors) : CPU(Scissors)") 
            print("It's a tie!")

   
    
    player_choice = input("Do you want to play again? (y/n)")
    if player_choice in ["Y", "y", "yes", "Yes"]:
        pass
    elif player_choice in ["N", "n", "no", "No"]:
        print("Bye!")
        break
    else:
        break