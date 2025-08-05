# filename: airline_filter_plot.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# Load the dataset (adjust the path as needed)
df = pd.read_csv('../Datasets/Global_Fleet.csv')

# Fill NaN values with 0
df = df.fillna(0)

# Display unique regions
print("Available Regions:")
print(df.Region.unique())

# User input for Region
r = input("Enter Region Name: ")
reg = df[df.Region == r]

# Display unique Parent Airlines in that region
print(f"\nAvailable Airlines in {r}:")
print(reg.ParentAirline.unique())

# User input for Airline
a = input("Enter Airline Name: ")
pa = reg[reg.ParentAirline == a]

# Plot bar chart for Aircraft Type vs Current
sb.barplot(x=pa.AircraftType, y=pa.Current)
plt.xticks(rotation=90)
plt.title(f"{a} Aircraft Types and Current Fleet")
plt.tight_layout()
plt.show()
