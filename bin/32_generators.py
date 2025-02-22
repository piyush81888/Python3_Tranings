"""
Generator: We can create object/value on the fly
OR
whenever we need value(object), that time we can create object
"""

print("WITHOUT using Generator")
print("-"*20)
# -------------


def my_square_function(my_list):
    result = []
    for i in my_list:
        result.append(i*i)
    return result

L = [1, 2, 3, 4]
squared_list = my_square_function(L)
print("Squared List:", squared_list, end="\n\n")

for i in squared_list:
    print("Each value:", i)

# Here, final requirement is
# print each squared value
# So,
# giving one squared value at a time is enough,
# instead of keeping all squared values in list
#   which occupying the memory
#
# Is it possible to give one square value
#   whener for-loop asks?
# ANSWER: YES, write generator function
print("#"*40, end="\n\n")
##########################

print("USING Generator")
print("-"*20)
# -------------


def my_square_function(my_list):
    for i in my_list:
        each_squared_value = i * i
        yield each_squared_value

L = [1, 2, 3, 4]
squared_list = my_square_function(L)
print("Squared List:", squared_list, end="\n\n")

for i in squared_list:
    print("Each value:", i)

print("#"*40, end="\n\n")
##########################