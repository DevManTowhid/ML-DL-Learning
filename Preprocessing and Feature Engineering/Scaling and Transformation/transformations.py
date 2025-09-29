import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.preprocessing import PowerTransformer, QuantileTransformer

# Generate sample skewed data (Income data)
np.random.seed(42)
data = {'Income': np.random.chisquare(df=2, size=1000) * 1000}  # Chi-square distribution to simulate skewed data
df = pd.DataFrame(data)

# Step 1: Log Transformation
df['Log_Income'] = np.log(df['Income'] + 1)  # Adding 1 to avoid log(0)

# Step 2: Square Root Transformation
df['Sqrt_Income'] = np.sqrt(df['Income'])

# Step 3: Box-Cox Transformation (positive data only)
df['BoxCox_Income'], lambda_param = stats.boxcox(df['Income'])

# Step 4: Yeo-Johnson Transformation (can handle both positive and negative data)
scaler_yeo_johnson = PowerTransformer(method='yeo-johnson')
df['YeoJohnson_Income'] = scaler_yeo_johnson.fit_transform(df[['Income']])

# Step 5: Quantile Transformation (normal distribution output)
quantile_transformer = QuantileTransformer(output_distribution='normal')
df['Quantile_Transformed_Income'] = quantile_transformer.fit_transform(df[['Income']])

# Step 6: Power Transformation (similar to Box-Cox)
scaler_power = PowerTransformer()
df['Power_Transformed_Income'] = scaler_power.fit_transform(df[['Income']])

# Plotting all transformations
plt.figure(figsize=(15, 10))

# Original Distribution
plt.subplot(3, 3, 1)
plt.hist(df['Income'], bins=50, color='skyblue', edgecolor='black')
plt.title('Original Income Distribution')

# Log Transformation
plt.subplot(3, 3, 2)
plt.hist(df['Log_Income'], bins=50, color='skyblue', edgecolor='black')
plt.title('Log Transformation')

# Square Root Transformation
plt.subplot(3, 3, 3)
plt.hist(df['Sqrt_Income'], bins=50, color='skyblue', edgecolor='black')
plt.title('Square Root Transformation')

# Box-Cox Transformation
plt.subplot(3, 3, 4)
plt.hist(df['BoxCox_Income'], bins=50, color='skyblue', edgecolor='black')
plt.title('Box-Cox Transformation')

# Yeo-Johnson Transformation
plt.subplot(3, 3, 5)
plt.hist(df['YeoJohnson_Income'], bins=50, color='skyblue', edgecolor='black')
plt.title('Yeo-Johnson Transformation')

# Quantile Transformation (Normal Distribution)
plt.subplot(3, 3, 6)
plt.hist(df['Quantile_Transformed_Income'], bins=50, color='skyblue', edgecolor='black')
plt.title('Quantile Transformation')

# Power Transformation
plt.subplot(3, 3, 7)
plt.hist(df['Power_Transformed_Income'], bins=50, color='skyblue', edgecolor='black')
plt.title('Power Transformation')

plt.tight_layout()
plt.show()
