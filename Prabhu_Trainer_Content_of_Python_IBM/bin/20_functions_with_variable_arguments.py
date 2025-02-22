"""
Functions with variable arguments
1. Functions with variable POSITIONAL arguments
2. Functions with variable KEYWORD arguments
"""

# about print-function
# -------------
print() # We can call with 0 arguments
print(10) # We can call with 1 arguments
print(10, 20, 30, 40, 50)  # We can call with n number of arguments
##########################

print("1. Functions with variable POSITIONAL arguments")
print("-"*20)
# -------------
# *a -> variable positional arguments
def add(*a):
    print("Received all values in TUPLE:", a)


add()
add(10)
add(10, "hello")
add(10, 20, "java", "python")

print("#"*40, end="\n\n")
##########################

print("2. Functions with variable KEYWORD arguments")
print("-"*20)
# -------------


def employee_profile(**a):
    print("Received values in dictionary:", a)


employee_profile()
employee_profile(name="emp-1")
employee_profile(name="emp-2", company="comp-2")
employee_profile(name="emp-3", company="comp-3", manager="xyz")

print("#"*40, end="\n\n")
##########################