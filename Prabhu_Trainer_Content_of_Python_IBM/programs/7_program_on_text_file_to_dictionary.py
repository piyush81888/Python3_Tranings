"""
Get data from web_server.log

then

Extract
IP
DATE
URL

then

keep extracted data in dictionary

Expected Dictionary:
----------------
{
    0: ('123.123.123.123','26/Apr/2000','http://www.jafsoft.com/asctortf/'),
    1: ('123.123.123.123','26/Apr/2000','http://search.netscape.com/Computers/Data_Formats/Document/Text/RTF'),
    2: ('123.123.123.123','26/Apr/2000','http://www.jafsoft.com/asctortf/'),
    3: ('123.123.123.123','26/Apr/2000','http://www.jafsoft.com/asctortf/'),
    4: ('123.123.123.123','26/Apr/2000','http://www.jafsoft.com/asctortf/'),
    5: ('123.123.123.123','26/Apr/2000','http://www.jafsoft.com/asctortf/')
}
----------------
"""

"""
OPTION-1
Using standard library 'json',
we can create json file using 
    numbers, string, tuple, list, dictionary
If we have data in other type like set, frozenset
then convert to list/tuple/dictionary and write to json
"""

"""
OPTION-2:
like 'json' library, we have many other libraries
which support reading/writing to json file
"""


print("Get data from web_server.log")
print("-"*20)
# -------------

my_log_file_handle = open(r"../log/web_server.log", "r")
log_file_content = my_log_file_handle.readlines()
my_log_file_handle.close()

print(log_file_content)

print("#"*40, end="\n\n")
##########################


print("Extract Info and write to dictionary")
print("-"*20)
# -------------

output_dictionary = {}
key = 0
for each_line in log_file_content:
    if each_line.startswith("123"):
        sp = each_line.split()
        # print("\nsp:", sp, end="\n\n")

        ip = sp[0]

        raw_date = sp[3] # '[26/Apr/2000:00:23:51'
        colon_index = raw_date.index(":")
        dt = raw_date[1:colon_index]

        raw_url = sp[10] # '"http://www.jafsoft.com/asctortf/"'
        url = raw_url[1:-1]
        each_line_tuple = (ip, dt, url)
        output_dictionary[key] = each_line_tuple
        key = key + 1


# Example:
# >>> D = {}
# >>> D[0] = (10,20)
# >>> D[1] = (10,20)
# >>> D
# {0: (10, 20), 1: (10, 20)}
# >>>


print(output_dictionary)

print("#"*40, end="\n\n")
##########################

print("Writing to log_report_1.json")
print("-"*20)
# -------------

my_json_file_handle = open("log_report_1.json", "w")

import json
json.dump(output_dictionary, my_json_file_handle) # write to json file

my_json_file_handle.close()

print("Created log_report_1.json file. Please check")

print("#"*40, end="\n\n")
##########################

print("Reading from log_report_1.json")
print("-"*20)
# -------------

my_json_file_handle = open("log_report_1.json", "r")

import json
json_file_content = json.load(my_json_file_handle)

my_json_file_handle.close()

print("json_file_content:", json_file_content, end="\n\n")

print("type of json_file_content:", type(json_file_content), end="\n\n")

print("#"*40, end="\n\n")
##########################