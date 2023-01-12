#!/usr/bin/python3

name = 'Joe'
password = 'mandevu'

username = input('Enter your username: ')
while username == 'Joe' or username == 'joe':
    usr_input = input('Enter password: ')
    if usr_input != 'mandevu':
        print('Wrong password. Try again')
    elif usr_input == 'mandevu':
        print('Welcome back, Ser Mandevu :)')
        break
    else:
        print('Access denied')
<<<<<<< HEAD:interpreter.py
    
=======
print('\n')
>>>>>>> f439bde847257d7c299cc75bb38fb46f55e90374:passCheck.py
