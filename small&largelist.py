#Write a Python program to get the largest and smallest number from a list without builtin functions.
# Example list
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Initialize the largest and smallest variables
largest = my_list[0]
smallest = my_list[0]

# Iterate through the list to find the largest and smallest numbers
for number in my_list:
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number

# Print the results
print("The largest number in the list is:", largest)
print("The smallest number in the list is:", smallest)


#output
#The largest number in the list is: 9
#The smallest number in the list is: 1
