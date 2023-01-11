#!/usr/bin/python3

a = ["You're", "being", "a", "little", "bitch"]
"""for i in range(len(a)):
    print(i,a[i])
"""
for index, value in enumerate(a, start=2):
    print(index, value)