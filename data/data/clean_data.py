import pandas as pd
import sys      #system module

#check if user provided input and output file
if len(sys.argv) < 3:
    print("Usage: python clean_data.py input.csv output.csv")
    sys.exit()

input_file = sys.argv[1]
output_file = sys.argv[2]

#load data
df = pd.read_csv(input_file)

print("Original Data:")
print(df)

#remove duplicates
df = df.drop_duplicates()

#fill missing values
df['age'] = df['age'].fillna(df['age'].mean()).round().astype(int)
df['salary'] = df['salary'].fillna(df['salary'].mean())
# Save cleaned data
df.to_csv(output_file, index=False)

print("Cleaning complete!")