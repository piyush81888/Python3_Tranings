"""
Get data from web_server.log
then extract info using regular expression
then
send it to database
"""

"""
How to communicate with database in python?

python-program  <--Communicate Using Library-->  Any Databases(SQL/No-SQL)

Example:
python-program  <--Communicate Using Library (cx-oracle) -->  Oracle Database
python-program  <--Communicate Using Library (mysql.connector) -->  MySQL Database
python-program  <--Communicate Using Library (sqlite3) -->  SQlite Database
"""

"""
We need database
- We can use SQLite database
- We lightweight database
- SQLite is serverless database
- It will just create one db file, on that db file we can execute the query
"""

"""
How to create/communicate with SQLite database
2 OPTIONS:
1. Using SQLite database software
2. WITHOUT Using SQLite database software,
    python library sqlite3 will be able to create database
    and communicate with database
"""
print("Create database and table")
print("-"*20)
# -------------

import sqlite3

print("Creating or connecting to database 'my_database.db'")
my_db_connection = sqlite3.connect("my_database.db")
print("Done\n")

print("To execute SQL statements, create cursor object")
my_db_cursor = my_db_connection.cursor()
print("Done\n")

print("Create table if not present")
my_query = """
CREATE TABLE IF NOT EXISTS MY_TABLE(
IP VARCHAR(100),
DATE VARCHAR(100),
URL VARCHAR(100)
)
"""
my_db_cursor.execute(my_query)
print("Done\n")


print("#"*40, end="\n\n")
##########################

print("Get data from web_server.log")
print("-"*20)
# -------------

my_log_file_handle = open(r"../log/web_server.log", "r")
log_file_content = my_log_file_handle.readlines()
my_log_file_handle.close()

print(log_file_content)

print("#"*40, end="\n\n")
##########################

print("EXTRACT IP, DATE, URL and write to database table 'my_table':")
print("-"*20)
# -------------

import re

for each_line in log_file_content:
    match_result = re.match(r'(\d\d\d\.\d{3}\.\d{1,3}\.[0-9]{3}).*(\d{2}/[a-zA-Z]{3}/\d{4}).*(http[s]?://[a-z./A-Z_]+).*', each_line)
    if match_result is not None:
        ip = match_result.group(1)
        dt = match_result.group(2)
        url = match_result.group(3)
        my_query = f"INSERT INTO MY_TABLE VALUES('{ip}', '{dt}', '{url}')"
        print("Executing Query:", my_query)
        my_db_cursor.execute(my_query)
        print("One record inserted\n")

my_db_connection.commit()
print("All records are inserted, check database\n")

print("#"*40, end="\n\n")
##########################

print("Getting data from database")
print("-"*20)
# -------------

my_query = "SELECT * FROM MY_TABLE"
my_db_cursor.execute(my_query)
my_db_result = my_db_cursor.fetchall()
my_db_connection.close()

print(my_db_result)

print("#"*40, end="\n\n")
##########################
