# introduction to lists in python and how to manipulate them

'''
x = "awesome"

def newfunct():
    global x
    x = "diabolical!"
    print("" + x)

newfunct()
print("That man is fucking " + x)


# Python Type Cpnversion
a, b, c = 1, 2.9, 3j
print(a, type(a))
print(b, type(b))
print(c, type(c))

j = float(a)
k = int(b)
l = complex(a)

print(j, type(j))
print(k, type(k))
print(l, type(l))


# Python Random Module
import random
print(random.randrange(0, 10))


a = "Hello, world!"
print(a[:5])

# strings are arrays in Python


text = """the blood diamonds were sold after the city fell
Never be afraid of the repercussions of your actions, you did the right thing regardless"""

print("act" not in text)
'''



quantity = 4
item = "drum sticks"
price = 400
order = "I'll pay {2} for {0} of those {1}"

print(order.format(quantity, item, price))