"""
Read from log_report.csv
then
write to log_report_2.txt

log_report_2.txt should look like log_report.txt
"""

print("Read from log_report.csv")
print("-"*20)
# -------------

my_csv_file_handle = open("log_report.csv", "r")
csv_file_content = my_csv_file_handle.readlines()
my_csv_file_handle.close()

print(csv_file_content)

print("#"*40, end="\n\n")
##########################

print("print each line using for-loop")
print("-"*20)
# -------------

for each_line in csv_file_content:
    print("Each Line:", repr(each_line))

print("#"*40, end="\n\n")
##########################

print("Write to log_report_2.txt")
print("-"*20)
# -------------

my_out_file_handle = open("log_report_2.txt", "w")

for each_line in csv_file_content:
    print("Each Line:", repr(each_line), end="\n\n")
    sp = each_line.split(",")
    print("sp:", sp, end="\n\n")

    final_url = sp[2].removesuffix("\n")
    print(sp[0], sp[1], final_url, sep="\t", file=my_out_file_handle)

my_out_file_handle.close()

print("""Created
log_report_2.txt
please check
""")

print("#"*40, end="\n\n")
##########################
