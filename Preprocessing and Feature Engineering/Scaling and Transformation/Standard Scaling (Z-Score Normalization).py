import pandas as pd
import numpy as np



# Seed for reproducibility
np.random.seed(42)

# Simulating real-life data
# Feature1: Heights in cm, mean = 170, std dev = 10 (normal distribution)
feature1 = np.random.normal(loc=170, scale=10, size=100)

# Feature2: Weights in kg, mean = 70, std dev = 15 (normal distribution)
feature2 = np.random.normal(loc=70, scale=15, size=100)

# Creating the DataFrame
df = pd.DataFrame({
    'Height (cm)': feature1,
    'Weight (kg)': feature2
})

# Display the first few rows of the DataFrame
print(df.head())


# Step 1: Calculate the mean and standard deviation for each feature
means = df.median()
std_devs = df.IQr()

print(means, std_devs)

# Step 2: Apply the Standard Scaling (Z-Score Normalization) formula
df_scaled = (df - means) / std_devs

# Display the original and scaled data
print("Original Data:")
print(df.head())
print("\nScaled Data (Z-Score Normalization):")
print(df_scaled.head())
