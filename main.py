import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('animal_data.csv', header=0)

# Display the first few rows of the DataFrame
#print(df.head())

# Filter rows where 'Conservation Status' is 'Endangered'
endangered_animals = df[df['Conservation Status'] == 'Endangered']
long_lived = df[df['Average Lifespan (Years)'] > 50] 

# Print the filtered rows
print(f"Endagered Animal! {endangered_animals}")
print(f"Long Lived Animal! {long_lived}")
print(f"Long Lived Animal Name {long_lived['Name']}") #value for long lived dict 

