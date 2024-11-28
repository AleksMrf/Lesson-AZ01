import pandas as pd

df = pd.read_csv('countries_visa_free_access.csv')
print(df.head())

print(df.info())

print(df.describe())
