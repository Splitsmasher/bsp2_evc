from typing import List, Tuple

import numpy as np

def define_triangle() -> Tuple[np.ndarray, np.ndarray, np.ndarray]:

    ### STUDENT CODE

    A = 1
    B = 2
    C = 3
    D = 3
    E = 3
    F = 4
    G = 6
    H = 8

    P1 = np.array([(1 + C), -(1 + A), -(1 + E)])
    P2 = np.array([-(1 + G), -(1 + B), (1 + H)])
    P3 = np.array([-(1 + D), (1 + F), -(1 + B)])

    ### END STUDENT CODE

    return P1, P2, P3

def define_triangle_vertices(P1:np.ndarray, P2:np.ndarray, P3:np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    ### STUDENT CODE
    # TODO: Implement this function.

	# NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    P1P2 = np.zeros(3)
    P2P3 = np.zeros(3)
    P3P1 = np.zeros(3)
    ### END STUDENT CODE

    return P1P2, P2P3, P3P1

def compute_lengths(P1P2:np.ndarray, P2P3:np.ndarray, P3P1:np.ndarray) -> List[float]:
    ### STUDENT CODE
    # TODO: Implement this function.

	# NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    norms = [0., 0., 0.]
    ### END STUDENT CODE

    return norms

def compute_normal_vector(P1P2:np.ndarray, P2P3:np.ndarray, P3P1:np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    ### STUDENT CODE
    # TODO: Implement this function.

	# NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    n = np.zeros(3)
    n_normalized = np.zeros(3)
    ### END STUDENT CODE

    return n, n_normalized

def compute_triangle_area(n:np.ndarray) -> float:
    ### STUDENT CODE
    # TODO: Implement this function.

	# NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    area = 0
    ### END STUDENT CODE

    return area

def compute_angles(P1P2:np.ndarray,P2P3:np.ndarray,P3P1:np.ndarray) -> Tuple[float, float, float]:
    ### STUDENT CODE
    # TODO: Implement this function.

	# NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    alpha, beta, gamma = 0., 0., 0.
    ### END STUDENT CODE

    return alpha, beta, gamma

