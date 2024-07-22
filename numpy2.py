#Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.
# Importing the NumPy library with an alias 'np'
import numpy as np

# Creating a NumPy array 'x' using arange() from 2 to 11 and reshaping it into a 3x3 matrix
x = np.arange(2, 11).reshape(3, 3)

# Printing the resulting 3x3 matrix 'x'
print(x)


#Output:

[[ 2  3  4]                                                             
 [ 5  6  7]                                                             
 [ 8  9 10]]
