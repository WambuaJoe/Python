# Sets in Python programming
#!/usr/bin/python3

'''
nums = 1, 2, 3, 3, 5, 6, 2, 7, 6
unique_nums = set(nums)
print(unique_nums)
'''

'''
- elements are added using the add() method
- elements are removed using the remove() method (random element is removed
- as sets are ordered unlike lists which are indexed)
- 
'''

thisSet = {2, 3, 3, 4, 4, 4,}
newSet = {5, 5, 5, 5}
thisSet.update(newSet)
print(thisSet)

for i in thisSet:
    print(i)

'''
- sets are joined using two methods
- union() method: returns a new set containg all items from both sets
- update() method: inserts all items from one set to another
- intersection_update() method: keeps only the items present in both sets; creates new set
- symmetric_difference_update() method: keep only items no present in both sets; creates new set
'''