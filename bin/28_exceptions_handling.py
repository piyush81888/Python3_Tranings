"""
Exceptions Handling
"""

# print("WITHOUT Handling Exceptions")
# print("-"*20)
# # -------------
#
# a = 10
# b = 0
# c = a/b # PROGRAM WILL TERMINATE HERE ABRUPTLY
# print("Value of c:", c)
#
# print("#"*40, end="\n\n")
# ##########################

print("Handling Exceptions using 'try-except'")
print("-"*20)
# -------------

try:
    pass
    # - keep code inside this block
    # - If any error in this block then program will NOT terminate,
    #       instead it will send it to except block
    # - If no error then skip except block
except:
    pass
    # Here, we will write code to take action if some error occurred in try


try:
    a = 10
    b = 0
    c = a/b # Program will not terminate here, instead control will be passed to except block
    print("Value of c:", c)
except:
    print("Reached except block")
    print("Some Error in try block")
    # exit()

print("#"*40, end="\n\n")
##########################

# About 'Exception' classes
# -------------
# - If we want to handle exception using try-except,
#   then We need to have class for each exception type
#
# - if we don't have class then we can't handle using 'try-except',
#   if we can't handle using 'try-except' then program will terminate
#   it is equillent to not handling
#
# - Few excepion classes are present in builtins
#
# - In above try-except block, any builtin type error comes
#   then 'default-except' will be able to handle
#
# - for any other type of error, we need to write class
##########################

print("Handling Exceptions using 'try-except with class names'")
print("-"*20)
# -------------


try:
    D = {}
    print("Value for key 'A' is:", D["A"]) # KEY NOT PRESENT SO ERROR
    a = 10
    b = 0
    c = a/b
    print("Value of c:", c)
except ZeroDivisionError: # This is 1-way to specify class name
    print("Reached ZDE except")
except NameError as ne: # This is 2-way to specify class name, where we are storing error class object
    print("Reached NE except block and value of 'ne; is:", ne)
except Exception as e:
    print("Some other type of error occurred and details:", type(e))

# class 'Exception' is super class for all exception classes
# so, 'Exception' can handle any type of error

print("#"*40, end="\n\n")
##########################

print("Handling Exceptions using 'try-except-else'")
print("-"*20)
# -------------

try:
    print("Reached try block")
    print("Opening file")
    my_file_handle = open(r"D/asdsa/wewrw.txt", "w")
    print("File open success")
except Exception as e:
    print("Reached except block")
    print("Not able to open file and Reason:", e)
else:
    print("Reached 'else' block")
    my_file_handle.write("Hi")
    my_file_handle.write("Hello")
    my_file_handle.close()

# If try success then 'else' block will execute, and it will skip 'except' block
# If try failed then 'except' block will execute, and it will skip 'else' block

print("#"*40, end="\n\n")
##########################

print("Handling Exceptions using 'try-except-else-finally'")
print("-"*20)
# -------------

try:
    print("Reached try block")
    print("Opening file")
    my_file_handle = open(r"D/asdsa/wewrw.txt", "w")
    print("File open success")
except Exception as e:
    print("Reached except block")
    print("Not able to open file and Reason:", e)
else:
    print("Reached 'else' block")
    my_file_handle.write("Hi")
    my_file_handle.write("Hello")
finally:
    print("Reached finally block")
    try:
        my_file_handle.close()
        print("File handle closed")
    except Exception as e:
        print("Not able to close file handle and the reason is:", e)


# if try/execpt/else Success/failed, finally will always execute

print("#"*40, end="\n\n")
##########################

print("user defined exception class example - 1")
print("-"*20)
# -------------

# Mandatory Step: it should be sub-class of 'Exception' class


class MyError(Exception):
    pass

try:
    x = 10
    if x == 10:
        raise MyError
    if x > 10:
        raise MyError
    if x < 10:
        raise MyError
except MyError:
    print("Reached MyError except block")


print("#"*40, end="\n\n")
##########################

print("user defined exception class example - 2")
print("-"*20)
# -------------

# Requirement: pass some message while throwing exception


class MyError(Exception):
    def __init__(self, msg):
        self.error_message = msg

try:
    x = 10
    if x == 10:
        raise MyError("Here value of x is 10, so raising MyError")
    if x > 10:
        raise MyError("Here value of x is gt 10, so raising MyError")
    if x < 10:
        raise MyError("Here value of x is lt 10, so raising MyError")
except MyError as me:
    print("Reached MyError except block and Details:", me.error_message)


print("#"*40, end="\n\n")
##########################