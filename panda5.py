import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the Excel file
file_path = '/Users/roccoiacobone/Desktop/Code/PythonCode-1/Lab2data(5).xlsx'
data = pd.read_excel(file_path)

# Extract the PPMSphysm columns
ppmsphysm_columns = ['PPMSphysm1', 'PPMSphysm2', 'PPMSphysm3', 'PPMSphysm4', 'PPMSphysm5']
ppmsphysm_data = data[ppmsphysm_columns]

# Create a scatter plot for each PPMSphysm column
for column in ppmsphysm_columns:
    plt.scatter(data.index, data[column], label=column)

plt.xlabel('Index')
plt.ylabel('PPMSphysm Values')
plt.title('Scatter Plot of PPMSphysm Columns')
plt.legend()
plt.show()