import pandas as pd
import numpy as np

# Generating a sample DataFrame with 100 products and categories
np.random.seed(42) 
products = [f'Product_{i}' for i in range(1, 101)]
categories = np.random.choice(['Electronics', 'Clothing', 'Groceries', 'Toys', 'Furniture'], size=100)

# Creating DataFrame
df = pd.DataFrame({'Product': products, 'Category': categories})



# Step 1: Assign unique category numbers (encoding each category as a unique integer)
df['Category_ID'] = pd.Categorical(df['Category']).codes  # Unique ID for each category

# Step 2: Frequency Encoding (count how many times each category appears)
freq_map = df['Category'].value_counts().to_dict()
df['Frequency'] = df['Category'].map(freq_map)  # Assign frequency to each category

# Step 3: Calculate the number of unique categories for dynamic padding
num_categories = len(df['Category'].unique())



# Step 4: Determine padding size based on number of categories
padding_size = len(str(num_categories))  # Padding size based on the number of categories

# Step 5: Concatenate unique category ID with frequency (with dynamic padding)
df['Custom_Encoded'] = df['Category_ID'].astype(str).str.zfill(padding_size) + df['Frequency'].astype(str).str.zfill(padding_size)

print(df)