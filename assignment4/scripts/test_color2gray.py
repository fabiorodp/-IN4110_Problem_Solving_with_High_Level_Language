# UiO: IN4110
# Assignment 4
# Task 4.1 - pytest
# Author: Fábio Rodrigues Pereira
# E-mail: fabior@uio.no


from python_color2gray import python_color2gray
from numpy_color2gray import numpy_color2gray
from numba_color2gray import numba_color2gray
import cv2


def test_numpy_color2gray():
    """Testing if the function makes the correct calculations."""

    image = cv2.imread("pictures/rain.jpg")

    python_gray_image = python_color2gray(image)
    numpy_gray_image = numpy_color2gray(image)
    numba_gray_image = numba_color2gray(image)

    assert python_gray_image[0, 0, 0] == numpy_gray_image[0, 0, 0] \
           == numba_gray_image[0, 0, 0] \
           == int(251 * 0.21 + 144 * 0.72 + 63 * 0.07)

    assert python_gray_image[0, 0, 1] == numpy_gray_image[0, 0, 1] \
           == numba_gray_image[0, 0, 1] \
           == int(251 * 0.21 + 144 * 0.72 + 63 * 0.07)

    assert python_gray_image[0, 0, 2] == numpy_gray_image[0, 0, 2] \
           == numba_gray_image[0, 0, 2] \
           == int(251 * 0.21 + 144 * 0.72 + 63 * 0.07)
