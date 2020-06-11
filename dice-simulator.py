import random #imports the random module which contains random numbers
import time # this module imports time in my code as i want the code to pause at certain stages before execution

"""introduction Screen to my users"""
print('Welcome to our Dice Rolling Simulator!\n') 
time.sleep(1) # this line executes the pause before the next line. We have a 1sec sleep method
print ("There will be 9 rounds, 2 players and only 1 winner, GoodLuck!\n") # prints out what the users can expect from this game

"""Random Dice generator"""
def dice_roll(): # defined a roll dice function
    diceRoll = random.randint(1, 6) # the dice generate random numbers between 1 - 6 and it is stored a variable
    return diceRoll #if the function is called, the value will be return to display

"""The beginning of the game"""
def main(): # deifined the main function that calls the game features
    player1 = 0 #player 1 starts off with a score of 0
    player1wins = 0 # player 1 wins states the number of rounds won so he/she starts off with 0
    player2 = 0 #player 2 starts off with a score of 0
    player2wins = 0 # player 2 wins states the number of rounds won so he/she starts off with 0
    rounds = 1 # rounds starts off on 1
    
    play_game = input('Are you ready to roll the dice? Enter Yes or No.\n').lower() #input for the user is asked and stored in a variable
    
    
    if play_game == "yes": #if input is "yes" the game will continue
            print("Lets begin!\n")
            name1 = input("Player 1, what is your name?\n") #input to ask for the players name is stored a variable
            name2 = input("Player 2, what is your name?\n")
    
            while rounds != 10: # a while loop that loops through this game until 9 rounds. THe game will end after the 9th round
                play_round = input('Players, are you READY to roll the dice? Enter Yes or No.\n').lower() #input for the user is asked and stored in a variable

                if play_round == "yes": # if input of the user is "yes" the dice will roll
                    print("Dice is rolling...\n")
                    time.sleep(1) # this line executes the pause before the next line. We have a 1sec sleep method
                    print("Round " + str(rounds))
                    time.sleep(2)# this line executes the pause before the next line. We have a 1sec sleep method
                    player1 = dice_roll() #the dice_roll function is stored in a variable for player 1 to roll the dice
                    player2 = dice_roll() #the dice_roll function is stored in a variable for player 2 to roll the dice
                    print(name1, str(player1))
                    time.sleep(2)# this line executes the pause before the next line. We have a 1sec sleep method
                    print(name2, str(player2))
                           
                    if player1 == player2: 
                        print("Draw!\n") # if scores are the same per round this will be displayed after each round
                    elif player1 > player2: 
                        player1wins = player1wins + 1
                        print(name1, "wins\n") # if player1 score more than player 2, this will be displayed after each round
                    else: 
                        player2wins = player2wins + 1
                        print(name2,"wins\n") # if player2 score more than player 1, this will be displayed after each round
 
                    rounds += 1 #after each round, the rounds are added by 1 uptill 9
                else:
                    print("The game has ended") # this will be printed if the user enter no and then the game will end
                    break
            """this adds up all results per round to see who won the game"""        
            if player1wins == player2wins:  
                print("Draw!")
            elif player1wins > player2wins:
                print("WELDONE!", name1 ," - Rounds Won:" , str(player1wins))
            else:
                print("WELDONE!", name2 , " - Rounds Won:" ,str(player2wins))
                
    else:
        print("The game has ended!") # if the user answer anything but yes, the program will end
            
 

 
main() # calling of the function
