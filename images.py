import numpy as np
import scipy.ndimage
from PIL import Image
from scipy.ndimage import correlate

import datastructures
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

    ### END STUDENT CODE

    return mask


def image_masked(img: np.ndarray, mask: np.ndarray) -> np.ndarray:
    """
        sets the pixels of the input image to zero where the mask is 1.
    """
    ### STUDENT CODE

    out = np.copy(img)

    out[mask == 1] = [1., 1., 1.]

    ### END STUDENT CODE

    return out


def grayscale(img: np.ndarray) -> np.ndarray:
    """
        Returns a grayscale image of the input. Use utils.rgb2gray().
    """
    ### STUDENT CODE

    out = np.copy(img)

    out = utils.rgb2gray(out)

    ### END STUDENT CODE

    return out


def cut_and_reshape(img_gray: np.ndarray) -> np.ndarray:
    """
        Cuts the image in half (x-dim) and stacks it together in y-dim.
    """
    ### STUDENT CODE

    temp = np.hsplit(img_gray, [int(img_gray.shape[0] / 2)])
    out = np.vstack((temp[1], temp[0]))

    ### END STUDENT CODE

    return out


def filter_image(img: np.ndarray) -> np.ndarray:
    """
        filters the image with the gaussian kernel given below. 
    """
    gaussian = utils.gauss_filter(5, 2)

    ### STUDENT CODE

    imgWithPadding = np.pad(img, ((2, 2), (2, 2), (0, 0)))

    newImg = []
    for row in range(len(imgWithPadding) - 4):
        newRow = []
        for pixel in range(len(imgWithPadding[row]) - 4):
            newPixel = []
            for color in range(len(imgWithPadding[row][pixel])):
                newMatrix = []
                for i in range(len(gaussian)):
                    newMatrixLine = []
                    for j in range(len(gaussian[0])):
                        newMatrixLine.append(imgWithPadding[row + i][pixel + j][color])
                    newMatrix.append(newMatrixLine)
                hardamanProdukt = datastructures.matrix_Xc_matrix(np.array(newMatrix), gaussian)
                sum = 0
                for i in range(len(hardamanProdukt)):
                    for j in range(len(hardamanProdukt[0])):
                        sum += hardamanProdukt[i][j]
                newPixel.append(sum)
            newRow.append(newPixel)
        newImg.append(newRow)

    out = np.array(newImg)

    ### END STUDENT CODE

    return out


def horizontal_edges(img: np.ndarray) -> np.ndarray:
    """
        Defines a sobel kernel to extract horizontal edges and convolves the image with it.
    """
    ### STUDENT CODE

    gHorizontal = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

    out = scipy.ndimage.correlate(img, gHorizontal,  mode='constant', cval=0.0)

    ### END STUDENT CODE

    return out
