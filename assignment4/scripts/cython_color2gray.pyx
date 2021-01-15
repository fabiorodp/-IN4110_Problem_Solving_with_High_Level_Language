# UiO: IN4110
# Assignment 4
# Task 4.1
# Author: Fábio Rodrigues Pereira
# E-mail: fabior@uio.no


import numpy as np
cimport numpy


cpdef numpy.ndarray[numpy.int8_t, ndim=3] cython_color2gray(n_array_image):
    """
    Convert an unsigned ndarray BGR image to an int8 ndarray
    gray-scale image, using different weights.

    weights = {Blue: 0.07, Green: 0.72, Red: 0.21}

    :param n_array_image: An unsigned ndarray BGR image

    :return: An int8 ndarray BGR gray-scale image
    """
    # weights
    grayscale_matrix = np.array([[0.21, 0.72, 0.07],
                                 [0.21, 0.72, 0.07],
                                 [0.21, 0.72, 0.07]])

    # creating n-array to store the new image
    grayscale_image = np.empty(np.shape(n_array_image))

    cpdef int x, y, z, i, h, w, c
    cpdef double w_avg

    h, w, c = np.shape(grayscale_image)

    # calculating the w_avg and setting up the grayscale image
    for x in range(h):           # 400
        for y in range(w):       # 600
            for z in range(c):   # 3

                w_avg = 0
                for i in range(c):

                    w_avg += n_array_image[x, y, i] *\
                             grayscale_matrix[z][i]

                grayscale_image[x, y, z] = w_avg

    # converting results to int
    grayscale_image = grayscale_image.astype("uint8")

    return grayscale_image
