import numpy as np

import datastructures
import triangles

"""
#TESTS Für Datastruktures:

import datastructures

v1, v2, M = datastructures.define_structures()

cross = datastructures.cross_product(v1, v2)
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

matrix_Xc_matrix = datastructures.matrix_Xc_matrix(M, M.transpose())
print(M)
print(M.transpose())
print(matrix_Xc_matrix)
print(np.multiply(M, M.transpose()))

print("-------------------------------------------")
print("Weird Test cases:")

M2 = np.array([[0, 1, 2], [3, 4, 5]])

#print(np.dot(M2, v1))
#print(datastructures.matrix_X_vector(M2, v1))
#print(np.dot(v1, M2))
#datastructures.vector_X_matrix(v1, M2)
#print(np.dot(M2, M))
#print(datastructures.matrix_X_matrix(M2, M))
#print(np.multiply(M, M2))
#datastructures.matrix_Xc_matrix(M, M2)
"""

P1, P2, P3 = triangles.define_triangle()
print(P1, P2, P3)
P1P2, P2P3, P3P1 = triangles.define_triangle_vertices(P1, P2, P3)
print(P1P2, P2P3, P3P1)
lengths = triangles.compute_lengths(P1P2, P2P3, P3P1)
print(lengths)
n, n_norm = triangles.compute_normal_vector(P1P2, P2P3, P3P1)
print(n, n_norm)
area = triangles.compute_triangle_area(n)
print(area)
alpha, beta, gamma = triangles.compute_angles(P1P2, P2P3, P3P1)
print(alpha, beta, gamma)

