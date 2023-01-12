#!/usr/bin/python3

name = 'Joe'
password = 'mandevu'

while name == 'Joe':
    print('Hi, yer bitch :P')
    usr_input = input('Enter password: ')
    if usr_input != 'mandevu':
        print('Wrong password. Try again')
    elif usr_input == 'mandevu':
        print('Welcome back, Ser Mandevu :)')
        break
    else:
        print('Access denied')
print('\n')
