# Fuctions in Python
#A function is a reusable block of code which performs operations specified in the function. They let you break down tasks and allow you to reuse your code in different programs.
# First function example: Add 1 to a and store as b
from ast import Mult, arg
from re import A

def add(a):
    b = a + 1
    """
    add 1 to A
    """
    print(a, "if you add one", b)
    return(b)

help(add)
add(1)
add(2)

# Define a function for multiple two numbers
def Mult(a,b):
    c = a * b
    return(c)
    print('This is not printed')

result = Mult(12,2)
print(result)
Mult(2,3)
# using two floats
Mult(10.0, 3.14)
# using two different type of values
Mult(2, "Michael Jackson ")

# Fuction definition 
def square(a):

    # Local varable b
    b = 1
    c = a * a + b
    print(a, "if you square +1", c)
    return(c)

# Initialize Global variable
x = 3
# Make function call and return function a y
y = square(x)
y
# Entering a number as a parameter
square(2)

# Define fuctions, one with return value None and the other w/out return value
def MJ():
    print("Michael Jackson")

def MJ1():
    print('Michael Jackson')
    return(None)

MJ()
MJ1()
# Printing the function after a call reveals a None is the default return statement:
print(MJ())
print(MJ1())

def con(a, b):
    return(a + b)

con("This ", "is")

# a and b calculation block1
a1 = 4
b1 = 5
c1 = a1 + b1 + 2 * a1 * b1 - 1
if(c1 < 0):
    c1 = 0
else:
    c1 = 5
c1

# a and b calculation block2
a2 = 0
b2 = 0
c2 = a2 + b2 + 2 * a2 * b2 - 1
if(c2 < 0):
    c2 = 0
else:
    c2 = 5
c2 

# Make a Fuction from the calculations above
def Equation(a, b):
    c = a + b + 2 * a * b - 1
    if(c < 0):
        c = 0
    else:
        c = 5
    return(c)
Equation(4, 5)
Equation(0, 0)

# Also we can now replace block1 and block2 with this simplification
# New block3
a1 = 4
b1 = 5
c1 = Equation(a1, b1)
c1
# New block4
a2 = 0
b2 = 0
c2 = Equation(a2, b2)
c2

# Examples of pre-defined functions
# Build-in function print()
album_ratings = [10.0, 8.5, 9.5, 7.0, 7.0, 9.5, 9.0, 9.5] 
print(album_ratings)
sum(album_ratings)
len(album_ratings)

# if/else statments and loops in fuctions
def type_of_album(artist, album, year_released):

    print(artist, album, year_released)
    if year_released > 1980:
        return "Modern"
    else:
        return "Oldie"

x = type_of_album("Michael Jackson", "Thriller", 1980)
print(x)

# Priting a list using for loop
def PrintList(the_list):
    for element in the_list:
        print(element)
# Implement the printlist fuction
PrintList(['1', 1, 'the man', "abc"])

# Defult argument values for a custom fuction
def isGoodRating(rating = 4):
    if(rating < 7):
        print("this album sucks it's rating is", rating)
    else:
        print("this album is good it's rating is", rating)
# Testing value w/ defult value and with input
isGoodRating()
isGoodRating(10)

#Global Variables
artist = "Michael Jackson"
def printer1(artist):
    internal_var1 = artist
    print(artist, "is an artist")

printer1(artist)

printer1(internal_var1)
# We get NameError: name 'internal_var1' is not defined b/c all the variables created in the fuction are local variables
#We can make global variables from w/in the fuction
artist = "Michael Jackson"
def printer(artist):
    global internal_var
    internal_var= "Whitney Houston"
    print(artist, "is an artist")

print(artist)
print(internal_var)

# Example of global variable
myFavoriteBand = "AC/DC"

def getBandRating(bandname):
    if bandname == myFavoriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is:", getBandRating("AC/DC"))
print("Deep Purple's rating is:",getBandRating("Deep Purple"))
print("My favorite band is:", myFavoriteBand)

# Delete the variable "myFavoriteBand" to show an example of a local variable
del myFavoriteBand

# Example of local variable
def getBandRating(bandname):
    myFavoriteBand = "AC/DC"
    if bandname == myFavoriteBand:
        return 10.0
    else:
        return 0.0
print("AC/DC's rating is: ", getBandRating("AC/DC"))
print("Deep Purple's rating is: ", getBandRating("Deep Purple"))
print("My favorite band is: ", myFavoriteBand)
# NameError: name 'myFavoriteBand' is not defined b/c we deleted myfavoriteBand

#Example of global variable and local variable w/ the same name 
myFavoriteBand = "AC/DC"
def getBandRating(bandname):
    myFavoriteBand = "Deep Purple"
    if bandname == myFavoriteBand:
        return 10.0
    else:
        return 0.0
print("AC/DC's rating is:", getBandRating("AC/DC"))
print("Deep Purple's rating is:", getBandRating("Deep Purple"))
print("My favorite band is:", myFavoriteBand)

 # All the arguments are 'packed' into args which can be treated like a tuple
def printALL(*args):
    print("No of arguments:", len(args))
    for argument in args:
        print(argument)
# printALL w/ 3 arguments
printALL('Horsefeather','Adonis','Bone')
# printALL w/ 4 arguments
printALL('Sidecar', 'Long Island', 'Mudslide', 'Carriage')

#Packing the arguments into a dictonary
def printDictionary(**args):
    for key in args:
        print(key + " : " + args[key])
printDictionary(Country='Canada',Province='Ontario',City='Toront')

def addItems(list):
    list.append("Three")
    list.append("Four")

myList = ["One","Two"]
addItems(myList)
myList
