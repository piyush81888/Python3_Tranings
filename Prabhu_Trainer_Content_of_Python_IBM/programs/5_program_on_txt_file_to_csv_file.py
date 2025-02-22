"""
Read from log_report.txt
then
write to log_report_2.csv

log_report_2.csv should look like log_report.csv
"""

print("Read from log_report.txt")
print("-"*20)
# -------------

my_txt_file_handle = open(r"log_report.txt", "r")
log_report_file_content = my_txt_file_handle.readlines()
my_txt_file_handle.close()

print("log_report_file_content:", log_report_file_content, sep="\n")

print("#"*40, end="\n\n")
##########################

print("FOR UNDERSTANDING: print each line in raw format")
print("-"*20)
# -------------

for each_line in log_report_file_content:
    print("Each Line:", repr(each_line), end="\n\n")
    sp = each_line.split("\t")
    print("After Split:", sp, end="\n\n")

print("#"*40, end="\n\n")
##########################

print("1-WAY: write to log_report_2.csv")
print("-"*20)
# -------------

my_csv_file_handle = open(r"log_report_2.csv", "w")

for each_line in log_report_file_content:
    sp = each_line.split("\t")
    print("sp:", sp, end="\n\n")
    ip = sp[0]
    dt = sp[1]
    url = sp[2]
    # remove \n
    url = url.removesuffix("\n")
    print(ip, dt, url, sep=",", file=my_csv_file_handle) # by default end="\n"

my_csv_file_handle.close()

print("""
log_report_2.csv file created, Please check
""")

print("#"*40, end="\n\n")
##########################

print("2-WAY: write to log_report_3.csv")
print("-"*20)
# -------------

my_csv_file_handle = open(r"log_report_3.csv", "w")

for each_line in log_report_file_content:

    # 1-way
    final_line = each_line.replace("\t", ",")
    my_csv_file_handle.write(final_line)

    # 2-way
    final_line = each_line.replace("\t", ",")
    final_line = final_line.replace("\n", "")
    # because print() will put \n at the end
    print(final_line, file=my_csv_file_handle)


my_csv_file_handle.close()

print("""
log_report_2.csv
log_report_3.csv
file created, Please check
""")

print("#"*40, end="\n\n")
##########################
