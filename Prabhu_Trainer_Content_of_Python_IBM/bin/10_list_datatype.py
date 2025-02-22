"""
list:
        -- We have option to store multiple values like list of names
        -- We can keep DUPLICATE values
        -- Automatically index number will be assigned to each value
"""
print("list PART-1")
print("Store Multiple Values")
print("-"*20)
# -------------

my_list = [10, 12.5, "python", (100, 200)]
# Internally it will create object of 'list' class and store the values
print("my_list:", my_list)

print("#"*40, end="\n\n")
##########################

print("list PART-2")
print("Indexes are similar to strings")
print("-"*20)
# -------------

my_list = [10, 12.5, "python", (100, 200)]
print("my_list:", my_list, end="\n\n")

print("Course Name:", my_list[2]) # 'Python'
print("2nd char in Course Name:", my_list[2][1], end="\n\n") # 'y'

print("Last value in my_list:", my_list[-1]) # (100, 200)
print("2nd value in nested list:", my_list[-1][-1]) # 200

print("#"*40, end="\n\n")
##########################

print("list PART-3")
print("Methods present inside 'list' class")
print("-"*20)
# -------------

print(dir(my_list))
# OR
# print(dir(list))

print("#"*40, end="\n\n")
##########################


print("list PART-4")
print("count and index methods")
print("-"*20)
# -------------

my_list = [10, 12.5, "python", (100, 200)]
print("my_list:", my_list, end="\n\n")

count_of_python = my_list.count("python") # 1
index_of_python = my_list.index("python") # 2

print("count_of_python:", count_of_python)
print("index_of_python:", index_of_python)

print("#"*40, end="\n\n")
##########################

print("list PART-5")
print("ADD/REMOVE/UPDATE")
print("-"*20)
# -------------

my_list = [10, 12.5, "python", (100, 200)]
print("my_list:", my_list, end="\n\n")

# ADD
my_list.append("Java")
print("my_list after adding 'Java':", my_list, end="\n\n")
# [10, 12.5, "python", (100, 200), "Java"]

# UPDATE
my_list[1] = "Perl"
print("my_list after updating to 'Perl':", my_list, end="\n\n")
# [10, "Perl", "python", (100, 200), "Java"]

# REMOVE
my_list.pop() # Remove last value
my_list.pop(2) # Remove value at index 2
my_list.remove("Perl")
print("my_list after deleting 'Java', 'python', 'Perl':", my_list, end="\n\n")
# [10,  (100, 200)]

print("#"*40, end="\n\n")
##########################
