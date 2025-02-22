"""
Get data from web_server.log
then extract info using regular expression
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

print("Check whether it is IP address line or not (YES/NO)")
print("-"*20)
# -------------

import re

for each_line in log_file_content:
    # match_result = re.match(r'\d\d\d\.\d{3}\.\d{1,3}\.[0-9][0-9][0-9]', each_line)
    # OR
    match_result = re.match(r'\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}.*', each_line)
    print("Each Line:", each_line)
    print("match_result:", match_result, end="\n\n")

# COMMENT
r"""
IDENTIFIERS
------------
\d -> it represent any ONE digit b/n 0 to 9
\D -> it represent any ONE non-digit. Any character except 0 to 9
. -> it represent any ONE any character
\. -> strictly DOT
[0-9] -> it represent any ONE digit b/n 0 to 9
------------

QUANTIFIERS
------------
\d{3} -> internally it will be \d\d\d
\d{1,3} -> minimum one digit, maximum 3 digits
------------

MODIFIERS
------------
* -> 0 or more times
+ -> 1 or more times
? -> 0 or 1 time
------------
"""

print("#"*40, end="\n\n")
##########################

print("EXTRACT IP:")
print("-"*20)
# -------------

import re

for each_line in log_file_content:
    # match_result = re.match(r'\d\d\d\.\d{3}\.\d{1,3}\.[0-9][0-9][0-9]', each_line)
    # OR
    match_result = re.match(r'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3})(.*)', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        remaining = match_result.group(2)
        print("ip:", ip, end="\n\n")
        print("Remaining data:", remaining, end="\n\n")

# COMMENT
r"""
put () to IP address to capture
- this is called grouping
- each group has index number starting from 1
"""

print("#"*40, end="\n\n")
##########################

print("EXTRACT IP, DATE:")
print("-"*20)
# -------------

import re

for each_line in log_file_content:
    # match_result = re.match(r'\d\d\d\.\d{3}\.\d{1,3}\.[0-9][0-9][0-9]', each_line)
    # OR
    match_result = re.match(r'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        print(ip,dt, end="\n\n")


# COMMENT
r"""

26/Apr/2000

26
----
\d\d # Strictly 2 digits
\d{2}# Strictly 2 digits
[0-9][0-9]# Strictly 2 digits
[0-9]{2}# Strictly 2 digits
[0-9]\d# Strictly 2 digits
\d[0-9]# Strictly 2 digits

\d{1,2} # Minimum 1 digit and maximum 2 digits
[0-9]{1,2} # Minimum 1 digit and maximum 2 digits
\d?\d # Minimum 1 digit and maximum 2 digits
[0-9]?[0-9] # Minimum 1 digit and maximum 2 digits
[0-9]?\d # Minimum 1 digit and maximum 2 digits
\d?[0-9] # Minimum 1 digit and maximum 2 digits
---

Apr
---
[A-Z][a-z][a-z]
[A-Z][a-z]{2}
[a-zA-Z]{3}
(Jan|Feb|Mar|Apr)
---

"""

print("#"*40, end="\n\n")
##########################

print("EXTRACT IP, DATE, URL:")
print("-"*20)
# -------------

import re

for each_line in log_file_content:
    # match_result = re.match(r'\d\d\d\.\d{3}\.\d{1,3}\.[0-9][0-9][0-9]', each_line)
    # OR
    match_result = re.match(r'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*(http[s]?://[a-z./A-Z_]+).*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        url = match_result.group(3)
        print(ip,dt,url, end="\n\n")


# COMMENT
r"""
http://search.netscape.com/Computers/Data_Formats/Document/Text/RTF

http[s]?://[a-z./A-Z_]+

http[s]? -> s is optional
https? -> s is optional
https+ -> s one or more time
(https)+ -> exact 'https' one or more time
[https]+ -> It can be 'h'
            OR
            It can be 't'
            OR
            It can be 'p'
            OF
            It can be 's'

"""

print("#"*40, end="\n\n")
##########################
