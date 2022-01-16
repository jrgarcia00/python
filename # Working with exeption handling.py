# Working with exeption handling 
# An exception is an error that occurs during the execution of code. This error causes the code to raise an exception and if not prepared to handle it will halt the execution of the code.

# Example of an math error
1/0
# Example of a name error
y = a + 2
# Example of a index error
a =[1, 2, 3]
a[10]

# Below is what the structure of a exception will general look like...
# potential code before try catch
try:
    # Code to try to execute
except:
    # Code to execute if there is an exception

# Code that will still execute if there is an exception

# Example
a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a =", a)
except:
    print("There was an error")
# Look at the terminal. You can add a number and potenital get a result- if the math "works".

# Below is what the structure of a specific exception will general look like...
# potential code before try catch
try:
    # code to try to execute
except (ZeroDivisionError, NameError):
    # code to execute if there is an exception of the given types
    
# code that will execute if there is no exception or a one that we are handling

# potential code before try catch
try:
    # code to try to execute
except ZeroDivisionError:
    # code to execute if there is a ZeroDivisionError
except NameError:
    # code to execute if there is a NameError

# code that will execute if there is no exception or a one that we are handling 

# potential code before try catch
try:
    # code to try to execute
except ZeroDivisionError:
    # code to execute if there is a ZeroDivisionError
except NameError:
    # code to execute if there is a NameError
except:
    # code to execute if ther is any exception
      
# code that will execute if there is no exception or a one that we are handling

# Example
a = 1
try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a =", a)
except ZeroDivisionError:
    print(" Thie Number you provided ca't divide 1 becuase it is 0")
except ValueError:
    print("Somthing went wrong")

# Below is what the structure of a else exception will general look like...

# potential code before try catch
try:
    # code to try to execute
except ZeroDivisionError:
    # code to execute if there is a ZeroDivisionError
except NameError:
    # code to execute if there is a NameError
except:
    # code to execute if ther is any exception
else:
    # code to execute if there is no exception
    
# code that will execute if there is no exception or a one that we are handling

# Finally can be added it allows us to always execute something even if there is an exception or not. This is usually used to signify the end of the try except.

# potential code before try catch
try:
    # code to try to execute
except ZeroDivisionError:
    # code to execute if there is a ZeroDivisionError
except NameError:
    # code to execute if there is a NameError
except:
    # code to execute if ther is any exception
else:
    # code to execute if there is no exception
finally:
    # code to execute at the end of the try except no matter what
    
# code that will execute if there is no exception or a one that we are handling

#Example of else and finally
a = 1
try:
    b = int(input("Please eneter a number to divide a"))
    a =  a/b
except ZeroDivisionError:
    print("The number yor provided can't be divide 1 becuase it is 0")
except ValueError:
    print("You did not provide a number")
else:
    print("Success a=", a) 
finally:
    print("Processing Complete")
