'''
""" Mad Libs Generator
----------------------------------------
"""
#Loop back to this point once code finishes
loop = 1
while (loop < 10):
# All the questions that the program asks the user
    noun = input("Choose a noun: ")
    p_noun = input("Choose a plural noun: ")
    noun2 = input("Choose a noun: ")
    place = input("Name a place: ")
    adjective = input("Choose an adjective (Describing word): ")
    noun3 = input("Choose a noun: ")
# Displays the story based on the users input
    print ("------------------------------------------")
    print ("Be kind to your",noun,"- footed", p_noun)
    print ("For a duck may be somebody's", noun2,",")
    print ("Be kind to your",p_noun,"in",place)
    print ("Where the weather is always",adjective,".")
    print ()
    print ("You may think that is this the",noun3,",")
    print ("Well it is.")
    print ("------------------------------------------")
# Loop back to "loop = 1"
    loop = loop + 1  
'''








'''
""" Number Guessing Game
----------------------------------------
"""
import random
attempts_list = []
def show_score():
    if len(attempts_list) <= 0:
        print("There is currently no high score, it's yours for the taking!")
    else:
        print("The current high score is {} attempts".format(min(attempts_list)))
def start_game():
    random_number = int(random.randint(1, 10))
    print("Hello traveler! Welcome to the game of guesses!")
    player_name = input("What is your name? ")
    wanna_play = input("Hi, {}, would you like to play the guessing game? (Enter Yes/No) ".format(player_name))
    #Where the show_score function USED to be
    attempts = 0
    show_score()
    while wanna_play.lower() == "yes":
        try:
            guess = input("Pick a number between 1 and 10 ")
            if int(guess) < 1 or int(guess) > 10:
                raise ValueError("Please guess a number within the given range")
            if int(guess) == random_number:
                print("Nice! You got it!")
                attempts += 1
                attempts_list.append(attempts)
                print("It took you {} attempts".format(attempts))
                play_again = input("Would you like to play again? (Enter Yes/No) ")
                attempts = 0
                show_score()
                random_number = int(random.randint(1, 10))
                if play_again.lower() == "no":
                    print("That's cool, have a good one!")
                    break
            elif int(guess) > random_number:
                print("It's lower")
                attempts += 1
            elif int(guess) < random_number:
                print("It's higher")
                attempts += 1
        except ValueError as err:
            print("Oh no!, that is not a valid value. Try again...")
            print("({})".format(err))
    else:
        print("That's cool, have a good one!")
if __name__ == '__main__':
    start_game()
'''




'''
def add(a,b):
    c=a+b
    return c
a=int(input(""))
b=int(input(""))

print(add(a,b))

def sub(a,b):
    c=a-b
    return c
print(sub(a,b))

'''


''' HANGMAN

import random
import time

print("\nWelcome to Hangman game by Bazgha\n")
name=input("Enter your name: ")
print("Hello "+ name+"! Best of Luck!")
time.sleep(2)
print("The game is about to start!\n Let's play Hangman!")
time.sleep(3)

def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess=['ashok','meenakshi','gaurav','parjaiji','kaka','kaki','ladli','ladla','saurav']
    word=random.choice(words_to_guess)
    length=len(word)
    count=0
    display='_'*length
    already_guessed=[]
    play_game=""

def play_loop():
    global play_game
    play_game=input("Do you want to play again? y=yes,n=No\n")
    while play_game not in["y","n","Y","N"]:
        play_game=input("Do you want to play again? y=Yes,n=No\n")
    if play_game=='y':
        main()
    elif play_game=='n':
        print("Thanks for playing! We except you back again!")
        time.sleep(3)
        exit()
        
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("This is the Hangman Word: "+ display +"\nEnter your guess: ")
    guess = guess.strip()
    if len(guess.strip())==0 or len(guess.strip())>=2 or guess<="9":
        print("Invalid Input,Try a letter\n")
        hangman()
        
    elif guess in word:
        already_guessed.extend([guess])
        index=word.find(guess)
        word=word[:index]+'_'+word[index+1:]
        display=display[:index]+guess+display[index+1:]
        print(display+"\n")
        
    elif guess in already_guessed:
        print("Try another letter.\n")
        
    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")

        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:",already_guessed,word)
            play_loop()

    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        play_loop()

    elif count != limit:
        hangman()


main()


hangman()

'''

''' Roll the dice

import random 
while True:     
     print(" 1. roll the dice \n 2. exit ")    
     user = int(input("what you want to do\n"))     
     if user==1:         
        number = random.randint(1,6)         
        print(number)     
     else:         
        break
 '''   


''' Dice Stimulator

import random

x=random.randint(1,6)
if x==1:
    print(" --------")
    print("|        |")
    print("|    O   |")
    print("|        |")
    print(" --------")
    
elif x==2:
    print(" --------")
    print("|        |")
    print("| O    O |")
    print("|        |")
    print(" --------")
    
elif x==3:
    print(" --------")
    print("|    O   |")
    print("|    O   |")
    print("|    O   |")
    print(" --------")

elif x==4:
    print(" --------")
    print("| O    O |")
    print("|        |")
    print("| O    O |")
    print(" --------")
    
elif x==5:
    print(" --------")
    print("| O    O |")
    print("|    O   |")
    print("| O    O |")
    print(" --------")

else:
    print(" --------")
    print("| O    O |")
    print("| O    O |")
    print("| O    O |")
    print(" --------")

'''

#Guess number

'''
import random
def guess(x):
    random_number=random.randint(1,x)
    
    guess=0
    while guess!=random_number:
        guess=int(input(f'Guess a number betweeen 1 and {x}: '))
        if guess<random_number:
            print('Too LOw!') 
         
        elif guess>random_number:
            print('Too High!')
            
    print('Correct Guess :)')

x=int(input())    
guess(x)
'''



#guess the number user

'''
import random

def computer_guess(x):
    low=1
    high=x
    feedback=''
    while feedback!='c':
        if low!=high:
            guess=random.randint(low,high)
        else:
            guess=low
        feedback=input(f'Is {guess} too high (H), too low (L), or correct (c)??').lower()
        if feedback=='h':
            high=guess-1
        elif feedback=='l':
            low=guess+1
            
    print('Computer guessed correctly')




x=int(input())    
computer_guess(x)
'''










