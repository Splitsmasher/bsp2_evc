from typing import List

import numpy as np
import matplotlib.pyplot as plt

import datastructures


def define_transformations() -> List[np.ndarray]:
    """
        Returns the four transformations t1, .., t4 to transform the quadrat. 
        The transformations are determined by using mscale, mrotate and mtranslate.
    """
    ### STUDENT CODE
    # TODO: Implement this function.

	# NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    t1 = datastructures.matrix_X_matrix(mtranslate(-3, 0), mrotate(55))

    t2 = datastructures.matrix_X_matrix(mrotate(55), mtranslate(-3, 0))

    t3 = mscale(3,2)
    t3 = datastructures.matrix_X_matrix(mrotate(70), t3)
    t3 = datastructures.matrix_X_matrix(mtranslate(3, 1), t3)

    t4 = mrotate(45)
    t4 = datastructures.matrix_X_matrix(mscale(1, 3), t4)

    ### END STUDENT CODE

    return [t1, t2, t3, t4]

def mscale(sx : float, sy : float) -> np.ndarray:
    """
        Defines a scale matrix. The scales are determined by sx in x and sy in y dimension.
    """
    ### STUDENT CODE

    m = np.array([[sx, 0., 0.], [0., sy, 0.], [0., 0., 1.]])

    ### END STUDENT CODE

    return m

def mrotate(angle : float) -> np.ndarray:
    """
        Defines a rotation matrix (z-axis) determined by the angle in degree (!).
    """
    ### STUDENT CODE

    rad = np.deg2rad(angle)

    m = np.array([[np.cos(rad), (np.sin(rad) * -1), 0.], [np.sin(rad), np.cos(rad), 0.], [0., 0., 1.]])


    ### END STUDENT CODE

    return m
    
def mtranslate(tx : float, ty : float) -> np.ndarray:
    """
        Defines a translation matrix. tx in x, ty in y direction.
    """
    ### STUDENT CODE

    m = np.array([[1., 0., tx], [0., 1., ty], [0., 0., 1.]])

    ### END STUDENT CODE

    return m

def transform_vertices(v : np.ndarray, m : np.ndarray) -> np.ndarray:
    """
        transform the (3xN) vertices given by v with the (3x3) transformation matrix determined by m.
    """
    ### STUDENT CODE

    out = datastructures.matrix_X_matrix(m, v)

    ### END STUDENT CODE

    return out

def display_vertices(v : np.ndarray, title : str) -> None:
    """
        Plot the vertices in a matplotlib figure.
    """
    # create the figure and set the title
    plt.figure()
    plt.axis('square')

    plt.title(title)

    # x and y limits
    plt.xlim((-6,6))
    plt.ylim((-6,6))
    plt.xticks(range(-6,6))
    plt.yticks(range(-6,6))

    # plot coordinate axis
    plt.axvline(color='black')
    plt.axhline(color='black')
    plt.grid()
    
    # we just add the last element, so plot can do our job :)
    v_ = np.concatenate((v, v[:, 0].reshape(3,-1)), axis=1)

    plt.plot(v_[0, :], v_[1, :], linewidth=3)
    plt.show()
