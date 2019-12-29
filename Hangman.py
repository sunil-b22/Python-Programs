import csv
import random
import re


# Method to check the letter
def check(x,guess):
    if x in word:
        print("{} is present {} times in the word".format(x, word.count(x)))
        for i in re.finditer(x, word):
            a = i.start()
            print("at {} position".format(a + 1))
    else:
        print("Wrong guess")
        guess -= 1
        print("{} is not present in the word {} guesses remaining".format(x, guess))
    return guess


# GAME STARTS HERE
# Randomly picks a word from this CSV file
with open("E:\Python Tutorials\Hangman Game\Scrabble Word.csv","r") as file:
    wo = csv.reader(file)
    wor = str((random.choice(list(wo))))
    file.close()
word = wor[2:-2]

guess=15
# print(word)
print("           Welcome to Hangman Game \n          Guess the word in 6 misses\n           (It is UPPER CASE Word)")
print("The word length = {}".format(len(word)))

x = input("Guess a letter: ")

guess = check(x,guess)

while guess != 0:
    y = int(input("Press 1 to guess another letter or 2 to guess the word: "))
    if y == 1:
        x = input("Guess another letter: ")
        guess = check(x,guess)

    elif y == 2:
        x = input("Guess the word")
        if x == word:
            print("You guessed the correct word, the word was {}".format(word))
            exit()
        else:
            guess -= 1
            print("Wrong guess {} guesses remaining".format(guess))

    else:
        print("Wrong input")

print("You lost, the word was {}".format(word))
