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

guess(10)