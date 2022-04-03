import os
import re
from tkinter import *
def findIndex(l, g):
    x = []
    for i in range(len(l)):
        if l[i] == g:
            x.append(i)
    return x
inp = input('Input word: ')
os.system('cls' if os.name == 'nt' else 'clear')
hangman = ['', '', '', ' ________', ' ________ \n  |     |', ' ________ \n  |     | \n  |     o', ' ________ \n  |     | \n  |     o \n  |   --|-- ', ' ________ \n  |     | \n  |     o \n  |   --|-- \n  |     |', ' ________ \n  |     | \n  |     o \n  |   --|-- \n  |     | \n  |    / \ \n you died GAME OVER']
word = []
guessed = []
guesses = 0
guess = ''
for i in inp:
    word.append('_')
def printman(x):
    print(hangman[int(x)])
    for i in range(len(word)):
        print(word[i], end=' ')
    if len(guessed):
        print('\n\nAlready guessed characters: ')
        guessed.sort()
        for i in guessed:
            print(i, end=' ')
while guesses != 8:
    printman(guesses)
    guess = input('\n\nGuess a character (Single alphabetical characters only): ')
    while not re.match('^[a-z]$', guess) or guess in guessed:
        guess = input('\nPlease try again. Guess a character (Single alphabetical characters only. No duplicates): ')
    if guess in inp:
        guesses -= 1
        for a in findIndex(inp, guess):
            word[a] = inp[a]
    guesses += 1
    if guess not in guessed:
        guessed.append(guess)
    if '_' not in word:
        printman(guesses)
        print('\nYou won :D')
        window = Tk()
        window.title("Victory")
        window.geometry('2736x1834')
        lbl = Label(window, text="You Won!", font=("Arial Bold", 100))
        lbl.grid(column=0, row=0)
        window.mainloop()
        exit()
if guesses == 8:
    print(hangman[8])
    for i in range(len(word)):
        print(word[i], end=' ')
    print('\nThe correct word was:', inp)