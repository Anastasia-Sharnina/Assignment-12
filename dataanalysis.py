import numpy as np
import pandas as pd

# Step 1: Create an ndarray that represents company income for 10 months
income = np.array([10000, 12000, 15000, 18000, 20000, 22000, 25000, 27000, 30000, 32000])  # Income for Jan to Oct

# Step 2: Multiply these incomes by 0.7 to get income without tax
income_without_tax = income * 0.7

# Step 3: Create another data collection that represents company expenses for the same 10 months
expenses = np.array([8000, 9000, 11000, 13000, 14000, 16000, 17000, 19000, 21000, 23000])  # Expenses for Jan to Oct

# Step 4: Create a DataFrame based on income_without_tax and expenses
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct']
data = {
    'Month': months,
    'Income_without_tax': income_without_tax,
    'Expenses': expenses
}
df = pd.DataFrame(data)

# Step 5: Output the DataFrame on the screen
print("Full DataFrame:")
print(df)

# Step 6: Output the data related to the 1st quarter only (Jan, Feb, Mar)
first_quarter_df = df[df['Month'].isin(['Jan', 'Feb', 'Mar'])]
print("nData for the 1st Quarter (Jan, Feb, Mar):")
print(first_quarter_df)
