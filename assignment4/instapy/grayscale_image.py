# UiO: IN4110
# Assignment 4
# Task 4.3
# Author: Fabio Rodrigues Pereira
# E-mail: fabior@uio.no


import numpy as np
from numba import jit
from instapy.filters import Filters


class GrayScaleImage(Filters):

    def __init__(self, input_filename, output_filename=None):
        super().__init__(input_filename, output_filename)

    def run(self, implementation, plot=False, scale_factor=1.0):

        image = self._import()

        if (scale_factor > 0.0) and (scale_factor < 1.0):
            image = self.scale(image, scale_factor)

        elif scale_factor == 1.0:
            pass

        else:
            raise ValueError('Error: Scale factor can only '
                             'be 0 < factor <= 1')

        weights = np.array([[0.21, 0.72, 0.07],
                            [0.21, 0.72, 0.07],
                            [0.21, 0.72, 0.07]])

        new_image = None

        if implementation == "python":
            new_image = self.python_color2gray(image, weights)

        elif implementation == "numpy":
            new_image = self.numpy_color2gray(image, weights)

        elif implementation == "numba":
            new_image = self.numba_color2gray(image, weights)

        # # # Unable because of a lot of bugs
        # elif implementation == "cython":
        #     new_image = cython_color2gray(image)

        else:
            ValueError("Implementation not correct")

        if plot is not None:
            self._plot(new_image)

        if self.output_filename is not False:
            self._export(new_image)

        return new_image

    @staticmethod
    def python_color2gray(image, weights):
        """
        Convert an unsigned ndarray BGR image to an int8 ndarray
        gray-scale image, using different weights and pure python.

        weights = {Blue: 0.07, Green: 0.72, Red: 0.21}

        :param n_array_image: An unsigned ndarray BGR image

        :return: An int8 ndarray BGR gray-scale image
        """
        # creating n-array to store the new image
        new_image = np.empty(np.shape(image))

        # getting lengths for height, width and channel
        h, w, c = np.shape(image)

        # calculating the w_avg and setting up the grayscale image
        for x in range(h):  # 400
            for y in range(w):  # 600
                for z in range(c):  # 3

                    w_avg = 0
                    for i in range(c):
                        w_avg += image[x, y, i] * \
                                 weights[z][i]

                    new_image[x, y, z] = w_avg

        # converting results to int
        new_image = new_image.astype("uint8")

        return new_image

    @staticmethod
    def numpy_color2gray(image, weights):
        """
        Convert an unsigned ndarray BGR image to an int8 ndarray
        gray-scale image, using different weights and numpy.

        weights = {Blue: 0.07, Green: 0.72, Red: 0.21}

        :param n_array_image: An unsigned ndarray BGR image

        :return: An int8 ndarray BGR gray-scale image
        """
        # mapping dot multiplication between channel and weights
        # laying the gray-scale values in a n-array image matrix
        new_image = image @ weights.T

        # converting elements to uint8
        new_image = new_image.astype("uint8")

        return new_image

    def numba_color2gray(self, image, weights):
        """
        Convert an unsigned ndarray BGR image to an int8 ndarray
        gray-scale image, using different weights and numba.

        weights = {Blue: 0.07, Green: 0.72, Red: 0.21}

        :param n_array_image: An unsigned ndarray BGR image

        :return: An int8 ndarray BGR gray-scale image
        """
        # creating n-array to store the new image
        new_image = np.empty(np.shape(image))

        new_image = self._use_numba(image, weights, new_image)

        # converting results to int
        new_image = new_image.astype("uint8")

        return new_image

    @staticmethod
    @jit
    def _use_numba(image, weights, new_image):
        """
        Isolating the for loop to be able to use numba and increase
        performance.
        """
        # getting lengths for height, width and channel
        h, w, c = np.shape(image)

        for x in range(h):  # 400
            for y in range(w):  # 600
                for z in range(c):  # 3

                    w_avg = 0
                    for i in range(c):
                        w_avg += image[x, y, i] * \
                                 weights[z][i]

                    new_image[x, y, z] = w_avg

        return new_image
