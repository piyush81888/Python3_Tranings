"""
Text File Operations: Read/Write text file with any extension like .txt, .log
"""

"""
We need to follow 3 steps
Step-1: Connect to file
Step-2: Read/Write
Step-3: Disconnect
"""

"""
We have functions for all 3 steps
Step-1: Connect to file
    - open() function
Step-2: Read/Write
    - FOR WRITING: 1) write 2) writelines 3) print-function
    - FOR READING: 1) read 2) readlines 3) readline
Step-3: Disconnect
    - close()
"""

print("All write operations")
print("-"*20)
# -------------

# Step-1: Connect to file
# -------------
# my_out_file_handle = open("provide file name or file path here", "provide mode")
my_out_file_handle = open("my_out_file.txt", "w")
# mode 'w': Write only mode, It will create new file
#           IMPORTANT: It erase existing content
# mode 'r': Read only mode, It will NOT create new file
#
# mode 'a': Append only mode, It will create new file only if file not present
#           If file is already present then it will make
#           use of same file


# Step-2: Write
# -------------
# Our data
x = 10
y = "python"

# 1) write : It will take ONE string
my_out_file_handle.write(str(x)+"\n")
my_out_file_handle.write(y+"\n")

# 2) writelines: It will take any collection like list/tuple/etc
L = [str(x)+"\n", y+"\n"]
my_out_file_handle.writelines(L)

# 3) print-function
print(x, y, 20, "java", sep="\n", file=my_out_file_handle)
# x -> no need of converting to string

# Step-3: Disconnect
# -------------
my_out_file_handle.close()

print("""
All write operations are completed,
Please check my_out_file.txt
""")

print("#"*40, end="\n\n")
##########################

print("Reading from file: 1) read()")
print("-"*20)
# -------------

# Step-1: Connect to file
# -------------
my_out_file_handle = open("my_out_file.txt", "r")

# Step-2: Read
# -------------
file_content = my_out_file_handle.read()
# read() : It will return entire file content in ONE string
print("file_content:", file_content, end="\n\n")
print("file_content in raw format:", repr(file_content), end="\n\n")

# Step-3: Disconnect
# -------------
my_out_file_handle.close()

print("#"*40, end="\n\n")
##########################

print("Reading from file: 2) readlines()")
print("-"*20)
# -------------

# Step-1: Connect to file
# -------------
my_out_file_handle = open("my_out_file.txt", "r")

# Step-2: Read
# -------------
file_content = my_out_file_handle.readlines()
# readlines() : It will return entire file content in list
print("file_content:", file_content, end="\n\n")


# Step-3: Disconnect
# -------------
my_out_file_handle.close()

print("#"*40, end="\n\n")
##########################

print("Reading from file: 3) readline()")
print("-"*20)
# -------------

# Step-1: Connect to file
# -------------
my_out_file_handle = open("my_out_file.txt", "r")

# Step-2: Read
# -------------
file_content = my_out_file_handle.readline()
# readline() : It will return one line
print("1st line:", file_content, end="\n\n")

file_content = my_out_file_handle.readline()
# readline() : It will return one line
print("2nd line:", file_content, end="\n\n")

file_content = my_out_file_handle.readline()
# readline() : It will return one line
print("3rd line:", file_content, end="\n\n")

# Step-3: Disconnect
# -------------
my_out_file_handle.close()

print("#"*40, end="\n\n")
##########################

print("Reading from file: 4) read line by line using for-loop")
print("-"*20)
# -------------

# Step-1: Connect to file
# -------------
my_out_file_handle = open("my_out_file.txt", "r")

# Step-2: Read
# -------------
for each_line in my_out_file_handle:
    print("Each Line:", each_line)

# Step-3: Disconnect
# -------------
my_out_file_handle.close()

print("#"*40, end="\n\n")
##########################