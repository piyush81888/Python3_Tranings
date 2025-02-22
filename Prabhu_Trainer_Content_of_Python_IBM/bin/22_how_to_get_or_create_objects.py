"""
How to get or obtain objects?
- Answer: Using class

In this section,
1. CLASS OBJECT
2. INSTANCE OBJECTS
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

print("DATA present inside each objects")
print("-"*20)
# -------------

print("DATA present in class object 'Employee':", Employee)
print("DATA present in instance object 'e1':", e1)
print("DATA present in instance object 'e2':", e2)

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

# About 'object' class
# -------------
#
# - Inside 'object' class we have basic methods which is required for each and every class
#   which we develop. like constructor method, initializer method etc
#
# - by default 'object' class is linked to each ande every class
#       - This linking is called INHERITANCE
#
# - by default whatever there in 'object' class, will automatically
#   come each and every class which we create, builtin classes
#
#
# - >>> dir(object)
#
##########################
