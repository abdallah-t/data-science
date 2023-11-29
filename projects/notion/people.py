import pandas as pd
import numpy as np
# Read the CSV file into a DataFrame
df = pd.read_csv('people.csv')

df['Name'] = df['Name'].str.title()

# Function to determine the country based on the phone number prefix
def determine_country(phone_number):
    phone_number = str(phone_number)
    if phone_number.startswith('20'):
        return 'Egypt'
    elif phone_number.startswith('973'):
        return 'Bahrain'
    else:
        return 'Unknown'  # You can change this to handle other cases

# Apply the function to create the 'phone-country' column
df['phone-country'] = df['phone number'].apply(determine_country)

# Optional: Display the DataFrame to verify the results
df.to_csv('updated_file.csv', index=False)
print(df)
