#import all the required modules here

import logo
import random
import word_list

print(logo.logo)

# choose a random word from the list
chosen_word = random.choice(word_list.words)
lives = 6

# create a list to store the letters entered by user if the letters are present in the chosen_word
display = []

# fill the display list with '_' to show empty blanks
for i in chosen_word:
    display.append("_")

endGame = False

while not endGame:
    guess = input("Guess a letter:\t")
    if guess in display:
        print("You have already guessed the letter.")
    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        if letter == guess:
            display[i] = guess

    str = ''.join(display)
    print(str)
    if "_" not in display:
        print("You won.")
        endGame = True
    if guess not in chosen_word:
        lives -= 1
        print(
            f"{guess} is not present in the word. \nYou lost a life.\n{lives} guess are left."
        )
        if lives == 0:
            print("You lost.")
            print(f"The word is {chosen_word}")
            endGame = True
    print(logo.stages[lives])
