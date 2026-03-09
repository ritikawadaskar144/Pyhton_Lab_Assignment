# Program to convert file content into uppercase

# open source file
f1 = open("inputP8.txt", "r")

# read content
data = f1.read()

# convert to uppercase
upper_data = data.upper()

# open new file to write
f2 = open("output.txt", "w")

# write uppercase data
f2.write(upper_data)

# close files
f1.close()
f2.close()

print("File converted to uppercase successfully!")