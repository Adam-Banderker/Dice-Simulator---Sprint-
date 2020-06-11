{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to our Dice Rolling Simulator!\n",
      "\n",
      "There will be 9 rounds, 2 players and only 1 winner, GoodLuck!\n",
      "\n"
     ]
    }
   ],
   "source": [
    "import random #imports the random module which contains random numbers\n",
    "import time # this module imports time in my code as i want the code to pause at certain stages before execution\n",
    "\n",
    "\"\"\"introduction Screen to my users\"\"\"\n",
    "print('Welcome to our Dice Rolling Simulator!\\n') \n",
    "time.sleep(1) # this line executes the pause before the next line. We have a 1sec sleep method\n",
    "print (\"There will be 9 rounds, 2 players and only 1 winner, GoodLuck!\\n\") # prints out what the users can expect from this game\n",
    "\n",
    "\"\"\"Random Dice generator\"\"\"\n",
    "def dice_roll(): # defined a roll dice function\n",
    "    diceRoll = random.randint(1, 6) # the dice generate random numbers between 1 - 6 and it is stored a variable\n",
    "    return diceRoll #if the function is called, the value will be return to display\n",
    "\n",
    "\"\"\"The beginning of the game\"\"\"\n",
    "def main(): # deifined the main function that calls the game features\n",
    "    player1 = 0 #player 1 starts off with a score of 0\n",
    "    player1wins = 0 # player 1 wins states the number of rounds won so he/she starts off with 0\n",
    "    player2 = 0 #player 2 starts off with a score of 0\n",
    "    player2wins = 0 # player 2 wins states the number of rounds won so he/she starts off with 0\n",
    "    rounds = 1 # rounds starts off on 1\n",
    "    \n",
    "    play_game = input('Are you ready to roll the dice? Enter Yes or No.\\n').lower() #input for the user is asked and stored in a variable\n",
    "    \n",
    "    \n",
    "    if play_game == \"yes\": #if input is \"yes\" the game will continue\n",
    "            print(\"Lets begin!\\n\")\n",
    "            name1 = input(\"Player 1, what is your name?\\n\") #input to ask for the players name is stored a variable\n",
    "            name2 = input(\"Player 2, what is your name?\\n\")\n",
    "    \n",
    "            while rounds != 10: # a while loop that loops through this game until 9 rounds. THe game will end after the 9th round\n",
    "                play_round = input('Players, are you READY to roll the dice? Enter Yes or No.\\n').lower() #input for the user is asked and stored in a variable\n",
    "\n",
    "                if play_round == \"yes\": # if input of the user is \"yes\" the dice will roll\n",
    "                    print(\"Dice is rolling...\\n\")\n",
    "                    time.sleep(1) # this line executes the pause before the next line. We have a 1sec sleep method\n",
    "                    print(\"Round \" + str(rounds))\n",
    "                    time.sleep(2)# this line executes the pause before the next line. We have a 1sec sleep method\n",
    "                    player1 = dice_roll() #the dice_roll function is stored in a variable for player 1 to roll the dice\n",
    "                    player2 = dice_roll() #the dice_roll function is stored in a variable for player 2 to roll the dice\n",
    "                    print(name1, str(player1))\n",
    "                    time.sleep(2)# this line executes the pause before the next line. We have a 1sec sleep method\n",
    "                    print(name2, str(player2))\n",
    "                           \n",
    "                    if player1 == player2: \n",
    "                        print(\"Draw!\\n\") # if scores are the same per round this will be displayed after each round\n",
    "                    elif player1 > player2: \n",
    "                        player1wins = player1wins + 1\n",
    "                        print(name1, \"wins\\n\") # if player1 score more than player 2, this will be displayed after each round\n",
    "                    else: \n",
    "                        player2wins = player2wins + 1\n",
    "                        print(name2,\"wins\\n\") # if player2 score more than player 1, this will be displayed after each round\n",
    " \n",
    "                    rounds += 1 #after each round, the rounds are added by 1 uptill 9\n",
    "                else:\n",
    "                    print(\"The game has ended\") # this will be printed if the user enter no and then the game will end\n",
    "                    break\n",
    "            \"\"\"this adds up all results per round to see who won the game\"\"\"        \n",
    "            if player1wins == player2wins:  \n",
    "                print(\"Draw!\")\n",
    "            elif player1wins > player2wins:\n",
    "                print(\"WELDONE!\", name1 ,\" - Rounds Won:\" , str(player1wins))\n",
    "            else:\n",
    "                print(\"WELDONE!\", name2 , \" - Rounds Won:\" ,str(player2wins))\n",
    "                \n",
    "    else:\n",
    "        print(\"The game has ended!\") # if the user answer anything but yes, the program will end\n",
    "            \n",
    " \n",
    "\n",
    " \n",
    "main() # calling of the function"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
