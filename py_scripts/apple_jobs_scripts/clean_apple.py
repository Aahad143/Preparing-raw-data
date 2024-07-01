import pandas as pd
from pathlib import Path

# Read the CSV file
df = pd.read_csv('raw_data/apple_jobs.csv')

# Split the 'region' column and create new columns
df[['region', 'state', 'country']] = df['region'].str.split(',', expand=True)

# Remove commas from all cell values
df = df.applymap(lambda x: x.replace(',', '') if isinstance(x, str) else x)

# Display the cleaned DataFrame
print(df.head())

# Specify the path to your CSV file
file_path = Path('clean_data/apple_jobs_clean.csv')

# Check if the file exists
if not file_path.exists():
    # Save the cleaned DataFrame to a new CSV file
    df.to_csv(file_path, index=False)
    print("File created successfully")
