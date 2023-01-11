#!/usr/bin/python3

passwordFile = open('SecretPassFile.txt')
secretPassW = passwordFile.read()
print('Enter password: ')
typedPassW = input()
if typedPassW == secretPassW:
    print('Welcome')
    if typedPassW == '12345':
        print('Only an idiot would have such a password')
else:
    print('Access Denied!')