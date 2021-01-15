# UiO: IN4110
# Assignment 4
# Task 4.3
# Author: Fabio Rodrigues Pereira
# E-mail: fabior@uio.no


import numpy as np
from numba import jit
from instapy.filters import Filters


class SepiaScaleImage(Filters):

    def __init__(self, input_filename, output_filename=None):
        super().__init__(input_filename, output_filename)

    def run(self, implementation, plot=False,
            scale_factor=1.0, sepia_power=1.0):

        image = self._import()

        if (scale_factor > 0.0) and (scale_factor < 1.0):
            image = self.scale(image, scale_factor)

        elif scale_factor == 1.0:
            pass

        else:
            raise ValueError('Error: Scale factor can only '
                             'be 0 < factor <= 1')

        weights = np.array([[0.131, 0.534, 0.272],
                            [0.168, 0.686, 0.349],
                            [0.189, 0.769, 0.393]])

        if (sepia_power > 0.0) and (sepia_power <= 1.0):
            weights *= sepia_power

        else:
            raise ValueError('Error: Sepia power can only '
                             'be 0 < power <= 1')

        new_image = None

        if implementation == "python":
            new_image = self.python_color2sepia(image, weights)

        elif implementation == "numpy":
            new_image = self.numpy_color2sepia(image, weights)

        elif implementation == "numba":
            new_image = self.numba_color2sepia(image, weights)

        # # # Unable because of a lot of bugs
        # elif implementation == "cython":
        #     new_image = cython_color2sepia(image)

        else:
            ValueError("Implementation not correct")

        if plot is not False:
            self._plot(new_image)

        if self.output_filename is not None:
            self._export(new_image)

        return new_image

    @staticmethod
    def python_color2sepia(image, weights):
        """
        Convert an unsigned ndarray BGR image to an int8 ndarray
        sepia-scale image, using different weights and pure python.

        weights:

            sepia_matrix = [[0.131, 0.534, 0.272],
                            [0.168, 0.686, 0.349],
                            [0.189, 0.769, 0.393]]

        :param n_array_image: An unsigned ndarray BGR image

        :return: An int8 ndarray BGR sepia-scale image
        """
        new_image = np.empty(np.shape(image))

        # getting lengths for height, width and channel
        h, w, c = np.shape(image)

        for x in range(h):          # 400
            for y in range(w):      # 600
                for z in range(c):  # 3

                    w_avg = 0
                    for i in range(c):
                        w_avg += image[x, y, i] * \
                                 weights[z][i]

                    if w_avg >= 255:
                        w_avg = 255

                    new_image[x, y, z] = w_avg

        # converting results to int
        new_image = new_image.astype("uint8")

        return new_image

    @staticmethod
    def numpy_color2sepia(image, weights):
        """
        Convert an unsigned ndarray BGR image to an int8 ndarray
        sepia-scale image, using different weights and numpy.

        weights:

            sepia_matrix = [[0.131, 0.534, 0.272],
                            [0.168, 0.686, 0.349],
                            [0.189, 0.769, 0.393]]

        :param n_array_image: An unsigned ndarray BGR image

        :return: An int8 ndarray BGR sepia-scale image
        """
        new_image = image @ weights.T

        new_image[new_image > 255] = 255

        new_image = new_image.astype("uint8")

        return new_image

    @jit
    def numba_color2sepia(self, image, weights):
        """
        Convert an unsigned ndarray BGR image to an int8 ndarray
        sepia-scale image, using different weights and numba.

        weights:

            sepia_matrix = [[0.131, 0.534, 0.272],
                            [0.168, 0.686, 0.349],
                            [0.189, 0.769, 0.393]]

        :param n_array_image: An unsigned ndarray BGR image

        :return: An int8 ndarray BGR sepia-scale image
        """
        new_image = np.empty(np.shape(image))

        # getting lengths for height, width and channel
        h, w, c = np.shape(image)

        for x in range(h):          # 400
            for y in range(w):      # 600
                for z in range(c):  # 3

                    w_avg = 0
                    for i in range(c):
                        w_avg += image[x, y, i] * \
                                 weights[z][i]

                    if w_avg >= 255:
                        w_avg = 255

                    new_image[x, y, z] = w_avg

        # converting results to int
        new_image = new_image.astype("uint8")

        return new_image
