"""
Seaborn: Plotting graphs
"""

print("Get data from iris.csv file")
print("-"*20)
# -------------

import pandas as pd
iris_data_df = pd.read_csv("Iris.csv")
print(iris_data_df)


print("#"*40, end="\n\n")
##########################

print("iris data in line plot example-1")
print("-"*20)
# -------------

import matplotlib.pyplot as plt

import seaborn as sns
sns.lineplot(data=iris_data_df)

plt.show()

print("#"*40, end="\n\n")
##########################

print("iris data in line plot example-2")
print("-"*20)
# -------------

import matplotlib.pyplot as plt

import seaborn as sns
sns.lineplot(data=iris_data_df, x="Species", y="SepalLengthCm")

plt.show()

print("#"*40, end="\n\n")
##########################

print("iris data in line plot example-3")
print("-"*20)
# -------------

import matplotlib.pyplot as plt

import seaborn as sns
sns.lineplot(data=iris_data_df, x="PetalLengthCm", y="SepalLengthCm")

plt.show()

print("#"*40, end="\n\n")
##########################


print("iris data in scatter plot")
print("-"*20)
# -------------

import matplotlib.pyplot as plt

import seaborn as sns
sns.scatterplot(data=iris_data_df, x="PetalLengthCm", y="SepalLengthCm")

plt.show()

print("#"*40, end="\n\n")
##########################