import cv2
import numpy as np
import scipy.ndimage
from PIL import Image
from pygments.formatters import img

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

    newImg = np.copy(img)

    for line in range(len(newImg)):
        for pixel in range(len(newImg[line])):
            red = newImg[line][pixel][0]
            green = newImg[line][pixel][1]

            newImg[line][pixel][1] = red
            newImg[line][pixel][0] = green

    out = np.array(newImg)

    ### END STUDENT CODE

    return out


def image_mark_green(img: np.ndarray) -> np.ndarray:
    """
        returns a numpy-array (HxW) with 1 where the green channel of the input image is greater or equal than 0.7, otherwise zero.
    """
    ### STUDENT CODE
    lo = 0.7

    green = img[:, :, 1]

    mask = np.where(green >= lo, 1, 0)

    #mask =  np.all(img[:, :, :1] >= lo, axis=-1)

    ### END STUDENT CODE

    return mask


def image_masked(img: np.ndarray, mask: np.ndarray) -> np.ndarray:
    """
        sets the pixels of the input image to zero where the mask is 1.
    """
    ### STUDENT CODE

    temp = np.copy(img)

    temp[mask == 1] = [1., 1., 1.]

    out = np.copy(temp)

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
