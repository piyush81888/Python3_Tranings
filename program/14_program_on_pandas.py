"""
Get data from below sources
1. log_report.txt
2. log_report.csv
3. log_report_1.json
4. log_report_2.json
5. my_database.db

produce single report in below files
final_report.csv
final_report.xlsx
final_report.json
final_report.xml
"""

print("txt_file_df:")
print("-"*20)
# -------------

import pandas as pd
txt_file_df = pd.read_csv("log_report.txt", sep="\t")
print(txt_file_df)

print("#"*40, end="\n\n")
##########################

print("csv_file_df:")
print("-"*20)
# -------------

import pandas as pd
csv_file_df = pd.read_csv("log_report.csv")
print(csv_file_df)

print("#"*40, end="\n\n")
##########################

print("json_file_df:")
print("-"*20)
# -------------

import pandas as pd
json_file_df = pd.read_json("log_report_1.json")
print(json_file_df)

print("#"*40, end="\n\n")
##########################

print("json_file_df after rotate:")
print("-"*20)
# -------------

json_file_df = json_file_df.T # Transpose -> Rotate
print(json_file_df)

print("#"*40, end="\n\n")
##########################

print("list of columns in json_file_df:")
print("-"*20)
# -------------

print(json_file_df.columns)

print("#"*40, end="\n\n")
##########################

print("list of columns in json_file_df after changing column names:")
print("-"*20)
# -------------

json_file_df.columns = ["IP", "DATE", "URL"]
print(json_file_df.columns)

print("#"*40, end="\n\n")
##########################

print("json_file_df_2:")
print("-"*20)
# -------------

import pandas as pd
json_file_df_2 = pd.read_json("log_report_2.json")
print(json_file_df_2)

print("#"*40, end="\n\n")
##########################

print("list of columns in json_file_df_2 after changing column names:")
print("-"*20)
# -------------

json_file_df_2.columns = ["IP", "DATE", "URL"]
print(json_file_df_2.columns)

print("#"*40, end="\n\n")
##########################

print("my_db_data_df:")
print("-"*20)
# -------------

import sqlite3
my_db_connection = sqlite3.connect("my_database.db")

import pandas as pd
my_db_data_df = pd.read_sql("SELECT * FROM MY_TABLE", my_db_connection)

print(my_db_data_df)

print("#"*40, end="\n\n")
##########################

print("Merge All")
print("-"*20)
# -------------
# Total 5 dfs:
#
# txt_file_df
# csv_file_df
# json_file_df
# json_file_df_2
# my_db_data_df

import pandas as pd
all_in_one_df = pd.concat([txt_file_df, csv_file_df, json_file_df, json_file_df_2, my_db_data_df], axis=0)
# axis=0 : Merge one below the other
print(all_in_one_df)

print("#"*40, end="\n\n")
##########################


print("All_in_one_df after reseting index")
print("-"*20)
# -------------

all_in_one_df = all_in_one_df.reset_index(drop=True)
# drop=True : remove existing index column
print(all_in_one_df)

print("#"*40, end="\n\n")
##########################

print("All_in_one_df after removing duplicates")
print("-"*20)
# -------------

# all_in_one_df = all_in_one_df.drop_duplicates()
# print(all_in_one_df)

print("#"*40, end="\n\n")
##########################

print("Write to files")
print("-"*20)
# -------------

# final_report.csv
all_in_one_df.to_csv("final_report.csv", index=None)

# final_report.xlsx
all_in_one_df.to_excel("final_report.xlsx", index=None)

# final_report.json
all_in_one_df.to_json("final_report_1.json")

rotated_df = all_in_one_df.T
rotated_df.to_json("final_report_2.json")

# final_report.xml
all_in_one_df.to_xml("final_report.xml")

print("""
Created below files, please check
final_report.csv
final_report.xlsx
final_report.json
final_report.xml
""")

print("#"*40, end="\n\n")
##########################