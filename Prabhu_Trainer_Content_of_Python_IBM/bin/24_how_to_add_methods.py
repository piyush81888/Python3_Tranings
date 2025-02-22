"""
How to add methods?

In this section,
1. Class methods
2. Instance methods
"""

"""
Requirement:
1. add method for storing employee_name
2. add method for getting employee_name
3. add method for checking employee_name_startswith
4. add method for storing company_name
5. add method for getting company_name
6. add method for compute average salary
"""

print("Create class")
print("-"*20)
# -------------


class Employee:
    # 1. add method for storing employee_name
    def store_employee_name(self, en):
        self.name = en

    # 2. add method for getting employee_name
    def get_employee_name(self):
        return self.name

    # 3. add method for checking employee_name_startswith
    def employee_name_startswith(self, prefix):
        if self.name.startswith(prefix):
            return True
        else:
            return False

    # 4. add method for storing company_name
    @classmethod
    def store_company_name(cls, cn):
        cls.company_name = cn

    # 5. add method for getting company_name
    @classmethod
    def get_company_name(cls):
        return cls.company_name

    # 6. add method for compute average salary
    @staticmethod
    def compute_avg_salary(sal1, sal2):
        return (sal1 + sal2) / 2


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

e1.store_employee_name("emp-1")
# Internally "e1" will passed to self
e2.store_employee_name("emp-2")
# Internally "e2" will passed to self
Employee.store_company_name("XYZ Company")
# Internally "Employee" will go to 'cls'

# - class method can be accessed using INSTANCE OBJECTS or CLASS OBJECTS
#
# - @classmethod, eventhough if we call class method using instance objects
#   like e1.store_company_name("XYZ Company")
#   Internally e1 will NOT pass to 'cls', @classmethod will take care of
#   passing CLASS OBJECT 'Employee' to 'cls'

print("#"*40, end="\n\n")
##########################

print("DATA present inside each objects")
print("-"*20)
# -------------

print("DATA present in class object 'Employee':", Employee.get_company_name())
print("DATA present in instance object 'e1':", e1.get_employee_name())
print("DATA present in instance object 'e2':", e2.get_employee_name(), end="\n\n")

print("Employee name startswith('emp'):", e1.employee_name_startswith("emp"))

s1 = 20000
s2 = 30000
avg_salary = Employee.compute_avg_salary(s1, s2)
print(avg_salary )

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


# INSTANCE METHODS
# ------------
# We are planning to store in INSTANCE OBJECT
# SO, INSTANCE OBJECT REQUIRED INSIDE METHOD
# 1. add method for storing employee_name
# 2. add method for getting employee_name

# Here, we need to pull employee name from object e1 or e2
# SO, INSTANCE OBJECT REQUIRED INSIDE METHOD
# 3. add method for checking employee_name_startswith


# CLASS METHODS
# ------------
# We are planning to store in CLASS OBJECT
# # SO, CLASS OBJECT REQUIRED INSIDE METHOD
# 4. add method for storing company_name
# 5. add method for getting company_name

# STATIC METHODS
# ------------
# Requirement: If we pass 2 numbers,
# it should take average and return
# NO OBJECT REQUIRED (INSTANCE OR CLASS OBJECT are not required)
# 6. add method for compute average salary




