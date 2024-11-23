import sys
# to see which python version we are using
print(sys.version)

# Python is what is called an interpreted language. Compiled languages examine your entire program at compile time, and are able to warn you about a whole class of errors prior to execution. In contrast, Python interprets your script line by line as it executes it. Python will stop executing the entire program when it encounters an error (unless the error is expected and handled by the programmer, a more advanced subject that we'll cover later on in this course).

# data types can be found by using type
type("print")

# floats are real numbers
# changing expression : typecasting
# float(2) will be 2.0
# int(1.1) will be 1 ?
# int("hello") will give error
# True or False is boolean type
type(True) # will give bool
bool(0) #will give false

sys.float_info # will display info about float like what is the max and min

# int('1') will give 1 but int('1 or 2 people') will give error

# 6/2 = 3.0 is float BUT 6//2 is 3 and thus int as // indicate integer division

