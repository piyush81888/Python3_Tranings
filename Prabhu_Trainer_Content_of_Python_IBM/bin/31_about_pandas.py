"""
About pandas
- pandas is one library
- pandas has many methods and many classes
- Few method names are :
    -- read_csv
    -- read_excel
    -- read_json
    -- read_sql
    Many more
- Few class names are:
    - DataFrame class
    - Series Class
    Many other classes

Here, MAIN class is DataFrame class
"""

"""
About MAIN class DataFrame
-- It has many methods which related to tabular data processing
    like csv, xlsx, db-table
"""

print("Inside pandas library")
print("-"*20)
# -------------

import pandas as pd
print(dir(pd))

print("#"*40, end="\n\n")
##########################

print("Inside DataFrame class")
print("-"*20)
# -------------

import pandas as pd
print(dir(pd.DataFrame))

print("#"*40, end="\n\n")
##########################

print("DataFrame Example-1")
print("-"*20)
# -------------

my_df = pd.DataFrame([[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]])
print(my_df)

print("#"*40, end="\n\n")
##########################

print("DataFrame Example-2")
print("-"*20)
# -------------

my_df = pd.DataFrame([[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]],
                     columns=["c1", "c2", "c3", "c4"],
                     index=["r1", "r2", "r3"]
                     )
print(my_df)

print("#"*40, end="\n\n")
##########################


print("sum() method example-1")
print("-"*20)
# -------------

my_df = pd.DataFrame([[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]],
                     columns=["c1", "c2", "c3", "c4"],
                     index=["r1", "r2", "r3"]
                     )
print(my_df.sum())

print("#"*40, end="\n\n")
##########################


print("sum() method example-2")
print("-"*20)
# -------------

my_df = pd.DataFrame([[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]],
                     columns=["c1", "c2", "c3", "c4"],
                     index=["r1", "r2", "r3"]
                     )
print(my_df.sum().sum())

print("#"*40, end="\n\n")
##########################


print("sum() method example-3")
print("-"*20)
# -------------

my_df = pd.DataFrame([[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]],
                     columns=["c1", "c2", "c3", "c4"],
                     index=["r1", "r2", "r3"]
                     )
print(my_df["c1"].sum())

print("#"*40, end="\n\n")
##########################
