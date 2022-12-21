# Tuples in python programming
#!/usr/bin/python3

'''
- can be used to assign multiple variables in a compact manner
- parentheses are optional during definitions
-
'''

dimensions = 3, 4, 5
width, height, hypotenuse = dimensions
#print("The triangle's dimensions are {}, {} and {}".format(width, height, hypotenuse))

# Packing and Unpacking Tuples
'''
triangle_dimen = 3, 4, 5
print(triangle_dimen)
width, height, hypotenuse = triangle_dimen
print(width)
print(height)
print(hypotenuse)
'''

# enumerate() function to get both index and value of each element after using a loop

tups = ('a', 'b', 'c', 'd', 'e')
for i, value in enumerate(tups):
    print(i, value)