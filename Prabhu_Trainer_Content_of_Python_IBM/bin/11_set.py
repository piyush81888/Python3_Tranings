"""
- set:
        -- We have option to store multiple values like list of names
        -- We can keep UNIQUE values
        -- NO index to each value
"""

print("set PART-1")
print("Store the values")
print("-"*20)
# -------------

my_set = {10, 10, 10, "Java", "Java", "Perl", "Perl"}
print(my_set)
# OR use class name
my_set = set([10, 10, 10, "Java", "Java", "Perl", "Perl"])
print(my_set)

# If we need index then we can convert to other type
# L = list(my_set)
# OR we can iterate using loops
print("#"*40, end="\n\n")
##########################


print("set PART-2")
print("Methods present in 'set' class")
print("-"*20)
# -------------

print(dir(my_set))
# OR
# print(dir(set))

print("#"*40, end="\n\n")
##########################


print("set PART-3")
print("Trying union, intersection, difference methods")
print("-"*20)
# -------------

java_course_candidates = set(["emp-1", "emp-2", "emp-3", "emp-4"])
python_course_candidates = set(["emp-3", "emp-4", "emp-5", "emp-6"])

print("java_course_candidates:", java_course_candidates)
print("python_course_candidates:", python_course_candidates, end="\n\n")

all_employees = java_course_candidates.union(python_course_candidates)
print("all_employees:", all_employees)

employees_not_in_python = java_course_candidates.difference(python_course_candidates)
print("employees_not_in_python:", employees_not_in_python)

employees_present_in_both = java_course_candidates.intersection(python_course_candidates)
print("employees_present_in_both:", employees_present_in_both)

print("#"*40, end="\n\n")
##########################

print("set PART-4")
print("ADD/REMOVE/UPDATE")
print("-"*20)
# -------------

java_course_candidates = {"emp-1", "emp-2", "emp-3", "emp-4"}
print("java_course_candidates:", java_course_candidates)

# ADD
java_course_candidates.add("emp-5")
print("java_course_candidates after adding 'emp-5':", java_course_candidates)

# REMOVE
java_course_candidates.remove("emp-1")
print("java_course_candidates after removing 'emp-1':", java_course_candidates)

java_course_candidates.pop()
print("java_course_candidates after pop():", java_course_candidates)

# UPDATE
another_set = {"emp-6", "emp-7", "emp-8"}
print("another_set:", another_set, end="\n\n")
java_course_candidates.update(another_set)
print("java_course_candidates after updating 'another_set':", java_course_candidates)

print("#"*40, end="\n\n")
##########################
