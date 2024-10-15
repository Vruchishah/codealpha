import random

name = input("type your name:- ")

print("Good Luck ! ", name)

words = ['build', 'sleep', 'child', 'Chinese',
         'classic', 'develop', 'elite', 'makeup',
         'flight', 'water', 'glass', 'highlight' ,'independence','laboratory','maintenance','minority','policy','restore']

word = random.choice(words)

print("Guess the characters")

guesses = ''
turns = 12

while turns > 0:

    failed = 0

    for char in word:

        if char in guesses:
            print(char, end=" ")

        else:
            print("_")
            failed += 1

    if failed == 0:
        print("You Win the game")
        print("The word is: ", word)
        break

    print()
    guess = input("guess a character:")

    guesses += guess

    if guess not in word:

        turns -= 1
        print("wrong answer")
        print("You have", + turns, 'more guesses')

        if turns == 0:
            print("You Loose !!! word was:- ",word)
