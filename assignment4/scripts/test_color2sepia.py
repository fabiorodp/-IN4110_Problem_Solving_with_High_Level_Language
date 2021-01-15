# UiO: IN4110
# Assignment 4
# Task 4.2 - pytest
# Author: Fábio Rodrigues Pereira
# E-mail: fabior@uio.no


from python_color2sepia import python_color2sepia
from numpy_color2sepia import numpy_color2sepia
from numba_color2sepia import numba_color2sepia
import cv2


def test_numpy_color2sepia():
    """Testing if the function makes the correct calculations."""

    image = cv2.imread("pictures/rain.jpg")

    python_sepia_image = python_color2sepia(image)
    numpy_sepia_image = numpy_color2sepia(image)
    numba_sepia_image = numba_color2sepia(image)

    assert python_sepia_image[0, 0, 0] == numpy_sepia_image[0, 0, 0] \
           == numba_sepia_image[0, 0, 0] \
           == int(251*0.131+144*0.534+63*0.272)

    assert python_sepia_image[0, 0, 1] == numpy_sepia_image[0, 0, 1] \
           == numba_sepia_image[0, 0, 1] \
           == int(251*0.168+144*0.686+63*0.349)

    assert python_sepia_image[0, 0, 2] == numpy_sepia_image[0, 0, 2] \
           == numba_sepia_image[0, 0, 2] \
           == int(251*0.189+144*0.769+63*0.393)
