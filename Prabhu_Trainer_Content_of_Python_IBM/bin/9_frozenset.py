"""
- Frozenset:
        -- We have option to store multiple values like list of names
        -- We can keep UNIQUE values
        -- NO index to each value
"""

print("Frozenset PART-1")
print("Store the values")
print("-"*20)
# -------------

my_fs = frozenset([10, 10, 10, "Java", "Java", "Perl", "Perl"])
print(my_fs)

# If we need index then we can convert to other type
# L = list(my_fs)
# OR we can iterate using loops
print("#"*40, end="\n\n")
##########################


print("Frozenset PART-2")
print("Methods present in 'frozenset' class")
print("-"*20)
# -------------

print(dir(my_fs))
# OR
# print(dir(frozenset))

print("#"*40, end="\n\n")
##########################


print("Frozenset PART-3")
print("Trying union, intersection, difference methods")
print("-"*20)
# -------------

java_course_candidates = frozenset(["emp-1", "emp-2", "emp-3", "emp-4"])
python_course_candidates = frozenset(["emp-3", "emp-4", "emp-5", "emp-6"])

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
