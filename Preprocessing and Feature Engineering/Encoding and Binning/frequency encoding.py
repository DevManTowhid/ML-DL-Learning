import pandas as pd
import numpy as np

# Generating a sample DataFrame with 100 products and categories
np.random.seed(42) 
products = [f'Product_{i}' for i in range(1, 101)]
categories = np.random.choice(['Electronics', 'Clothing', 'Groceries', 'Toys', 'Furniture'], size=100)

# Creating DataFrame
df = pd.DataFrame({'Product': products, 'Category': categories})

# Manually compute frequency of each category
freq_map = df['Category'].value_counts().to_dict()  # Get the frequency of each category
df['Encoded_Category'] = df['Category'].map(freq_map)  # Map frequencies to each category

# Display the first few rows
print(df.head(10))  # Display the first 10 rows for brevity
