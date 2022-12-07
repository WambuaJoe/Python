'''
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(is_even(4))  # prints True
print(is_even(5))  # prints False
print(is_even(6))


# isinstance() - funct used to determine whether objects is of certain type
a = 10
b = 1.2
c = 'noice'

print(isinstance(a, int))
print(isinstance(b, int))
print(isinstance(c, complex))
'''

fruit_list = ["mango", "apple", "cherry", "passion", "orange"]
print(len(fruit_list))
print(type(fruit_list))

car_make = list(("Subaru", "Volvo", "Honda", "Hyundai", "Volkswagen", "Toyota"))
print(car_make)
print(len(car_make))
print(type(car_make))
