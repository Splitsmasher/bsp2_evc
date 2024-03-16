import numpy as np
import scipy.ndimage
from PIL import Image

import utils


def read_img(inp: str) -> Image.Image:
    """
        Returns a PIL Image given by its input path.
    """
    img = Image.open(inp)
    return img


def convert(img: Image.Image) -> np.ndarray:
    """
        Converts a PIL image [0,255] to a numpy array [0,1].
    """
    ### STUDENT CODE

    array = np.array(img)
    out = array.astype(np.float32) / 255

    ### END STUDENT CODE
    return out


def switch_channels(img: np.ndarray) -> np.ndarray:
    """
        Swaps the red and green channel of a RGB image given by a numpy array.
    """
    ### STUDENT CODE

    for line in range(len(img)):
        for pixel in range(len(img[line])):
            red = img[line][pixel][0]
            green = img[line][pixel][1]

            img[line][pixel][1] = red
            img[line][pixel][0] = green

    out = np.array(img)

    ### END STUDENT CODE

    return out


def image_mark_green(img: np.ndarray) -> np.ndarray:
    """
        returns a numpy-array (HxW) with 1 where the green channel of the input image is greater or equal than 0.7, otherwise zero.
    """
    ### STUDENT CODE

    lo = 0.7

    green = img[:, :, 1]

    mask = np.where(green > lo, 1, 0)

    ### END STUDENT CODE

    return mask


def image_masked(img: np.ndarray, mask: np.ndarray) -> np.ndarray:
    """
        sets the pixels of the input image to zero where the mask is 1.
    """
    ### STUDENT CODE

    out =

    ### END STUDENT CODE

    return out


def grayscale(img: np.ndarray) -> np.ndarray:
    """
        Returns a grayscale image of the input. Use utils.rgb2gray().
    """
    ### STUDENT CODE
    # TODO: Implement this function.

    # NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    out = np.zeros(img.shape)

    ### END STUDENT CODE

    return out


def cut_and_reshape(img_gray: np.ndarray) -> np.ndarray:
    """
        Cuts the image in half (x-dim) and stacks it together in y-dim.
    """
    ### STUDENT CODE
    # TODO: Implement this function.

    # NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    out = np.zeros(img_gray.shape)

    ### END STUDENT CODE

    return out


def filter_image(img: np.ndarray) -> np.ndarray:
    """
        filters the image with the gaussian kernel given below. 
    """
    gaussian = utils.gauss_filter(5, 2)

    ### STUDENT CODE
    # TODO: Implement this function.

    # NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    out = np.zeros(img.shape)

    ### END STUDENT CODE

    return out


def horizontal_edges(img: np.ndarray) -> np.ndarray:
    """
        Defines a sobel kernel to extract horizontal edges and convolves the image with it.
    """
    ### STUDENT CODE
    # TODO: Implement this function.

    # NOTE: The following lines can be removed. They prevent the framework
    #       from crashing.

    out = np.zeros(img.shape)

    ### END STUDENT CODE

    return out
