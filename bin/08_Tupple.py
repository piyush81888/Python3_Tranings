"""
Tuple:
        -- We have option to store multiple values like list of names
        -- We can keep DUPLICATE values
        -- Automatically index number will be assigned to each value
"""
print("Tuple PART-1")
print("Store Multiple Values")
print("-"*20)
# -------------

my_tuple = (10, 12.5, "python", (100, 200))
# Internally it will create object of 'tuple' class and store the values
print("my_tuple:", my_tuple)

print("#"*40, end="\n\n")
##########################

print("Tuple PART-2")
print("Indexes are similar to strings")
print("-"*20)
# -------------

my_tuple = (10, 12.5, "python", (100, 200))
print("my_tuple:", my_tuple, end="\n\n")

print("Course Name:", my_tuple[2]) # 'Python'
print("2nd char in Course Name:", my_tuple[2][1], end="\n\n") # 'y'

print("Last value in my_tuple:", my_tuple[-1]) # (100, 200)
print("2nd value in nested tuple:", my_tuple[-1][-1]) # 200

print("#"*40, end="\n\n")
##########################

print("Tuple PART-3")
print("Methods present inside 'tuple' class")
print("-"*20)
# -------------

print(dir(my_tuple))
# OR
# print(dir(tuple))

print("#"*40, end="\n\n")
##########################


print("Tuple PART-4")
print("count and index methods")
print("-"*20)
# -------------

my_tuple = (10, 12.5, "python", (100, 200))
print("my_tuple:", my_tuple, end="\n\n")

count_of_python = my_tuple.count("python") # 1
index_of_python = my_tuple.index("python") # 2

print("count_of_python:", count_of_python)
print("index_of_python:", index_of_python)

print("#"*40, end="\n\n")
##########################