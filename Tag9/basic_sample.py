import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


path = r"E:\Workspaces\Kurse\aktueller-kurs\Material\WA_Fn-UseC_-Telco-Customer-Churn.csv"
# Load data
data = pd.read_csv(path)

print(data)

# Basic data analysis with pandas
print(data.describe())  # Show basic statistics of the dataset

print(list(data.keys()))
# Visualize the data with seaborn
#sns.pairplot(data)  # Create a pairplot
#plt.show()  # Display the plot

data_dict = data.to_dict(orient="records")
print(len(data_dict))


ad = data[["gender", "SeniorCitizen", "Churn"]]
ad['SeniorCitizen'] = ad['SeniorCitizen'].replace({0: "No", 1: "Yes"})

grouped_data = ad.groupby(["gender", "SeniorCitizen", "Churn"])["Churn"].count()
print(grouped_data)

grouped_data.to_excel("output.xlsx")#, index=False)
