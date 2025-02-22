"""
Functions with arguments:

Here,
Case-2: How to pass values to variables present inside the function

3-ways we can pass values to variables present inside the function

1-way: we can pass either only value or arg_name=value format
    CALLED, positional or keyword arguments
2-way: Strictly we can pass only value
    CALLED, only positional arguments
3-way: Strictly we can pass only in arg_name=value format
    CALLED, only keyword arguments
"""

print("""
1-way: we can pass either only value or arg_name=value format
    CALLED, positional or keyword arguments
""")
print("-"*20)
# -------------


def employee(name, company):
    print("Employee Name:", name)
    print("Company:", company)
    return {"name": name, "company": company}


# WE CAN PASS ONLY VALUES
received_value = employee("emp-1", "comp-1")
print("received_value:", received_value)

# WE CAN PASS IN ARG=VALUE format
received_value = employee(name="emp-1", company="comp-1")
print("received_value:", received_value)

print("#"*40, end="\n\n")
##########################

print("""
2-way: Strictly we can pass only value
    CALLED, only positional arguments
""")
print("-"*20)
# -------------


# / -> it is just syntax tp tell it only positional argument
# / -> not counted as argument
# / -> we are not passing any values
def employee(name, company, /):
    print("Employee Name:", name)
    print("Company:", company)
    return {"name": name, "company": company}


# WE CAN PASS ONLY VALUES
received_value = employee("emp-1", "comp-1")
print("received_value:", received_value)

# THIS WILL NOT WORK
# WE CAN PASS IN ARG=VALUE format
# received_value = employee(name="emp-1", company="comp-1")
# print("received_value:", received_value)

print("#"*40, end="\n\n")
##########################


print("""
3-way: Strictly we can pass only in arg_name=value format
    CALLED, only keyword arguments
""")
print("-"*20)
# -------------

# * -> it is just syntax to tell it is only keyword argument
# * -> not counted as argument
# * -> we are not passing any values


def employee(*, name, company):
    print("Employee Name:", name)
    print("Company:", company)
    return {"name": name, "company": company}


# THIS WILL NOT WORK
# WE CAN PASS ONLY VALUES
# received_value = employee("emp-1", "comp-1")
# print("received_value:", received_value)

# WE CAN PASS IN ARG=VALUE format
received_value = employee(name="emp-1", company="comp-1")
print("received_value:", received_value)

print("#"*40, end="\n\n")
##########################
