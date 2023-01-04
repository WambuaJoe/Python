#!/usr/bin/python3

# string concatenation

name = input("Name: ")
age = input("Age: ")
course = input("Course: ")
date_of_completion = input("Date of Completion: ")

madlibs = (f"I am {name}, a {age} year old currently enrolled in the ALX {course} program. \
It is a challenge course where you really do have to study and work \
on projects to ensure you stay update on the workings of an \"IT guy\" \
I am supposed to finish the progam on {date_of_completion}, and I look forward to the \
mentioned date. ADIOS!")

print(madlibs)
