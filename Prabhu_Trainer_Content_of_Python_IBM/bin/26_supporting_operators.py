"""
Supporting + operator

In python, for each operator there is name given
Example: for +, __add__
for -, __sub__

So,
If we want to support + then in our class we need to write __add__
"""

print("Create class")
print("-"*20)
# -------------


class Employee:

    def __init__(self, en):
        self.name = en

    def __add__(self, other): # self=e1, other=e2
        concat_result = self.name + other.name
        return concat_result

print("#"*40, end="\n\n")
##########################

print("Create objects")
print("-"*20)
# -------------

e1 = Employee("emp-1")
# It will create object and store in 'e1'
e2 = Employee("emp-2")
# It will create object and store in 'e2'

print("#"*40, end="\n\n")
##########################

print("Adding e1 & e2")
print("-"*20)
# -------------

# Requirement: If we add 2 Emplyee objects then it should concat both names
# "emp-1emp-2"
add_result = e1 + e2 # + calls e1.__add__(e2)
print("add_result:", add_result)

print("#"*40, end="\n\n")
##########################


