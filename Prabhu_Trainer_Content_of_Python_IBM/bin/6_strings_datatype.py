"""
- String:
    -- We have option to store text data like name, email-id etc
    -- Automatically index number will be assigned to each value
"""

print("Strings PART-1")
print("Store the values")
print("-"*20)
# -------------

a = 'PERSON'
b = "PERSON'S"
c = """PERSON'S HEIGHT IS XYZ" (" REPRESENTS INCH)"""
d = '''PERSON'S HEIGHT IS XYZ" (" REPRESENTS INCH)'''
e = 'PERSON\'S'

# In all the above cases, it will create object of builtin class 'str' and
# store the values

print(a, b, c, d, e, sep="\n")

# Not assigned to any variable
# it is comment
'''PERSON'S HEIGHT IS XYZ" (" REPRESENTS INCH)'''

print("#"*40, end="\n\n")
##########################


print("Strings PART-2")
print("Store the values")
print("-"*20)
# -------------

my_file_path_1 = "C:\newfolder\test.py"
# \n-> will get replaced with newline
# \t-> will get replaced with tab space


my_file_path_2 = r"C:\newfolder\test.py"
# r -> raw string, no special meaning for \n\t

# Convert non-raw to raw string
my_file_path_3 = repr(my_file_path_1)

print("\nmy_file_path_1:", my_file_path_1, end="\n\n")
print("my_file_path_2:", my_file_path_2, end="\n\n")
print("my_file_path_3:", my_file_path_3, end="\n\n")

print("#"*40, end="\n\n")
##########################

print("Strings PART-3")
print("Store the values")
print("-"*20)
# -------------

x = 10
y = 20

my_string = f"value of x is {x} and value of y is {y}"
# f -> format
# f -> replaces {variable_name} with value
print("my_string:", my_string)

print("#"*40, end="\n\n")
##########################

# Some Example:
#
# x = "Hello"
# print(x)
# print("Hello")
# print(f"value of x is {x} and value of y is {y}")

print("Strings PART-4")
print("Indexes: Access each character using index")
print("-"*20)
# -------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

# Refer example-1 in 7_strings.xlsx file

print("Get 0th character using positive index:", my_string[0])
print("Get 0th character using negative index:", my_string[-8])

# print("Get 1000th character using positive index:", my_string[1000]) # ERROR

print("#"*40, end="\n\n")
##########################

print("Strings PART-5")
print("Slicing: Getting substring")
print("-"*20)
# -------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

# Refer example-2 in 7_strings.xlsx file

print("sub string from index-1 to 6 using positive indexes:", my_string[1:6])
print("sub string from index-1 to 6 using negative indexes:", my_string[-7:-2])
print("sub string from index-1 to 6 using positive/negative indexes:", my_string[1:-2])
print("sub string from index-1 to 6 using positive/negative indexes:", my_string[-7:6], end="\n\n")

print("sub string from index-1 to END using positive indexes:", my_string[1:])
print("sub string from index-1 to END using negative indexes:", my_string[-7:], end="\n\n")

print("sub string from BEGINNING to 6 using positive indexes:", my_string[:6])
print("sub string from BEGINNING to 6 using negative indexes:", my_string[:-2], end="\n\n")

print("#"*40, end="\n\n")
##########################

print("Strings PART-6")
print("Step Value: We can skip characters in between")
print("-"*20)
# -------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

# Refer example-3 in 7_strings.xlsx file

print("sub string from index-1 to 6 using positive index with default step=1:", my_string[1:6])
print("sub string from index-1 to 6 using negative index with default step=1:", my_string[-7:-2])
# step=1: which means from index-1 to 6, give me every character

print("sub string from index-1 to 6 using positive index with step=1:", my_string[1:6:1])
print("sub string from index-1 to 6 using negative index with step=1:", my_string[-7:-2:1])
# step=1: which means from index-1 to 6, give me every character

print("sub string from index-1 to 6 using positive index with step=2:", my_string[1:6:2])
print("sub string from index-1 to 6 using negative index with step=2:", my_string[-7:-2:2])
# step=2: which means from index-1 to 6, give me every 2nd character

print("sub string from index-1 to 6 using positive index with step=3:", my_string[1:6:3])
print("sub string from index-1 to 6 using negative index with step=3:", my_string[-7:-2:3])
# step=2: which means from index-1 to 6, give me every 3rd character

print("#"*40, end="\n\n")
##########################


print("Strings PART-7")
print("-ve Step Value: We can traverse in reverse direction")
print("-"*20)
# -------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

# Refer example-4 in 7_strings.xlsx file

# Example: index-6 to 1 in reverse then
# we need to follow below steps
# step-1: start index should be 6
# step-2: end index should be 1
# step-3: step value should be -ve
# IMPORTANT: If we miss any of the steps then we will get EMPTY string

print("sub string from index-6 to 1 using positive index with step=-1:", my_string[6:1:-1])
print("sub string from index-6 to 1 using negative index with step=-1:", my_string[-2:-7:-1], end="\n\n")

print("sub string from index-6 to 1 using positive index with step=-2:", my_string[6:1:-2])
print("sub string from index-6 to 1 using negative index with step=-2:", my_string[-2:-7:-2], end="\n\n")

print("sub string from index-6 to 1 using positive index with step=-3:", my_string[6:1:-3])
print("sub string from index-6 to 1 using negative index with step=-3:", my_string[-2:-7:-3], end="\n\n")

print("#"*40, end="\n\n")
##########################

print("Strings PART-8")
print("Methods pres ent inside 'str' class")
print("-"*20)
# -------------

print(dir(my_string))
# OR
# print(dir(str))


print("#"*40, end="\n\n")
##########################


print("Strings PART-9")
print("help() function")
print("-"*20)
# -------------

print(help(str))


print("#"*40, end="\n\n")
##########################

print("Strings PART-10")
print("help() function")
print("-"*20)
# -------------

print(help(str.startswith))


print("#"*40, end="\n\n")
##########################


# --------------
# Why __names??
# --------------
# __names are system defined names
# -- We are not directly calling these __named methods
# -- these __ methods are internally called by some operators
#       OR some functions
#       OR
#       through function or operators we are calling those methods
#
# Example:
# s1 = "Hello"
# s2 = "Hi"
# s3 = s1 + s2 # Internally + calls __add__
# len(s3) # Internallly it calls __len__ present inside str class
# 7
# s1[1]
# 'e'
# s1.__getitem__(1)
# 'e'
# # [] -> calling __getitem__ method
##########################


print("Strings PART-11")
print("Learning startswith() method")
print("-"*20)
# -------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

startswith_result = my_string.startswith("WEL") # True/False
print("startswith_result:", startswith_result) # True

print("#"*40, end="\n\n")
##########################
