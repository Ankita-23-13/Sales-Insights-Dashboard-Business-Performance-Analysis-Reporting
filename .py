import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Example sales dataset
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Sales': [12000, 15000, 18000, 17000, 21000, 25000, 23000, 24000, 22000, 26000, 30000, 32000]
}

df = pd.DataFrame(data)

# Create line plot
sns.set(style="whitegrid")
plt.figure(figsize=(10,6))
sns.lineplot(x='Month', y='Sales', data=df, marker='o', linewidth=2.5, color='royalblue')

# Add title and labels
plt.title("Company Monthly Sales Trend", fontsize=16, fontweight='bold')
plt.xlabel("Month")
plt.ylabel("Sales (USD)")
plt.show()
