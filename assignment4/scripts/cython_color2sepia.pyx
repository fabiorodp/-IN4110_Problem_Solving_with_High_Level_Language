# UiO: IN4110
# Assignment 4
# Task 4.2
# Author: Fábio Rodrigues Pereira
# E-mail: fabior@uio.no


import numpy as np
cimport numpy


cpdef numpy.ndarray[numpy.int8_t, ndim=3] cython_color2sepia(n_array_image):
    """
    Convert an unsigned ndarray BGR image to an int8 ndarray
    sepia-scale image, using different weights.

    weights:

        sepia_matrix = [[0.131, 0.534, 0.272],
                        [0.168, 0.686, 0.349],
                        [0.189, 0.769, 0.393]]

    :param n_array_image: An unsigned ndarray BGR image

    :return: An int8 ndarray BGR sepia-scale image
    """
    # weights
    sepia_matrix = np.array([[0.131, 0.534, 0.272],
                             [0.168, 0.686, 0.349],     # BGR
                             [0.189, 0.769, 0.393]])

    # creating n-array to store the new image
    sepia_image = np.empty(np.shape(n_array_image))

    cpdef int x, y, z, i, h, w, c
    cpdef double w_avg

    h, w, c = np.shape(sepia_image)

    # calculating the w_avg and setting up the sepia-scale image
    for x in range(h):               # 400
        for y in range(w):           # 600
            for z in range(c):       # 3

                w_avg = 0
                for i in range(c):

                    w_avg += n_array_image[x, y, i] * \
                             sepia_matrix[z][i]

                if w_avg >= 255:
                    w_avg = 255

                sepia_image[x, y, z] = w_avg

    # converting results to int
    sepia_image = sepia_image.astype("uint8")

    return sepia_image
