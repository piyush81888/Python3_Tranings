"""
About print function
"""

print("print function with 'sep' argument")
print("-"*20)
# -------------

a = 10
b = 20
c = 30
d = 40

print(a, b, c, d) # default sep="ONE-SPACE" :In output, It will display each value separated by SPACE
print(a, b, c, d, sep=",") # In output, It will display each value separated by COMMA
print(a, b, c, d, sep="XYZ") # In output, It will display each value separated by XYZ

print("#"*40, end="\n\n")
##########################

print("print function with 'end' argument")
print("-"*20)
# -------------

a = 10
b = 20
c = 30
d = 40

print(a, b, c, d) # By Default, in output, put \n at the end
print(a, b, c, d) # By Default, in output, put \n at the end
print(a, b, c, d, end="\n\n") # put \n\n at the end
print(a, b, c, d, end="\n\n") # put \n\n at the end
print(a, b, c, d, end="\n\n") # put \n\n at the end

print(a, b, c, d, end="XYZ")
print(a, b, c, d, end="ABC")
print(a, b, c, d, end="MMM\n")

# We can also pass 'file' argument to print
# This we will discuss during file operations

print("#"*40, end="\n\n")
##########################
