#!/usr/bin/python3

# lists in python programming

carModel = list(("Subaru", "Volkswagen", "Toyota", "Nissan", "Hyundai"))
print(carModel)
for i in carModel:
    print(i)

# 'in' keyword to check for presence of an item in the list
'''
if "Hyundai" in carModel:
    print("'Hyundai' is present in the list")
elif
    print("'Hyundai' is not present in the list")
'''

#insert() function - inserts item at specified index without replacing existing value(s)
'''
carModel.insert(3, "Fiat")
print(carModel)
'''

# extend() function - appends elements from another list to the current list
'''
newCarModel = list(("Porsche", "Fiat", "Dodge", "Tesla"))
newCarModel.clear()
print(newCarModel)
'''