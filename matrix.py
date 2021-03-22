"""import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[3, -1], [0, 2]])
С = A.dot(B)	# умножение двух матриц
#C = A + B      # сложение соответствующих элементов
print(C)
#print(A.transpose()) # транспонированая матрица
_________________________________________________________________

# creating a 2X2 Numpy matrix 
n_array = np.array([[50, 29], [30, 44]]) 
  
# Displaying the Matrix 
print("Numpy Matrix is:") 
print(n_array) 
  
# calculating the determinant of matrix 
det = np.linalg.det(n_array) 
  
print("\nDeterminant of given 2X2 matrix:") 
print(int(det)) 
____________________________________________________________________

# creating a 3X3 Numpy matrix 
n_array = np.array([[55, 25, 15], 
                    [30, 44, 2], 
                    [11, 45, 77]]) 
  
# Displaying the Matrix 
print("Numpy Matrix is:") 
print(n_array) 
  
# calculating the determinant of matrix 
det = np.linalg.det(n_array) 
  
print("\nDeterminant of given 3X3 square matrix:") 
print(int(det)) 
_____________________________________________________________________
"""
import numpy as np # inverse of a matrix 
from fractions import Fraction as frac 

A = np.array(([2,-17,11], [-1,11,-7], [0,3,-2]))
A_inv = np.linalg.inv(A)

print(A_inv)