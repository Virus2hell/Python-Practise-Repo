import pandas as pd

df = pd.read_csv("Chp13-Pandas/california_housing_test.csv")

print(df.head(10))

print(df['total_bedrooms']) # This will print the total_bedrooms column of the DataFrame df.
print(df['total_bedrooms'][0]) # This will calculate and print the mean (average) of the total_bedrooms column in the DataFrame df using the mean() method.

print(df.total_bedrooms)
print(df.total_bedrooms[0])

