# Python test file for both school and personal project(s)

#!/usr/bin/python3

person = input("Enter Nationality: ")
if person == "Russian" or person == "russian":
    print("Zdrastvuyte! Вы предпочитаете говорить на русском языке?")
elif person == "French" or person == "french":
    print("Bonjour! Préférez-vous parler français?")
else:
    print("You are neither French nor Russian.")
    print("Let us converse in English. Hello!")

print("\n")
