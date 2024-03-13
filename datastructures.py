from typing import Tuple
import numpy as np


def define_structures() -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
        Defines the two vectors v1 and v2 as well as the matrix M determined by your matriculation number.
    """
    ### STUDENT CODE

    # Matrikelnr: 12333468
    # A=1 B=2 C=3 D=3 E=3 F=4 G=6 H=8

    # D A C
    v1 = np.array([3, 1, 3])

    # F B E
    v2 = np.array([4, 2, 3])

    # [D B C][B G A][E H F]
    M = np.array([[3, 2, 3], [2, 6, 1], [3, 8, 4]])

    ### END STUDENT CODE

    return v1, v2, M


def sequence(M: np.ndarray) -> np.ndarray:
    """
        Defines a vector given by the minimum and maximum digit of your matriculation number. Step size = 0.25.
    """
    ### STUDENT CODE

    min = np.min(M)
    max = np.max(M)

    result = np.arange(min, (max + 0.25), 0.25)

    ### END STUDENT CODE

    return result


def matrix(M: np.ndarray) -> np.ndarray:
    """
        Defines the 15x9 block matrix as described in the task description.
    """
    ### STUDENT CODE

    zeros = np.zeros((3, 3))
    v1 = np.hstack((M, zeros, M))
    v2 = np.hstack((zeros, M, zeros))
    r = np.vstack((v1, v2, v1, v2, v1))

    ### END STUDENT CODE

    return r


def dot_product(v1: np.ndarray, v2: np.ndarray) -> float:
    """
        Dot product of v1 and v2.
    """
    ### STUDENT CODE

    r = 0
    if len(v1) == len(v2):
        for i in range(len(v1)):
            r += v1[i] * v2[i]

    ### END STUDENT CODE

    return r


def cross_product(v1: np.ndarray, v2: np.ndarray) -> np.ndarray:
    """
        Cross product of v1 and v2.
    """
    ### STUDENT CODE

    """
     I wanted to do a Version that works on Vectors of any length and not just on 3D vectors
     I don't know if i needed to do this or if the hardcoded version for 3 Dimensions would have been enough 
     also i tried to comment my work
    """
    r = []

    # Both Vectors need to have the same length
    if len(v1) == len(v2):
        # If the vector is 3 long we need a 3 long output
        for i in range(len(v1)):
            # Getting the Upper Index of this Part of the Crossproduct
            if i + 1 <= len(v1) - 1:
                indexUp = i + 1
            else:
                indexUp = i + 1 - len(v1)
            # Getting the Lower Index of this Part of the Crossproduct
            if indexUp + 1 <= len(v1) - 1:
                indexDown = indexUp + 1
            else:
                indexDown = indexUp + 1 - len(v1)

            # Adding this part of the Crossproduct
            r.append(v1[indexUp] * v2[indexDown] - v1[indexDown] * v2[indexUp])

            print(np.cross(v1, v2))

    ### END STUDENT CODE

    return r


def vector_X_matrix(v: np.ndarray, M: np.ndarray) -> np.ndarray:
    """
        Defines the vector-matrix multiplication v*M.
    """
    ### STUDENT CODE
    # TODO: Implement this function.

    # NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.
    r = np.zeros((v.shape[0], M.shape[1]))
    ### END STUDENT CODE

    return r


def matrix_X_vector(M: np.ndarray, v: np.ndarray) -> np.ndarray:
    """
        Defines the matrix-vector multiplication M*v.
    """
    ### STUDENT CODE
    # TODO: Implement this function.

    # NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.
    r = np.zeros((M.shape[0], v.shape[0]))
    ### END STUDENT CODE

    return r


def matrix_X_matrix(M1: np.ndarray, M2: np.ndarray) -> np.ndarray:
    """
        Defines the matrix multiplication M1*M2.
    """
    ### STUDENT CODE
    # TODO: Implement this function.

    # NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.
    r = np.zeros((M1.shape[0], M2.shape[1]))
    ### END STUDENT CODE

    return r


def matrix_Xc_matrix(M1: np.ndarray, M2: np.ndarray) -> np.ndarray:
    """
        Defines the element-wise matrix multiplication M1*M2 (Hadamard Product).
    """
    ### STUDENT CODE
    # TODO: Implement this function.

    # NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.
    r = np.zeros(M1.shape)
    ### END STUDENT CODE

    return r
