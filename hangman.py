#!/usr/bin/env python3
# Created By: Jack Turcotte
# Date: March 25th, 2025

# Hangman Program in python

import random
import words

word_list = words.wl
starting_lives = 3
word = "hangman"

#Function to check if the guess is valid
def check_valid(word_array,guessed):
    if word_array==guessed:
        return True
    else:
        return False
        
def chose_word():
    return word_list[random.randint(1,len(word_list))-1]

def main():
    print("Welcome to jacks hangman game, please only use lowercase letters")
    
    #Set starting lives
    lives = starting_lives
    word = chose_word()
    word_array = []
    guessed = []

    #Append word to word array
    for i in range(0,len(word)):
        word_array.append(word[i])
        guessed.append("_")
    
    while True:

        #Get user's guess
        print(guessed)
        user_guess = str(input("Guess a letter:"))
        guess_correct = False
        
        #Update guessed word
        for i in range(0,len(word)):
            if user_guess==word_array[i]:
                guessed[i]=user_guess
                guess_correct = True
        
        #If the user guessed wrong
        if not guess_correct:
            lives-=1
            if lives>0:
                print("Oops! you have",lives,"lives left!")
            else:
                print("You lost all of your lives!")
                break
        
        #Check if the user has guessed the right word
        if check_valid(word_array,guessed) == True:
            print("YOU GUESSED THE WORD!")
            break
    
    #Ask the user to try again
    print("The word was ",word)
    prompt = input("Try again? (yes/no)")
    if prompt == "yes":
        main()
    else:
        print("Too bad")
        main()

#Initiate the program
if __name__ == "__main__":
    main()