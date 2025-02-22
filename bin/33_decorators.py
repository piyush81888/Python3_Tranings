"""
Decorators: If we have common functionality that needs to be
added in more than one function then we can keep that common functionality
in separate function and use this in all other functions
"""
print("WITHOUT using Decorators")
print("-"*20)
# -------------


def add(a, b):
    print("Result is:")
    print(a+b)
    print("End of the result")


def sub(a, b):
    print("Result is:")
    print(a-b)
    print("End of the result")


add(10, 20)
sub(10, 20)

# Common functionality here is,
#       - print("Result is:")
#       - print("End of the result")

# How to create function to keep above common functionality?
#   Because those statements are getting repeated in between,
#   not in sequence.

print("#"*40, end="\n\n")
##########################

print("USING Decorators: PARTIAL")
print("-"*20)
# -------------


def my_decorator(my_func): # my_func = sub
    def decorated_function(x,y):
        print("Result is:")
        my_func(x,y) # add(10,20)
        print("End of the result")
    return decorated_function


def add(a,b):
    print(a+b)

nested_function_reference = my_decorator(add)
# nested_function_reference will be holding decorated_function
nested_function_reference(10, 20)

def sub(a,b):
    print(a-b)

nested_function_reference = my_decorator(sub)
# nested_function_reference will be holding decorated_function
nested_function_reference(10, 20)

def mul(a,b):
    print(a*b)

nested_function_reference = my_decorator(mul)
# nested_function_reference will be holding decorated_function
nested_function_reference(10, 20)


print("#"*40, end="\n\n")
##########################

print("USING Decorators: FINAL IMPLEMENTATION")
print("-"*20)
# -------------


def my_decorator(my_func): # my_func = sub
    def decorated_function(x,y):
        print("Result is:")
        my_func(x,y) # add(10,20)
        print("End of the result")
    return decorated_function


@my_decorator
def add(a,b):
    print(a+b)

add(10, 20)

# @my_decorator, will take care of doing below 2 steps
# nested_function_reference = my_decorator(add)
# nested_function_reference(10, 20)
@my_decorator
def sub(a,b):
    print(a-b)

sub(10, 20)

# @my_decorator, will take care of doing below 2 steps
# nested_function_reference = my_decorator(sub)
# nested_function_reference(10, 20)
@my_decorator
def mul(a,b):
    print(a*b)

mul(10, 20)

# @my_decorator, will take care of doing below 2 steps
# nested_function_reference = my_decorator(mul)
# nested_function_reference(10, 20)

print("#"*40, end="\n\n")
##########################