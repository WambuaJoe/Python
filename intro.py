# Introduction to Python programming language

mandevu = "sick to the core"
def theWord():
    global mandevu
    mandevu = "an incorrigible piece of shit"

theWord()

print("You are " + mandevu)