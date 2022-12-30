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

# fibonacci sequence

a, b = 0, 1
print(a)
print(b)

for i in range(12):
    fib = a + b
    print(fib)
    a, b = b, fib

print("\n")
nacci_fibo = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]

odd_nums = list(filter(lambda x: x % 2, nacci_fibo))
print("Odd numbers filtered from the fibonacci sequence: ")
print(odd_nums)
print(len(odd_nums))
even_nums = list(filter(lambda x: x % 2 == 0, nacci_fibo))
print("Even numbers filtered from the fibonacci sequence: ")
print(even_nums)
print(len(even_nums))