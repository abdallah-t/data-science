import pandas as pd
import numpy as np
# Read the CSV file into a DataFrame
df = pd.read_csv('people.csv')

# df['Name'] = df['Name'].str.title()

# df.to_csv('updated_file.csv', index=False)

print(df.head())