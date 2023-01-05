#!/usr/bin/python3

import random

def guess(x):
    random_num = random.randint(1, x)
    guess_num = 0

    while guess_num != random_num:
        guess_num = int(input(f'Enter number between 1 and {x}: '))
        if guess_num < random_num:
            print("Try again. Guess is lower than actual value")
        elif guess_num > random_num:
            print("Try again. Guess is higher than actual value")
        else:
            print(f"Gotcha bitch! Correct value is {random_num}")

def comp_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} high (H), low (L), or correct (C)?? ').lower
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"Nice guess computer, {guess} is correct")

comp_guess(10)