import numpy as np

import datastructures

v1, v2, M = datastructures.define_structures()

cross = datastructures.cross_product(v1,v2)
print(cross)

vector_X_matrix = datastructures.vector_X_matrix(v1, M)
print(vector_X_matrix)
print(np.dot(v1, M))
print(np.dot(M, v1))
