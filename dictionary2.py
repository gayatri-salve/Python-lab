# Sample dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Create a new dictionary by concatenating the given dictionaries
result = {}
for d in (dic1, dic2, dic3):
    result.update(d)

# Print the result
print("The concatenated dictionary is:", result)


#output
#The concatenated dictionary is: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
