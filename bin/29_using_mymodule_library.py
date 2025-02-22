"""
In this program, we are accessing
- variables
- functions
- classes
present in mymodule.py LIBRARY
"""
print("1-WAY: using 'import-statement'")
print("-"*20)
# -------------

import mymodule

print("Course Name:", mymodule.course)

add_result = mymodule.add(10, 20)
print("add_result:", add_result)

e1 = mymodule.Employee()
e1.store_name("emp-1")
print("employee 1 name:", e1.get_name())

print("#"*40, end="\n\n")
##########################

print("2-WAY: using 'from-import-statement'")
print("-"*20)
# -------------

from mymodule import course, add, Employee

print("Course Name:", course)

add_result = add(10, 20)
print("add_result:", add_result)

e1 = Employee()
e1.store_name("emp-1")
print("employee 1 name:", e1.get_name())

print("#"*40, end="\n\n")
##########################

print("SHORT NAME 1-WAY: using 'import-statement'")
print("-"*20)
# -------------

import mymodule as mm

print("Course Name:", mm.course)

add_result = mm.add(10, 20)
print("add_result:", add_result)

e1 = mm.Employee()
e1.store_name("emp-1")
print("employee 1 name:", e1.get_name())

print("#"*40, end="\n\n")
##########################

print("SHORT NAME 2-WAY: using 'from-import-statement'")
print("-"*20)
# -------------

from mymodule import course as c, add as a, Employee as E

print("Course Name:", c)

add_result = a(10, 20)
print("add_result:", add_result)

e1 = E()
e1.store_name("emp-1")
print("employee 1 name:", e1.get_name())

print("#"*40, end="\n\n")
##########################