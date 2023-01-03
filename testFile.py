# file for testing python code for my projects before pushing to my git repo

#!/usr/bin/python3


person = input("Nationality? ")
if person == "Russion" or person == "russian":
    print("Zdrastvuyte! Вы предпочитаете говорить на русском языке?")
elif person == "French" or person == "french":
    print("Bonjour! Préférez-vous parler français?")
else:
    print("You are neither French no Russian.")
    print("Let us converse in English. Hello!")