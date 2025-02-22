"""
2 Cases:
Case-1: How to access values outside the function
Case-2: How to pass values to variables present inside the function

In this section,
Case-1: How to access values outside the function
"""

# -------------
# 2 steps to access values outside the functions
# -------------
# step-1: use 'return-statement' inside function to specify values to send
# step-2: assign function-call to variables to store values returned by function
##########################

print("Function with returning single value")
print("-"*20)
# -------------


def employee():
    name = "emp-1"
    company = "comp-1"
    print("Employee Name:", name)
    print("Company:", company)
    # step-1: use 'return-statement' inside function to specify values to send
    return name


# step-2: assign function-call to variables to store values returned by function
received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
##########################

print("Function with returning multiple values: TUPLE")
print("-"*20)
# -------------


def employee():
    name = "emp-1"
    company = "comp-1"
    print("Employee Name:", name)
    print("Company:", company)
    # step-1: use 'return-statement' inside function to specify values to send
    return (name, company)


# step-2: assign function-call to variables to store values returned by function
received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
##########################

print("Function with returning multiple values: LIST")
print("-"*20)
# -------------


def employee():
    name = "emp-1"
    company = "comp-1"
    print("Employee Name:", name)
    print("Company:", company)
    # step-1: use 'return-statement' inside function to specify values to send
    return [name, company]


# step-2: assign function-call to variables to store values returned by function
received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
##########################

print("Function with returning multiple values: DICTIONARY")
print("-"*20)
# -------------


def employee():
    name = "emp-1"
    company = "comp-1"
    print("Employee Name:", name)
    print("Company:", company)
    # step-1: use 'return-statement' inside function to specify values to send
    return {"name": name, "company": company}

# step-2: assign function-call to variables to store values returned by function
received_value = employee()
print("received_value:", received_value)

print("#"*40, end="\n\n")
##########################

# -------------
# Scopes
# -------------
# 1. Local Scope : Within function we can access the variables
# 2. Enclosed Scope : Within function and in nested function, we can access the variables
# 3. Global Scope : Outside of function-block, This we can access anywhere in the program
# 4. Builtin Scope:
##########################