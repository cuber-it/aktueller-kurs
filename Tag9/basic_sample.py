import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
data = pd.read_csv('path_to_your_data.csv')

# Basic data analysis with pandas
print(data.describe())  # Show basic statistics of the dataset

# Visualize the data with seaborn
sns.pairplot(data)  # Create a pairplot
plt.show()  # Display the plot
