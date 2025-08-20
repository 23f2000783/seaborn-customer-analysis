# 1. Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 2. Generate realistic synthetic data
# Set a seed for reproducibility
np.random.seed(42)

# Define customer segments and their properties
segments = {
    'High-Value': {'mean': 450, 'std': 120, 'n': 100},
    'Medium-Value': {'mean': 220, 'std': 50, 'n': 250},
    'Low-Value': {'mean': 80, 'std': 25, 'n': 400}
}

# Create an empty list to store data
data = []

# Generate data for each segment
for segment, props in segments.items():
    purchase_amounts = np.random.normal(loc=props['mean'], scale=props['std'], size=props['n'])
    # Ensure no negative purchase amounts
    purchase_amounts = np.abs(purchase_amounts)
    for amount in purchase_amounts:
        data.append({'Segment': segment, 'Purchase Amount': amount})

# Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(data)

# 3. Style the chart for a professional, publication-ready look
# Set the overall style
sns.set_style("whitegrid")
# Set the context for presentation-quality text and elements
sns.set_context("talk", font_scale=0.8)

# 4. Create the boxplot
# Set the figure size (8 inches * 64 dpi = 512 pixels)
plt.figure(figsize=(8, 8))

# Define a professional color palette
palette = {'Low-Value': '#66c2a5', 'Medium-Value': '#fc8d62', 'High-Value': '#8da0cb'}

# Create the boxplot with the corrected arguments
ax = sns.boxplot(
    x='Segment',
    y='Purchase Amount',
    data=df,
    order=['Low-Value', 'Medium-Value', 'High-Value'], # Logical order
    palette=palette,
    width=0.6,
    hue='Segment',      # <-- FIX: Assign the x-variable to hue
    legend=False        # <-- FIX: Disable the redundant legend
)

# 5. Add meaningful titles and labels
plt.title('Purchase Amount Distribution by Customer Segment', fontsize=16, weight='bold')
plt.xlabel('Customer Segment', fontsize=12, weight='bold')
plt.ylabel('Purchase Amount ($)', fontsize=12, weight='bold')

# Remove the top and right spines for a cleaner look
sns.despine()

# 6. Save the chart with specified dimensions
# Use dpi=64 to get a 512x512 pixel image from an 8x8 figure
# bbox_inches='tight' ensures all elements (like labels) are included
plt.savefig('chart.png', dpi=64, bbox_inches='tight')

# Optional: Display the plot if running the script locally
# plt.show()