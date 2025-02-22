"""
conditional block 'if-block': We can execute block code based on condition
"""

print("using 'if-block'")
print("-"*20)
# -------------

x = 10
if x == 10:
    print("Value of x is eq to 10")
    print("Value of x is eq to 10")
    print("Value of x is eq to 10")

print("outside the block, some other statement")

if x > 10:
    print("Value of x is gt  10")
    print("Value of x is gt  10")
    print("Value of x is gt  10")

if x < 10:
    print("Value of x is eq to 10")
    print("Value of x is eq to 10")
    print("Value of x is eq to 10")

print("#"*40, end="\n\n")
##########################

print("using 'if-elif-block'")
print("-"*20)
# -------------

x = 10
if x == 10:
    print("Value of x is eq to 10")
    print("Value of x is eq to 10")
    print("Value of x is eq to 10")

elif x > 10:
    print("Value of x is gt  10")
    print("Value of x is gt  10")
    print("Value of x is gt  10")

elif x < 10:
    print("Value of x is eq to 10")
    print("Value of x is eq to 10")
    print("Value of x is eq to 10")

print("#"*40, end="\n\n")
##########################


print("using 'if-elif-else-block'")
print("-"*20)
# -------------

x = 10
if x == 10:
    print("Value of x is eq to 10")
    print("Value of x is eq to 10")
    print("Value of x is eq to 10")

elif x > 10:
    print("Value of x is gt  10")
    print("Value of x is gt  10")
    print("Value of x is gt  10")

else:
    print("Value of x is eq to 10")
    print("Value of x is eq to 10")
    print("Value of x is eq to 10")

print("#"*40, end="\n\n")
##########################


print("using 'if-block' with collection classes like str, list, tuple etc")
print("-"*20)
# -------------

my_string = "python"
my_list = ["Java", "perl", 200, "python"]

if ("th" in my_string) and (my_string != "Java") and ("perl" in my_list):
    print("All conditions are True")

print("#"*40, end="\n\n")
##########################

print("using 'if-block' with dictionary")
print("-"*20)
# -------------

my_dictionary = {"duration":5, "course":"python", "mode":"online"}
print("my_dictionary:", my_dictionary, end="\n\n")

# >>> my_dictionary.keys()
# ['duration', 'course', 'mode']
if "course" in my_dictionary.keys():
    print("Key Found")


# >>> my_dictionary.values()
# [5, 'python', 'online']
if "online" in my_dictionary.values():
    print("Value found")

# >>> my_dictionary.items()
# [('duration', 5), ('course', 'python'), ('mode', 'online')]
if ('duration', 5) in my_dictionary.items():
    print("Item found")

print("#"*40, end="\n\n")
##########################