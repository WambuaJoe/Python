# file for testing python code for my projects before pushing to my git repo

#!/usr/bin/python3
# Python function to search for vowels in a sequence of letters
"""
def funct(vars):
    letters = ['a', 'e', 'i', 'o', 'u']
    if vars in letters:
        return True
    else:
        return False


# letter sequence
seq_l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'o', 'p', 'q', 'r', 's', 't']

# employ filter function
funct_filter = filter(funct, seq_l)

# print filtered sequence
print(funct_filter)
for a in funct_filter:
    print(a)
"""


a, b = 0, 1
print(a)
print(b)

for i in range(6):
    fib = a + b
    print(fib)
    a, b = b, fib

strI = str(fib)
print(strI)

lst = list(strI)
lst.append('2')
print(lst)
