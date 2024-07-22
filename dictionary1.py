# Given dictionary
test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4}

# Calculate the sum of values
total = 0
for value in test_dict.values():
    total += value

# Calculate the mean
mean = total / len(test_dict)

# Print the result
print("The mean of the values in the dictionary is:", mean)


#output
#The mean of the values in the dictionary is: 6.2
