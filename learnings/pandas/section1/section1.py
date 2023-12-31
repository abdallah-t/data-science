import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv("people.csv")

# getting the head of the dataframe
# head is the first few rows of the df
head = df.head()
print(head)

# getting the info the dataframe
# info provides the type of each column and 
info = df.info()
print(info)

# getting the shape of the dataframe
# the shape is the row-column tuple of the df
shape = df.shape
print(shape)

# getting the description of the dataframe
# the description show some stats about the dataframe

description = df.describe()
print(description)


# getting hold  of the values of the dataframe
# the values are a numpy 2d array

values = df.values
print(values)


# getting hold of the columns

columns = df.columns
print(columns)


# getting hold the rows

rows = df.index
print(rows)