# PYTHON CASTING

x = str(3)
y = int(3)
z = float(3)

# GET TYPEOF
print(type(x))
print(type(y))
print(type(z))

# ASSIGN MULTIPLE VARIABLES 
oranges,banana,cherry = "oranges","banana","cherry"
print(oranges)
print(banana)
print(cherry)

# UNPACKING A COLLECTION
fruits = ["apple","banana","oranges"]
x,y,z = fruits
print(x,y,z)

# GLOBAL VARS
# local var 
def myfunc():
    x = "fantastic"

    print("Python is " + x)

myfunc()
print(x) #Gives "apple" which is outside the function

# GLOBAL VAR
def myfunctg():
    global g
    g = "fantastic"
myfunctg()

print("Python is " + g)


#Random Number
import random
print(random.randrange(10,100))

# Multiline Strings
a =""""
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
"""
print(a)


# String Length
print(len(a))

print("Lorem" in a)
print("lorem" not in a)


# Slicing
# return a range of character
print(a[0:9])

# Upper Case
print(a.upper())
print(a.lower())

F-Strings
name = "Velocibyte"
age = 27
print(f"My name is {name} and I am {age} years old.")
