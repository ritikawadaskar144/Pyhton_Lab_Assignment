#Practical-5 Lab Assignment
#TASK-1

# Taking input from user
# numbers = input("Enter a series of integers separated by space: ")
#
# num_list = numbers.split()
# num_tuple = tuple(int(x) for x in num_list)
#
# print("Total number of items in the tuple:", len(num_tuple))
#
# print("Last item in the tuple:", num_tuple[-1])
#
# print("Tuple in reverse order:", num_tuple[::-1])
#
# if 5 in num_tuple:
#     print("Yes, 5 is present in the tuple.")
# else:
#     print("No, 5 is not present in the tuple.")
#
# if len(num_tuple) > 2:
#     new_tuple = num_tuple[1:-1]   # removing first and last
#     sorted_tuple = tuple(sorted(new_tuple))
#     print("Sorted tuple after removing first and last elements:", sorted_tuple)
# else:
#     print("Not enough elements to remove first and last.")

#TASK-2


prices = input("Enter the prices of sold items separated by space: ")
price_list = prices.split()
price_tuple = tuple(float(x) for x in price_list)

print("Total number of items sold:", len(price_tuple))

print("Cheapest item price:", min(price_tuple))

max_price = max(price_tuple)
print("Costliest item price:", max_price)

sorted_prices = tuple(sorted(price_tuple))
print("Prices in ascending order:", sorted_prices)

count_max = price_tuple.count(max_price)
print("Number of costliest items sold:", count_max)


