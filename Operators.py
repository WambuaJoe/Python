# Operator types in Python programming

#!/usr/bin/python3

"""
Lambda() function
- small, anonymous (throw-away) function(s) that can take any number of arguments but
  only one expression
- syntax is
    lambda x, y, z: x + y + z
    - arguments: comma separated list of arguments
    - expression: arithmetic expression using the arguments
- these function can be passed as arguments to a function or assigned to a variable
- power of a lambda function is best shown when used as an anonymous function inside another function
"""

"""
a = lambda x, y: x - y
print(a(5, 7))
"""
"""
def newfunc(k):
    return lambda a: a - (a + k)
mathops = newfunc(2)
print(mathops(7))
"""

"""
Map() function
- often used to apply a function to each element of an iterable in a concise and efficient way.
- applies a specified function to each element of an iterable sequence
- returns new iterator with the transformed elements
- syntax:
    r = map(func, seq)
    - func: name of the function
    - seq: iterable sequence (list, string, tuple etc)
    - returns: new iterator with transformed elements
- when working with more than one sequence, map function will stop when the shorter sequence has been consumed
- can be applied to more than one list, the lists don't have to be the same length
- 
"""
"""
def newFunct(a):
    return a * 3
numbers = [1, 2, 3, 4]
triples = map(newFunct, numbers)
print(list(triples))

nums = [1,2, 3, 4]
trips = map(lambda x: x * 3, nums)
print(list(trips))
"""

"""
Filter() Function
- returns a sequence where items are filtered through a  function to test if the item is accepted or not
- includes only the items from input iterables for which the function returns 'True'
- syntax is:
    filter(function, iterable/sequence)
    - function: tests if each element of the sequence is true or not
    - iterable: sequence to be filtered
    - return: filtered Python object(s) 
"""
print('Legal driving age in the US of A')
u_age = [12, 15, 22, 21, 17, 19, 18, 14]
drive_legal = filter(lambda x: x >= 16, u_age)
print(list(drive_legal), '\n')

print('Legal drinking age in Kenya')
k_age = [16, 11, 19, 17, 14, 18, 21, 20]
def calcAge(x):
    if x >= 18:
        return True
    else:
        return False

drink_legal = filter(calcAge, k_age)
print(list(drink_legal))
