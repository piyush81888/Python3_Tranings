"""
while-loop: Execute loop based on condition
"""

print("While loop example")
print("-"*20)
# -------------

x = 0
while x < 10:
    print("Value of x is:", x)
    x = x + 1

print("#"*40, end="\n\n")
##########################

# 2 Options:
# -------------
# Option-1: 'break-statement' : We can end while-loop whenever we want
# Option-2: 'continue-statement': We can skip current iteration,
#           and we can send it for next iteration whenever we want
##########################

print("# Option-1: 'break-statement' : We can end while-loop whenever we want")
print("-"*20)
# -------------

my_courses = ["C++", "Java-1", "Perl", "Java-2", "Python"]
print("my_courses:", my_courses, end="\n\n")

# Requirement: Check are there any value starting with Java

index_no = 0
while index_no < len(my_courses):
    each_course = my_courses[index_no]
    index_no = index_no + 1
    if each_course.startswith("Java"):
        print("Course Found")
        break

# for each_course in my_courses:
#     if each_course.startswith("Java"):
#         print("Course Found")
#         break

print("#"*40, end="\n\n")
##########################

print("""
# Option-2: 'continue-statement': We can skip current iteration,
#           and we can send it for next iteration whenever we want
""")
print("-" * 20)
# -------------

my_courses = ["C++", "Java-1", "Perl", "Java-2", "Python"]
print("my_courses:", my_courses, end="\n\n")

index_no = 0
while index_no < len(my_courses):
    each_course = my_courses[index_no]
    index_no = index_no + 1
    # Below code is applicable only for java course
    # Other than Java courses are not required
    # so, we can goto next iteration
    if not each_course.startswith("Java"):
        continue  # Send it to next iteration
    print("This Java course name is:", each_course)
    print("This Java course duration is 5 days")
    print("This Java course mode is Online", end="\n\n")

# for each_course in my_courses:
#     # Below code is applicable only for java course
#     # Other than Java courses are not required
#     # so, we can goto next iteration
#     if not each_course.startswith("Java"):
#         continue # Send it to next iteration
#     print("This Java course name is:", each_course)
#     print("This Java course duration is 5 days")
#     print("This Java course mode is Online", end="\n\n")

print("#" * 40, end="\n\n")
##########################

print("Iterate dictionary")
print("-"*20)
# -------------

my_dictionary = {"duration": 5, "course": "python", "mode": "online"}
print("my_dictionary:", my_dictionary, end="\n\n")

list_of_keys = list(my_dictionary.keys())
index_no = 0
while index_no < len(list_of_keys):
    key = list_of_keys[index_no]
    index_no = index_no + 1
    print("Key:", key)
    print("Value:", my_dictionary[key])


# for i in my_dictionary: # Iterate KEY, so i will be key
#     print("Key:", i)
#     print("Value:", my_dictionary[i])

print("#"*40, end="\n\n")
##########################