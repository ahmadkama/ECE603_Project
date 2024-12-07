import pandas as pd

# Read the input data and mappings
data = pd.read_excel('5G_Dataset_Network_Slicing_CRAWDAD_Shared.xlsx', sheet_name='Model_Inputs_Outputs', usecols='B:J')
mappings = pd.read_excel('5G_Dataset_Network_Slicing_CRAWDAD_Shared.xlsx', sheet_name='Modeling Parameters', usecols='B:J')

# Convert each column to mapped indices (1-indexed)
mapped_data = pd.DataFrame()
for col in data.columns:
    # Get unique values from mapping sheet for this column
    mapping_values = mappings[col].dropna().values
    # Create dictionary mapping values to 1-based indices 
    value_to_index = {val: idx+1 for idx, val in enumerate(mapping_values)}
    # Map the values in data to indices
    mapped_data[col] = data[col].map(value_to_index)

# Save mapped data to txt file
mapped_data.to_csv('large_dataset.txt', index=False, header=False)
