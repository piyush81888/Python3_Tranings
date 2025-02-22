"""
3 Things we are planning here

1) rewrite/override 'object' class method
    - when we create object like e1=Employee()
     then 2 methods will execute
     1) __new__ which will construct the object
     2) __init__ which will initialize the object

     let us override __init__ to initialize each object with employee name

2) declare variable inside class
3) support + operator
"""

print("Create class")
print("-"*20)
# -------------


class Employee:

    company_name = "XYZ Company"
    # This will get store in class object

    def __init__(self, en):
        self.name = en

    def get_employee_name(self):
        return self.name

    @classmethod
    def get_company_name(cls):
        return cls.company_name

print("#"*40, end="\n\n")
##########################

print("Create objects")
print("-"*20)
# -------------

e1 = Employee("emp-1") # __init__
# It will create object and store in 'e1'
e2 = Employee("emp-2")
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

print("DATA present in class object 'Employee':", Employee.get_company_name())
print("DATA present in instance object 'e1':", e1.get_employee_name())
print("DATA present in instance object 'e2':", e2.get_employee_name(), end="\n\n")

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
