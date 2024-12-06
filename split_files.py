import pandas as pd
from sklearn.model_selection import train_test_split

# Read the data file
data = pd.read_csv('filtereddata.txt', header=None)

# Split into train (70%) and test (30%) sets
train_data, test_data = train_test_split(data, test_size=0.3, random_state=42)

# Save train and test sets to files
train_data.to_csv('input.txt', header=False, index=False)
test_data.to_csv('test.txt', header=False, index=False)
