import numpy as np

import datastructures

v1, v2, M = datastructures.define_structures()

cross = datastructures.cross_product(v1,v2)
print(cross)

vector_X_matrix = datastructures.vector_X_matrix(v1, M)
print(vector_X_matrix)
print(np.dot(v1, M))

matrix_X_vector = datastructures.matrix_X_vector(M, v1)
print(matrix_X_vector)
print(np.dot(M, v1))

matrix_X_matrix = datastructures.matrix_X_matrix(M, M.transpose())
print(matrix_X_matrix)
print(np.dot(M, M.transpose()))
