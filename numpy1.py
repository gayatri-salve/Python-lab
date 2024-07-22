#1. Write a NumPy program to create an array of 10 zeros, 10 ones, and 10 fives
# Importing the NumPy library with an alias 'np'
import numpy as np

# Creating an array of 10 zeros using np.zeros()
array = np.zeros(10)

# Printing a message indicating an array of 10 zeros
print("An array of 10 zeros:")

# Printing the array of 10 zeros
print(array)

# Creating an array of 10 ones using np.ones()
array = np.ones(10)

# Printing a message indicating an array of 10 ones
print("An array of 10 ones:")

# Printing the array of 10 ones
print(array)

# Creating an array of 10 fives by multiplying an array of 10 ones by 5
array = np.ones(10) * 5

# Printing a message indicating an array of 10 fives
print("An array of 10 fives:")

# Printing the array of 10 fives
print(array)

#Output:

#An array of 10 zeros:
#[ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
#An array of 10 ones:
#[ 1.  1.  1.  1.  1.  1.  1.  1.  1.  1.]
#An array of 10 fives:
#[ 5.  5.  5.  5.  5.  5.  5.  5.  5.  5.] 
