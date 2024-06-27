import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset from CSV
tips = pd.read_csv("tips.csv")
#tips = pd.read_csv("csv_fw.csv")


# Create violin plot
#sns.violinplot(data=tips, x='tip', y='sex', hue='smoker', split=True)
sns.violinplot(data=tips, x='sex', y='tip', hue='smoker')

plt.show()
