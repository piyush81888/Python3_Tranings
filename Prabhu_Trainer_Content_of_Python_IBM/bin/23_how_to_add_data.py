"""
How to store data inside object

In this section,
1. CLASS VARIABLES
2. INSTANCE VARIABLES
"""

print("Create class")
print("-"*20)
# -------------


class Employee:
    pass
# pass -> dummy keyword
# pass -> use this to keep any block empty like if-block, for-block etc

# Even though it is empty class, we can create objects

print("#"*40, end="\n\n")
##########################

print("Create objects")
print("-"*20)
# -------------

e1 = Employee()
# It will create object and store in 'e1'
e2 = Employee()
# It will create object and store in 'e2'

print("#"*40, end="\n\n")
##########################

print("Total 3 objects we have")
print("-"*20)
# -------------

# CLASS OBJECT: 'Employee', In the name of class, automatically one object is getting created
# INSTANCE OBJECTS: e1, e2 which we create

print("#"*40, end="\n\n")
##########################

print("Store data in all 3 objects")
print("-"*20)
# -------------

Employee.company_name = "XYZ Company"
# It will create, new variable 'company_name' inside that object and store the value
e1.name = "emp-1"
# It will create, new variable 'name' inside that object and store the value
e2.name = "emp-2"
# It will create, new variable 'e2' inside that object and store the value

print("#"*40, end="\n\n")
##########################

print("DATA present inside each objects")
print("-"*20)
# -------------

print("DATA present in class object 'Employee':", Employee.company_name)
print("DATA present in instance object 'e1':", e1.name)
print("DATA present in instance object 'e2':", e2.name)

print("#"*40, end="\n\n")
##########################

print("METHODS/VARIABLES present inside each objects")
print("-"*20)
# -------------

print("METHODS/VARIABLES present in class object 'Employee':", dir(Employee), sep="\n", end="\n\n")
print("METHODS/VARIABLES present in instance object 'e1':", dir(e1), sep="\n", end="\n\n")
print("METHODS/VARIABLES present in instance object 'e2':", dir(e2), sep="\n", end="\n\n")

print("#"*40, end="\n\n")
##########################

# About class object 'Employee'
# -------------
# - class object 'Employee' is common space for all instance objects
# - data which is common for all, that data we can keep it in class object
##########################

