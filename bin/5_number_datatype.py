"""
- Numbers:
    -- We have option to store numbers like int, float etc
"""
print("Numbers Example")
print("-"*20)
# -------------

a = 10
# internally it will create object of builtin class 'int'
# and inside that object, it will store the value 10
b = 12.5
# internally it will create object of builtin class 'float'
# and inside that object, it will store the value 12.5

c = a + b

print(a, b, c, sep="\n")

print("#"*40, end="\n\n")
##########################