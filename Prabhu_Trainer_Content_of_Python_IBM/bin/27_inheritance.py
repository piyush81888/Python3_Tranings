"""
Inheritance:
1. multilevel inheritance
2. multiple inheritance
"""

print("1. multilevel inheritance")
print("-"*20)
# -------------


# Assume below class is existing class
class Salary:
    def store_salary(self, s):
        self.salary = s
    def get_salary(self):
        return self.salary


# Clients new requirement: Add below functionalities to
#   salary class
# 1. add store_tax method
# 2. add get_tax method
# 3. modify get_salary method to return (salary-tax)
# 4. add get_old_scheme_salary method

# Inheritance: Create new class by extending salary class
class Employee(Salary):
    # 1. add store_tax method
    def store_tax(self, t):
        self.tax = t

    # 2. add get_tax method
    def get_tax(self):
        return self.tax

    # 3. modify get_salary method to return (salary-tax)
    # POLYMORPHISM: We can use same name as super class method
    # Below get_salary method will OVERRIDE super class get_salary method
    def get_salary(self):
        return (self.salary - self.tax)

    # 4. add get_old_scheme_salary method
    def get_old_scheme_salary(self):
        # 1-Way to call super class method
        old_sal = super().get_salary()

        # 2-Way to call super class method
        old_sal = Salary.get_salary(self)
        return old_sal

print("#"*40, end="\n\n")
##########################

print("Create object")
print("-"*20)
# -------------

e1 = Employee()
e1.store_salary(20000)
e1.store_tax(2000)

print("Salary:", e1.get_salary())
print("tax:", e1.get_tax())
print("Old Salary:", e1.get_old_scheme_salary())

print("#"*40, end="\n\n")
##########################

print("1. multilevel inheritance: Method Resolution Order")
print("-"*20)
# -------------

# If we access any method then in below order and in below classes
#   it will search for that method which we are calling
print(Employee.mro())


print("#"*40, end="\n\n")
##########################


print("2. multiple inheritance: Method Resolution Order")
print("-"*20)
# -------------

class A:
    pass

class B:
    pass

class C(A,B):
    pass


# If we access any method then in below order and in below classes
#   it will search for that method which we are calling
print(C.mro())


print("#"*40, end="\n\n")
##########################
