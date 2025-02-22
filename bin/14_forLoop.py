"""
for-loop: Iterate any collection like str,list, tuple etc
"""

print("Iterate String")
print("-"*20)
# -------------

my_string = "Python"
print("my_string:", my_string, end="\n\n")

for i in my_string:
    print("Each char", i)


print("#"*40, end="\n\n")
##########################

print("Iterate list/tuple/set etc any other collections")
print("-"*20)
# -------------

my_list = [100, "Python", (100, 200), {"A":10, "B":20}]
print("my_list:", my_list, end="\n\n")

for i in my_list:
    print("Each Value:", i)

print("#"*40, end="\n\n")
##########################

print("Iterate dictionary")
print("-"*20)
# -------------

my_dictionary = {"duration": 5, "course": "python", "mode": "online"}
print("my_dictionary:", my_dictionary, end="\n\n")

for i in my_dictionary: # Iterate KEY, so i will be key
    print("Key:", i)
    print("Value:", my_dictionary[i])

print("#"*40, end="\n\n")
##########################

# 2 Options:
# -------------
# Option-1: 'break-statement' : We can end for-loop whenever we want
# Option-2: 'continue-statement': We can skip current iteration,
#           and we can send it for next iteration whenever we want
##########################

print("# Option-1: 'break-statement' : We can end for-loop whenever we want")
print("-"*20)
# -------------

my_courses = ["C++", "Java-1", "Perl", "Java-2", "Python"]
print("my_courses:", my_courses, end="\n\n")

# Requirement: Check are there any value starting with Java
for each_course in my_courses:
    if each_course.startswith("Java"):
        print("Course Found")
        break

print("#"*40, end="\n\n")
##########################

print("""
# Option-2: 'continue-statement': We can skip current iteration,
#           and we can send it for next iteration whenever we want
""")
print("-"*20)
# -------------

my_courses = ["C++", "Java-1", "Perl", "Java-2", "Python"]
print("my_courses:", my_courses, end="\n\n")

for each_course in my_courses:
    # Below code is applicable only for java course
    # Other than Java courses are not required
    # so, we can goto next iteration
    if not each_course.startswith("Java"):
        continue # Send it to next iteration
    print("This Java course name is:", each_course)
    print("This Java course duration is 5 days")
    print("This Java course mode is Online", end="\n\n")

print("#"*40, end="\n\n")
##########################