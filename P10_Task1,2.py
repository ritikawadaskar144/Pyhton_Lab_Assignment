#Assingment 1

import pandas as pd

df = pd.read_csv("books.csv")

print("Complete Book Report")
print(df)

author = input("Enter author name: ")
print(df[df['Author'] == author])

publisher = input("Enter publisher name: ")
print(df[df['Publisher'] == publisher])

cheap = df.loc[df['Price'].idxmin()]
costly = df.loc[df['Price'].idxmax()]

print("Cheapest Book:", cheap['Title'])
print("Costliest Book:", costly['Title'])

sorted_books = df.sort_values(by='Year')
print(sorted_books)


#Assignment 2

import pandas as pd
data = {
    "State": ["Maharashtra", "Gujarat", "Karnataka", "Tamil Nadu", "Rajasthan"],
    "Area": [307713, 196244, 191791, 130058, 342239],  # in sq km
    "Population": [124000000, 70000000, 68000000, 75000000, 81000000]
}
df = pd.DataFrame(data)
print("\nState Information:\n")
print(df)
largest_area = df.loc[df['Area'].idxmax()]
print("\nState with Largest Area:")
print(largest_area['State'])
largest_pop = df.loc[df['Population'].idxmax()]
print("\nState with Largest Population:")
print(largest_pop['State'])
df['Density'] = df['Population'] / df['Area']
print("\nPopulation Density of States:\n")
print(df[['State', 'Density']])
highest_density = df.loc[df['Density'].idxmax()]
print("\nState with Highest Population Density:")
print(highest_density['State'])

