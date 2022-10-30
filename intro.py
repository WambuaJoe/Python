# Introduction to Python programming language

#global variables in Python
'''
mandevu = "sick to the core"
def theWord():
    global mandevu
    mandevu = "an incorrigible piece of shit"

theWord()

print("You are " + mandevu)
'''

#type conversions
longNum = [123, 4.56, 789j]
a, b, c = longNum

d = float(a)
e = int(b)
f = complex(c)

print(d, type(d))
print(e, type(e))
print(f, type(f))
