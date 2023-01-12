#!/usr/bin/python3

while True:
    print('Who are you?')
    name = input()
    if name == 'Joe':
        continue
    print(f'Hi {name}, what\'s the password? (Hint: type of fish)')
    password = input()

    if password == 'swordfish':
        break
print('Welcome back Ser')
