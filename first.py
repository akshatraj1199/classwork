import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# data import  -
df = sns.load_dataset("tips")

# data exploration -
print(df.head())
print(df.tail())
print(df.info())
print(df.shape)
print(df.describe())

# manipulation of dataset -
# missing values -
print(df.isna().sum())
# duplicate values -
print(df.duplicated().sum())

# basic stats -
print(df["total_bill"].mean())
print(df["total_bill"].median())
print(df["total_bill"].mode())

# filtering and sorting -
fil = df[(df["day"] == "Sat") & (df["smoker"] == "No")]


sort = df.sort_values("total_bill", ascending=False)
print(sort)

# filling the missing values -
df["size"].fillna(df["size"].median(), inplace = True)

# rename the column -
df.rename(columns={"total_bill" : "totalbill"}, inplace=True)
print(df.head())

# add new column -
df["new_col"] = df["tip"]/df["totalbill"]
print(df.head())

# map - cat convert number -
df["sex"] = df["sex"].map({"Male" : 1, "Female" : 2})
print(df.head())

# relace
df["smoker"] = df["smoker"].replace({"Yes" : "Smoker", "No" : "Non smoker"})
print(df)