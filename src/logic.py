"""Core logic for Save the Watermelon."""

import random
from src.words import WORD_LIST

MAX_SLICES = 6

def select_secret_word():
    return random.choice(WORD_LIST)

def display_word(secret, guessed):
    return " ".join([letter if letter in guessed else "_" for letter in secret])

def play_game():
    secret = select_secret_word()
    guessed = set()
    slices = MAX_SLICES

    print("🍉 Welcome to Save the Watermelon!")
    print("Guess the word before the watermelon gets sliced!")

    while slices > 0:
        print("\nWord:", display_word(secret, guessed))
        print(f"Slices left: {slices}")
        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter (a-z).")
            continue

        if guess in guessed:
            print("You already guessed that letter!")
            continue

        guessed.add(guess)

        if guess in secret:
            print("Nice guess!")
        else:
            slices -= 1
            print("Wrong! The watermelon got a slice...")

        if all(letter in guessed for letter in secret):
            print(f"\n🥳 You saved the watermelon! The word was '{secret}'.")
            break
    else:
        print(f"\n☠️ The melon was sliced! The word was '{secret}'.")
