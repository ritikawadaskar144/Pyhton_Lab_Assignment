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

