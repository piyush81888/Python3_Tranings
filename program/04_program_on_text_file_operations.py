"""
Get data from web_server.log

then

Extract
IP
DATE
URL

then

Write extracted data to log_report.txt, log_report.csv

Expected file content in log_report.txt:
----------------
    IP                  DATE                URL
123.123.123.123     26/Apr/2000     http://www.jafsoft.com/asctortf/
123.123.123.123     26/Apr/2000     http://search.netscape.com/Computers/Data_Formats/Document/Text/RTF
123.123.123.123     26/Apr/2000     http://www.jafsoft.com/asctortf/
123.123.123.123     26/Apr/2000     http://www.jafsoft.com/asctortf/
123.123.123.123     26/Apr/2000     http://www.jafsoft.com/asctortf/
123.123.123.123     26/Apr/2000     http://www.jafsoft.com/asctortf/
----------------

Expected file content in log_report.csv:
----------------
IP,DATE,URL
123.123.123.123,26/Apr/2000,http://www.jafsoft.com/asctortf/
123.123.123.123,26/Apr/2000,http://search.netscape.com/Computers/Data_Formats/Document/Text/RTF
123.123.123.123,26/Apr/2000,http://www.jafsoft.com/asctortf/
123.123.123.123,26/Apr/2000,http://www.jafsoft.com/asctortf/
123.123.123.123,26/Apr/2000,http://www.jafsoft.com/asctortf/
123.123.123.123,26/Apr/2000,http://www.jafsoft.com/asctortf/
----------------

"""

print("Get data from web_server.log")
print("-"*20)
# -------------
# We can provide Absolute Path
# my_log_file_handle = open(r"C:\python_training\log\web_server.log","r")
# prefix-r : to make RAW string
# 2nd argument "r": mode -> "r"

# OR we can provide Relative Path
my_log_file_handle = open(r"../log/web_server.log", "r")
log_file_content = my_log_file_handle.readlines()
my_log_file_handle.close()

print(log_file_content)

print("#"*40, end="\n\n")
##########################

print("Extract Info and write to files")
print("-"*20)
# -------------

my_txt_file_handle = open("log_report.txt", "w")
my_csv_file_handle = open("log_report.csv", "w")

# Write heading text file
# 1-WAY
# my_txt_file_handle.write("IP\tDATE\tURL\n")

# 2-WAY
# headings = ["IP\t", "DATE\t", "URL\n"]
# my_txt_file_handle.writelines(headings)

# 3-WAY
print("IP", "DATE", "URL", sep="\t", file=my_txt_file_handle)

# Write heading csv file
# 1-WAY
# my_csv_file_handle.write("IP,DATE,URL\n")

# 2-WAY
# headings = ["IP,", "DATE,", "URL\n"]
# my_csv_file_handle.writelines(headings)

# 3-WAY
print("IP", "DATE", "URL", sep=",", file=my_csv_file_handle)

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

        print(ip, dt, url, sep="\t", file=my_txt_file_handle)
        print(ip, dt, url, sep=",", file=my_csv_file_handle)


my_txt_file_handle.close()
my_csv_file_handle.close()

print("""
Files,

log_report.txt
log_report.csv

created, Please check
""")

print("#"*40, end="\n\n")
##########################