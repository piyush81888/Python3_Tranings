"""
From the given string,

Extract
IP
DATE
URL

Expected Output:
----------------
123.123.123.123
26/Apr/2000
http://www.jafsoft.com/asctortf/
----------------
"""

print("input data:")
print("-"*20)
# -------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
print(input_data)

print("#"*40, end="\n\n")
##########################

print("Extract IP: 1-way : PARTIAL")
print("-"*20)
# -------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
ip = input_data[0:15]
print(ip)

print("#"*40, end="\n\n")
##########################

print("Extract IP: 2-way ")
print("-"*20)
# -------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
index_of_1st_space = input_data.index(" ")
ip = input_data[0:index_of_1st_space]
print(ip)

# Example:
#
# >>> # About find() method
# >>> # feature-1
# >>> my_string = "WEL COME"
# >>> my_string.find("E") # return index of 1st occurance of 'E'
# 1
# >>> # feature-2
# >>> my_string = "WEL COME"
# >>> my_string.find("E", 3) # start from index-3
# 7
# >>> # feature-3
# >>> my_string = "WEL COME"
# >>> my_string.find("COME") # Returns index of 'C'
# 4
# >>> # feature-4
# >>> my_string = "WEL COME"
# >>> my_string.find("XYZZ") # Returns -1 if not present
# -1
# >>> # find() and index() both are same, except feature-4
# >>> # index will throw error if not found, find() will return -1

print("#"*40, end="\n\n")
##########################

print("Extract IP: 3-way ")
print("-"*20)
# -------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
sp = input_data.split()
print("Value of sp:", sp, end="\n\n")

ip = sp[0]
print("ip:", ip)

print("#"*40, end="\n\n")
##########################