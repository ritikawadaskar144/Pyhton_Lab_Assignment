name = input("Enter Vendor Name: ")
year = input("Enter Year of Association: ")
contact = input("Enter Contact Number: ")
email = input("Enter Email ID: ")

monthly_purchase = []

print("Enter monthly purchase amounts:")

for i in range(1, 13):
    amount = float(input(f"Month {i}: "))
    monthly_purchase.append(amount)

annual_total = sum(monthly_purchase)

print("\n Annual Billing Report ")
print("Vendor Name:", name)
print("Year of Association:", year)
print("Contact:", contact)
print("Email:", email)
print("Total Annual Purchase:", annual_total)
