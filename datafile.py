import pandas as pd

df = pd.read_csv("IndianWeatherRepository.csv")

# Specify the state you want to keep
state_to_keep = 'Maharashtra'

# Create a boolean mask to filter rows based on the specified state
mask = df['region'] == state_to_keep

# Use the mask to select rows that match the specified state
filtered_df = df[mask]

# Display the filtered DataFrame
print(filtered_df)
filtered_df.to_csv('current_maha.csv', index=False)
