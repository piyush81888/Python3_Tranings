"""
- Dictionary:
        -- We have option to store multiple values like list of names
        -- We can keep DUPLICATE values
        -- We-can/we-have to provide index to each values
"""

print("Dictionary PART-1")
print("Store values")
print("-"*20)
# -------------

my_dictionary_1 = {0:5, 1:"python", 2:"online"}

# FOR KEYS: We can use any IMMUTABLE VALUES like numbers, string, tuple
my_dictionary_2 = {"duration":5, "course":"python", "mode":"online"}

# FOR VALUES: We can store any type of values in dictionary
my_dictionary_3 = {
    "duration":5,
    "course":"python",
    "mode":["online", "offline"],
    "trainer": {"fname": "abc", "lname": "xyz"}
}

print("my_dictionary_1:", my_dictionary_1)
print("my_dictionary_2:", my_dictionary_2)
print("my_dictionary_3:", my_dictionary_3)

print("#"*40, end="\n\n")
##########################

print("Dictionary PART-2")
print("Access each value using KEY")
print("-"*20)
# -------------

my_dictionary = {
    "duration":5,
    "course":"python",
    "mode":["online", "offline"],
    "trainer": {"fname": "abc", "lname": "xyz"}
}
print("my_dictionary:", my_dictionary, end="\n\n")

print("Duration:", my_dictionary["duration"], end="\n\n") # 5

course_name = my_dictionary["course"] # 'python'
print("2nd character in course_name:", course_name[1]) # "y"
print("Other Way: 2nd character in course_name:", my_dictionary["course"][1], end="\n\n") # "y"

print("Mode:", my_dictionary["mode"]) # ["online", "offline"]
print("Mode:", my_dictionary["mode"][-1]) # "offline"
print("Mode:", my_dictionary["mode"][-1][3], end="\n\n") # "l"

print("Trainer:", my_dictionary["trainer"]) # {"fname": "abc", "lname": "xyz"}
print("LName of the Trainer:", my_dictionary["trainer"]["lname"]) # "xyz"
print("2nd char in LName of the Trainer:", my_dictionary["trainer"]["lname"][1]) # "y"

print("#"*40, end="\n\n")
##########################


print("Dictionary PART-3")
print("List of methods present in 'dict' class")
print("-"*20)
# -------------

print(dir(my_dictionary))
# OR
# print(dir(dict))

print("#"*40, end="\n\n")
##########################

print("Dictionary PART-4")
print("ADD/REMOVE/UPDATE")
print("-"*20)
# -------------

my_dictionary = {"duration":5, "course":"python", "mode":"online"}
print("my_dictionary:", my_dictionary, end="\n\n")

# ADD/UPDATE : same step
my_dictionary["location"] = "India"
# If key present then update else add new values
print("my_dictionary after updating location using ['location']:", my_dictionary, end="\n\n")

another_dictionary = {"location": "India"}
my_dictionary.update(another_dictionary)
# If key present then update else add new values
print("my_dictionary after updating location using update():", my_dictionary, end="\n\n")

# REMOVE
my_dictionary.pop("duration")
print("my_dictionary after pop(duration):", my_dictionary, end="\n\n")
my_dictionary.popitem() # removed last key/value
print("my_dictionary after popitem():", my_dictionary, end="\n\n")

print("#"*40, end="\n\n")
##########################