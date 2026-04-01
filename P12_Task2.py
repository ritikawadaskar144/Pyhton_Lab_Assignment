import pandas as pd

# Read Excel file
df = pd.read_excel("employee.xlsx")

print("\nEmployee Data:\n")
print(df)

# a) Employees in Automotive domain
auto_emp = df[df['Department'] == "Automotive"]
print("\nEmployees in Automotive Department:\n")
print(auto_emp)

# b) Details of employee by ID
emp_id = int(input("\nEnter Employee ID: "))
emp_details = df[df['Employee ID'] == emp_id]

print("\nEmployee Details:\n")
print(emp_details)

# c) List of Developers
developers = df[df['Designation'] == "Developer"]
print("\nList of Developers:\n")
print(developers)