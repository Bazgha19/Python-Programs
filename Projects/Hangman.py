# Hangman


import random

from Words import words

name=input("Enter your name: ")

print("Welcome!",name,"in Hangman")

def get_valid_words(words):
    word=random.choice(words)
    while '-' in word or ' ' in word:
        word=random.choice(words)
        
    return word

def hangman():
    word=get_valid_words(words)
    