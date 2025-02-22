"""
Write function for log processing

Function-1: log_process_function_1
- It should take 1 argument and argument name is log_file_path
- Function should read the log file content
- Function should extract ip, dt, url
- Function should return extracted info in Dictionary(refer 7th program)

Function-2: log_process_function_2
- It should take 1 argument and argument name is log_file_path
- Function should read the log file content
- Function should extract ip, dt, url
- Function should return extracted info in List (refer 8th program)

Function-3: get_only_ips_function
- It should take 1 argument and argument name is log_file_path
- Function should read the log file content
- Function should extract Only ip
- Function should return extracted info in List =
    ['123.123.123.123', '123.123.123.123','123.123.123.123',]

Function-4: write_output_to_text_file_function
- it takes 2 arguments
    extracted_data_in_dictionary, out_file_path

Function-5: write_output_to_json_file_function
- it takes 2 arguments
    extracted_data_in_dictionary, out_file_path
"""

print("Writing log_process_function_1")
print("-"*20)
# -------------


def log_process_function_1(log_file_path):
    # -----------
    # Read log file
    # -----------
    my_log_file_handle = open(log_file_path, "r")
    log_file_content = my_log_file_handle.readlines()
    my_log_file_handle.close()
    ############

    # -----------
    # Extract info
    # -----------
    output_dictionary = {}
    key = 0
    for each_line in log_file_content:
        if each_line.startswith("123"):
            sp = each_line.split()
            # print("\nsp:", sp, end="\n\n")

            ip = sp[0]

            raw_date = sp[3]  # '[26/Apr/2000:00:23:51'
            colon_index = raw_date.index(":")
            dt = raw_date[1:colon_index]

            raw_url = sp[10]  # '"http://www.jafsoft.com/asctortf/"'
            url = raw_url[1:-1]
            each_line_tuple = (ip, dt, url)
            output_dictionary[key] = each_line_tuple
            key = key + 1

    return output_dictionary
    ############

print("#"*40, end="\n\n")
##########################


print("Calling log_process_function_1")
print("-"*20)
# -------------

extracted_data = log_process_function_1(r"../log/web_server.log")
print(extracted_data)

print("#"*40, end="\n\n")
##########################

print("Writing log_process_function_2")
print("-"*20)
# -------------


def log_process_function_2(log_file_path):
    # -----------
    # Read log file
    # -----------
    my_log_file_handle = open(log_file_path, "r")
    log_file_content = my_log_file_handle.readlines()
    my_log_file_handle.close()
    ############

    # -----------
    # Extract info
    # -----------
    output_list = []
    for each_line in log_file_content:
        if each_line.startswith("123"):
            sp = each_line.split()
            # print("\nsp:", sp, end="\n\n")

            ip = sp[0]

            raw_date = sp[3]  # '[26/Apr/2000:00:23:51'
            colon_index = raw_date.index(":")
            dt = raw_date[1:colon_index]

            raw_url = sp[10]  # '"http://www.jafsoft.com/asctortf/"'
            url = raw_url[1:-1]
            each_line_tuple = (ip, dt, url)
            output_list.append(each_line_tuple)

    return output_list
    ############

print("#"*40, end="\n\n")
##########################


print("Calling log_process_function_2")
print("-"*20)
# -------------

extracted_data = log_process_function_2(r"../log/web_server.log")
print(extracted_data)

print("#"*40, end="\n\n")
##########################

print("Writing log_process_function_3")
print("-"*20)
# -------------


def log_process_function_3(log_file_path):
    # -----------
    # Read log file
    # -----------
    my_log_file_handle = open(log_file_path, "r")
    log_file_content = my_log_file_handle.readlines()
    my_log_file_handle.close()
    ############

    # -----------
    # Extract info
    # -----------
    output_list = []
    for each_line in log_file_content:
        if each_line.startswith("123"):
            sp = each_line.split()
            ip = sp[0]
            output_list.append(ip)

    return output_list
    ############

print("#"*40, end="\n\n")
##########################


print("Calling log_process_function_3")
print("-"*20)
# -------------

extracted_data = log_process_function_3(r"../log/web_server.log")
print(extracted_data)

print("#"*40, end="\n\n")
##########################

print("Write to text file function")
print("-"*20)
# -------------

def write_to_text_file_function(data_dictionary, out_file_path):
    # data_dictionary will be in dictionary
    my_out_file_handle = open(out_file_path, "w")
    print("IP", "DATE", "URL", sep="\t", file=my_out_file_handle)
    for each_row_tuple in data_dictionary.values():
        print(each_row_tuple[0], each_row_tuple[1], each_row_tuple[2], sep="\t", file=my_out_file_handle)
    my_out_file_handle.close()


# Example:
# >>> D
# {0: (10, 20), 1: (10, 20)}
# >>>
# >>>
# >>> {0: (10, 20), 1: (10, 20)}
# {0: (10, 20), 1: (10, 20)}
# >>> D.values()
#  [(10, 20), (10, 20)]

print("#"*40, end="\n\n")
##########################

print("Calling write to text file function")
print("-"*20)
# -------------

data_in_dictionary = log_process_function_1("../log/web_server.log")
print("data_in_dictionary:", data_in_dictionary, end="\n\n")

write_to_text_file_function(data_in_dictionary, "log_report_3.txt")
print("Created log_report_3.txt, please check")

print("#"*40, end="\n\n")
##########################