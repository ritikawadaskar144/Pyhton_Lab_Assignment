#Practical 11
#Assignment 1

import matplotlib.pyplot as plt

# Data
months = [1,2,3,4,5,6,7,8,9,10,11,12]
total_profit = [211000,183300,224700,222700,209600,201400,
                295500,361400,234000,266700,412800,300200]

facecream = [2500,2630,2140,3400,3600,2760,2980,3700,3540,1990,2340,2900]
facewash = [1500,1200,1340,1130,1740,1555,1120,1400,1780,1890,2100,1760]

# a) Line Plot (Total Profit)
plt.plot(months, total_profit, marker='o')
plt.title("Total Profit Per Month")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.show()

# b) Multiline Plot (All Products)
plt.plot(months, facecream, label="Face Cream")
plt.plot(months, facewash, label="Face Wash")
plt.title("Product Sales Data")
plt.xlabel("Month")
plt.ylabel("Sales Units")
plt.legend()
plt.show()

# c) Bar Chart (Face Cream & Face Wash)
plt.bar(months, facecream, label="Face Cream")
plt.bar(months, facewash, bottom=facecream, label="Face Wash")
plt.title("Face Cream & Face Wash Sales")
plt.xlabel("Month")
plt.ylabel("Units")
plt.legend()
plt.show()

# d) Pie Chart (Yearly Sales)
labels = ["Face Cream", "Face Wash"]
sales = [sum(facecream), sum(facewash)]

plt.pie(sales, labels=labels, autopct='%1.1f%%')
plt.title("Yearly Product Sales")
plt.show()

#Assignment 2
import matplotlib.pyplot as plt

# Company data
companies = ["Microsoft", "Google", "Amazon", "IBM", "Deloitte", "Capgemini", "ATOS", "Amdocs"]
recruitments = [120, 150, 180, 90, 110, 130, 70, 80]

# a) Bar Chart
plt.bar(companies, recruitments)
plt.title("Company Recruitment Data")
plt.xlabel("Companies")
plt.ylabel("No. of Students")
plt.xticks(rotation=45)
plt.show()

# b) Pie Chart
plt.pie(recruitments, labels=companies, autopct='%1.1f%%')
plt.title("Recruitment Distribution")
plt.show()

# c) Customized Pie Chart
colors = ['red','blue','green','yellow','orange','pink','purple','cyan']
plt.pie(recruitments, labels=companies, colors=colors,
        autopct='%1.1f%%', startangle=90)
plt.title("Customized Pie Chart")
plt.show()

# d) Doughnut Chart
plt.pie(recruitments, labels=companies, autopct='%1.1f%%')
circle = plt.Circle((0,0), 0.7, color='white')
plt.gca().add_artist(circle)
plt.title("Doughnut Chart")
plt.show()

# e) Comparison IBM & Amdocs
compare_companies = ["IBM", "Amdocs"]
compare_values = [90, 80]

plt.bar(compare_companies, compare_values, color=['blue','green'])
plt.title("IBM vs Amdocs Recruitment")
plt.ylabel("Students")
plt.show()